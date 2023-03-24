import requests
from bs4 import BeautifulSoup
import pprint


news = requests.get('https://nairametrics.com/')
news_soup = BeautifulSoup(news.text, 'html.parser')

news_item_soup = news_soup.select('.jeg_post_title')
# print(news_item_soup[0].a['href'])
print(news_item_soup[0].a.getText())
news_items = []

for index, value in enumerate(news_item_soup):
  title = news_item_soup[index].a.getText()
  url = news_item_soup[index].a['href']

  news_items.append({'title': title, 'url': url})

print("news items ! below")
pprint.pprint(news_items)
