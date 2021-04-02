import requests
import bs4

url = "https://www.kobus.co.kr/main.do"
response = requests.get(url)
response.status_code
html = response.text

bsobj = bs4.BeautifulSoup(html, "html.parser")
value_bsobj = bsobj.find('div', {"class":"clfix"})
print(value_bsobj.find("h2").text)
