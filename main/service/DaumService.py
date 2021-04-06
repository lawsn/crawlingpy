from datetime import datetime
import requests
from bs4 import BeautifulSoup
import json
import redis
import time
from apscheduler.schedulers.blocking import BlockingScheduler

# call crawler
def crawl():
    url = getUrl()
    bs = getHtml(url)
    articles = bs.select('strong.tit_thumb > a')
    # for article in articles:
    #     print('{} <> {}'.format(article.text, article['href']))

    dicts = list(filter(lambda d: '코인' in d.text, articles))
    datas = {}
    for dict in dicts:
        datas[dict.text] = dict['href']

    if len(datas) > 0:
        save(datas)

# parsing
def getUrl():
    return 'https://news.daum.net/breakingnews/digital{}'.format('')

def getHtml(url):
    return BeautifulSoup(requests.get(url).text, 'html.parser')


# call extractor

# save
rd = redis.StrictRedis(host='localhost', port=6379, db=0)
def save(data):
    # datekey
    now = datetime.now()
    datekey = now.strftime("%Y%m%d_%H%M%S")

    # json dump
    jsonDump = json.dumps(data, ensure_ascii=False).encode("utf-8")
    rd.set(datekey, jsonDump)

sched = BlockingScheduler()
@sched.scheduled_job('interval', minutes=3, id='test_1')
def logic():
    print('run time = ', datetime.now())
    crawl()

if __name__ == '__main__':
    sched.start()
