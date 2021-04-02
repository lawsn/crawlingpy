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

    return BeautifulSoup(response.text, 'html.parser')

# parse
def parse_daum_digital(html):
    titles = html.select('strong.tit_thumb > a')

    title_len = len(titles)
    for i in range(0, title_len):
        if match_word(titles[i].text):
            print(titles[i].text)

# match
words = ['국', '빅']
def match_word(text):
    for word in words:
        if word in text:
            return True
    return False

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
    html = job_crawling()
    parse_daum_digital(html)