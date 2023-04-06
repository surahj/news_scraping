from GoogleNews import GoogleNews
import pandas as pd

googlenews = GoogleNews(lang='en')

googlenews.search('Business Nigeria')

#uncomment the line below to get more than 10 result
#googlenews.getpage(2)
# googlenews.getpage(3)
result = googlenews.result()
googlenews.get_texts()
googlenews.set_period('12h')


for article in result:
    for key, value in article.items():
        print(key, ':', value)

df = pd.DataFrame(result, columns=['title', 'link', 'date'])

df.to_csv('today_stories.csv', index=False)
