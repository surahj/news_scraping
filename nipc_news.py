import requests
from bs4 import BeautifulSoup
import pandas as pd


# Create an empty list to store the data
data = []

#function to Send a GET request to the URL and parse the HTML response with BeautifulSoup
def get_data(url):
  response = requests.get(url)
  soup = BeautifulSoup(response.text, 'html.parser')

  # Find all the news article links on the page
  try:
    article_links = soup.select('.posts-container')[0].find_all('article')
  except:
    article_links = None
    return

  # Loop through the article links and extract the data we want
  for i in range(len(article_links)):
    title = article_links[i].select('.title')[0].getText().strip()
    href = article_links[i].select('.title')[0].a['href']
    publish_date = article_links[i].select('.date')[0].getText().replace('\n', ' ')

    # Append the data to our list
    data.append([title, href, publish_date])

  print(data)
  next_link = None
  try:
    next_link = soup.select('.next')[0].a['href']
  except:
    next_link = None
  if next_link:
    print('next_link is', next_link)
    get_data(next_link)

years = ['2016']
months = ['05','06', '07', '08', '09', '10', '11', '12']

# Loop through the years and months you want to scrape
for year in years:
  for month in months:
    # Create the URL for the current month's news page
    url = f'https://nipc.gov.ng/{year}/{month}/'
    print(url)

    # call the get_data function
    get_data(url)


print(data)
# Convert the data list to a pandas DataFrame
df = pd.DataFrame(data, columns=['Title', 'Link', 'Publish Date'])

# Save the DataFrame to a CSV file
df.to_csv('nipc_news.csv', index=False)
