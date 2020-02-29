import psycopg2 as pg
import os
from recommender import recommender

# get heroku database URL
DATABASE_URL = os.environ['DATABASE_URL']

# Postgres connection
sql_conn = pg.connect(DATABASE_URL, sslmode='require')

# create recommender
my_recommender = recommender(sql_conn)