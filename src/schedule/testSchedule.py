import schedule
import time

def job():
    print("I'm working...")

# schedule.every(10).minutes.do(job)
schedule.every(1).seconds.do(job)


while True:
    schedule.run_pending()
    time.sleep(1)
