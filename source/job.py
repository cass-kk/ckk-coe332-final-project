import uuid
from hotqueue import HotQueue
from redis import StrictRedis
import os
import json

redis_ip = os.environ.get('REDIS_IP')

q = HotQueue("queue", host = redis_ip, port = 6379, db=1)
rd = StrictRedis(host = redis_ip, port = 6379, db=0)

def _generate_jid():
    return str(uuid.uuid4())
    
def _generate_job_key(jid):
    return 'job.{}'.format(jid)
    
def _instantiate_job(jid, status, start, end):
    if type(jid) == str:
    return {'id': jid, 'status': status, 'start': start, 'end': end}
    return {'id': jid.decode('utf-8'), 'status': status.decode('utf-8'), 'start': start.decode('utf-8'), 'end': end.decode('utf-8')}
    
def _save_job(job_key, job_dict):
    rd.hmset(job_key, job_dict)
    
def _queue_job(jid):
    q.put(jid)
    
def add_job(start, end, status="submitted"):
    jid = _generate_jid()
    job_dict = _instantiate_job(jid, status, start, end)
    _save_job(_generate_job_key(jid), job_dict)
    _queue_job(jid)
    return job_dict
    
def update_job_status(jid, status):
    jid, status, start, end = rd.hmget(generate_job_key(jid), 'id', 'status', 'start', 'end')
    job = _instantiate_job(jid, status, start, end)
    if job:
        job['status'] = status_save_job(_gnerate_job_key(jid), job)
    else:
        raise Exception()
