import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/sise/'
response = requests.get(url)
doc = response.text

data = BeautifulSoup(doc)

result = data.select_one("#KOSPI_now")

print(result.text)
