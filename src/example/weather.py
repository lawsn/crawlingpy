import requests
from bs4 import BeautifulSoup

url = 'https://weather.com/weather/tenday/l/'
param = 'b757e0078b0b135DetailsSummary--tempValue--RcZzi0973ea8930d24ef111c7b8457939f4e2046fc8bbe48119f17'
response = requests.get(url + param)

print(response.text)

soup = BeautifulSoup(response.text, 'html.parser')

dateTime = soup.select('h2.DetailsSummary--daypartName--1Mebr')
weather = soup.select('span.DetailsSummary--lowTempValue--1DlJK')

print(weather)

dateTimeLen = len(dateTime)
weatherLen = len(weather)

print(weatherLen)

# for i in range(0, dateTimeLen):
#     # print(dateTime[i].text)
#     print(weather[i])