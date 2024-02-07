# imports


import requests
import pandas as pd
import json
import psycopg2
from sqlalchemy import create_engine

# 1. get 1000 users

URL = 'https://randomuser.me/api/?results=1000'

r = requests.get(url = URL)
data = r.json()

# 2. convert data to pandas
df = pd.json_normalize(data['results'])

col_types = {'gender':'category', 'nat':'category', 'name.title':'category',
             'location.coordinates.latitude':'float', 'location.coordinates.longitude':'float',
             #"dob.date":"datetime64[ns]", "registered.date":"datetime64[ns]",'registered.date': "datetime64[ns]",
             'dob.age':'int'}
for col in df.columns:
  if col not in col_types:
    col_types[col] = 'string'
df = df.astype(col_types)
df

# 3. query on data
#choosing male over 30


df = df[(df['dob.age']>30) & (df['gender']=='male')]
#df.reset_index(drop=True, inplace=True)
df.head(5)

# 4. hash passwords
df['login.password'] = df['login.password'].apply(hash)


# 4. save to database
url = 'postgresql://postgres:myPassword@localhost:5432/chartbox' 
engine = create_engine(url, echo=True)
df.to_sql('users', engine, if_exists='replace')

