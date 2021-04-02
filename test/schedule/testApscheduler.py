import time

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.base import JobLookupError

def job():
    print("I'm working........ " + "I [time]")


sched = BackgroundScheduler()
sched.start()

sched.add_job(job, 'interval', seconds=3, id="test_2")

while True:
    print("Running main process....................")
    time.sleep(1)
