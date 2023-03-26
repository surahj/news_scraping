import requests
from bs4 import BeautifulSoup
import pprint

url = 'https://nairametrics.com/'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

news_item_soup = soup.select('.jeg_post_title')

#Top_five news
print("Top five news")
top_five_news = []
top_stories = soup.find(class_='jeg_postblock_22').find_all(class_='jeg_post_title')

for story in top_stories[:5]:
    title = story.a.text.strip()
    url = story.a['href']
    top_five_news.append({'title': title, 'url': url})

pprint.pprint(top_five_news)

# All news
print("All news")
news = []
for index, value in enumerate(news_item_soup):
  title = news_item_soup[index].a.getText()
  url = news_item_soup[index].a['href']

  news.append({'title': title, 'url': url})

pprint.pprint(news)
