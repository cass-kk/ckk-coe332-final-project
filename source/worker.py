from jobs import q, update_job_status, _save_job
import time
import os
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

    with open("/app/pet_data.json", "r") as json_file:
        data_json = json.load(json_file)
    return data_json

    test = get_data()
    jsonList = test['data']

    doggos = [x for x in JsonList if (x[13] == dog)]
    d = dict(doggos)
    bre = d[14]

#    x_values_to_plot = []
#    y_values_to_plot = []

#    for key in raw_data.keys(): #client to the raw data stored in redis
#        if (int(start) <= key['date'] <= int(end)):
#            x_values_to_plot.append(key['interesting_property_1'])
#            y_values_to_plot.append(key['interesting_property_2'])

 #   plt.scatter(x_values_to_plot, y_values_to_plot)
 #   plt.savefig('/output_image.png')


    plt.hist(bre, 10)
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
