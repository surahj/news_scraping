# news_scraping

It exract data from from google news, the data was formatted in title, url and date.

It returns array of object, each object contains title of the news, url to the full news, and date when it was posted 

The results would be saved to an csv file.

## Getting Started

This project makes use of **Python**. To be able to run this project locally, all aforementioned packages must be installed first.


### Installing Dependencies


1. **Virtual Enviornment** - I recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

2. **PIP Dependencies** - Once you have your virtual environment setup and running, install dependencies while in the root directory.
```
pip install -r requirements.txt
```
This will install all of the required packages we selected within the `requirements.txt` file.


### To scrape google news Run the script as below
```
python3 script.py
```

### To scrape nipc.gov.ng website Run the script as below

Edit ```years``` and ```months``` variable in ```nipc_news.py```  to the range of year and months to scrape from.
```
python3 nipc_news.py
```

