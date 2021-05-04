from jobs import q, update_job_status, _save_job
import time
import os

@q.worker
def execute_job(jid):
    jobs.update_job_status(jid, 'in progress')
    
    worker_ip = os.environ.get('WORKER_IP')
    job_dict = {'worker ip': worker_ip.decode('utf-8')}
    _save_job(worker_ip, job_dict)
    
    time.sleep(15)
    jobs.update_job_status(jid, 'complete')
    
execute_job()
