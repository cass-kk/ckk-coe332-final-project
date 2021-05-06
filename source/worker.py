from job import q, update_job_status, _save_job
import time
import os
from hotqueue import HotQueue
import redis
import matplotlib.pyplot as plt

ip_redis = os.environ.get('REDIS_IP')

rd = redis.StrictRedis(host=ip_redis, port=6379, db=0)
q = HotQueue('queue', host=ip_redis, port=6379, db=1)

@q.worker
def execute_job(jid):
    jobs.update_job_status(jid, 'in progress')
    
    worker_ip = os.environ.get('WORKER_IP')
    job_dict = {'worker ip': worker_ip.decode('utf-8')}
    _save_job(worker_ip, job_dict)

    time.sleep(15)
    jobs.update_job_status(jid, 'complete')

    data_list = rd.hgetall(job)

    results = []

    for key in data_list(): #client to the raw data stored in redis
        if ((int(start) <= key[12] <= int(end)) and (key[13] == dog)):
            results.append(key[14])

    plt.hist(results, 10)
    plt.show()
    plt.xlabel('Breed Types')
    plt.ylabel('Number of Dogs')
    plt.title('Dog Breeds')    
    plt.savefig('breeds.png')

    with open('/output_image.png', 'rb') as f:
        img = f.read()

    rd.hset(jobid, 'image', img)
    rd.hset(jobid, 'status', 'finished')
   
    return

execute_job()
