import time
from apscheduler.schedulers.background import BackgroundScheduler
import requests
from bs4 import BeautifulSoup


# crawling job
def job_crawling():
    print('start crawling')
    url = 'https://news.daum.net/breakingnews/digital'
    #param = '?page=2'
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    print(soup)

    titles = soup.select('strong.tit_thumb > a')
    title_len = len(titles)
    print(title_len)
    for i in range(0, title_len):
        print(titles[i].text)

# parse
# save at Redis



# scheduler
# sched = BackgroundScheduler()
# sched.start()
#
# sched.add_job(job_crawling, 'interval', seconds=10, id="test_2")
#
# while True:
#     time.sleep(1)

if __name__ == '__main__':
    job_crawling()