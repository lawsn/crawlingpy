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
    articles = bs.select('h3.tit > a')
    # for article in articles:
    #     print('{} <> {}'.format(article.text, article['href']))

    # print(articles)

    dicts = list(filter(lambda d: '삼성' in d.text, articles))
    datas = {}
    for dict in dicts:
        datas[dict.text] = 'https:' + dict['href']

    print(datas)

    if len(datas) > 0:
        save(datas)

# parsing
def getUrl():
    return 'https://www.hankyung.com/finance/01{}'.format('')

def getHtml(url):
    # r = requests.get(url)
    # return BeautifulSoup(r.content.decode('euc-kr', 'replace'), 'html.parser')
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
    # sched.start()
    crawl()
