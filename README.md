# Joe Rogan Podcast Recommender

Topic modelling on JRE podcast transcripts and recommendations made with cosine similiarity. Project deployed on heroku at [https://jre-recommender.herokuapp.com/](https://jre-recommender.herokuapp.com/).

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

BeautifulSoup
pymongo
sklearn
pandas
nltk
SpaCy
gensim
sqlalchemy
psycopg2

## Downloading the data

The data is on podgist and podscribe. Check their `robots.txt`, at the time of my scraping, it was not banned. Scraping is in [01_scrape_transcripts](01_scrape_transcripts.ipynb).

## Credentials file

Set up your credentials in new file named cred.py in [credentials](credentials) in the form:
```
mongo_user = 'your username'
mongo_pass = 'your password'
mongo_host = 'your server:port number'
mongo_auth_db = 'authorizing DB for your user'
sql_host = 'your postgres server'
sql_port = your posgres port
sql_user = 'postgres username'
sql_pass = 'postgres password'
heroku_DB = 'postgres DB from heroku, take a look at your heroku settings'
```

## Data Cleaning

Data is cleaned from a MongoDB database in [02_clean_transcripts](02_clean_transcripts.ipynb).

## Topic Modelling

Topics are modelled in [04_topic_modelling](04_topic_modelling).


## Authors

* **Eric Bassett** - *Initial work* - [github](https://github.com/ericbassett)

