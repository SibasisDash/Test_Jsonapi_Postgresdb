import pandas as pd
import json
import psycopg2
import os

df = pd.read_json("data.json")
df.index.name = "Date"

df_new = pd.json_normalize(df['rates'])
df_new['Date'] = df.index
df_new['EUR'] = 1
df_new = df_new[['Date', 'EUR', 'USD', 'CAD', 'NZD', 'INR', 'JPY', 'GBP']]


conn_cred = {
    'host': 'localhost',
    'port': '5432',
    'dbname': 'mydb',
    'user': 'postgres',
    'password': 'password'
}

conn = psycopg2.connect(**conn_cred)
conn.autocommit = True
cur = conn.cursor()

#save to local disk and copy from csv
# Save the dataframe to disk
tmp_df = "./tmp_dataframe.csv"
df_new.to_csv(tmp_df, index_label='id', header=False)

cur = conn.cursor()
f = open(tmp_df, 'r')
cur.copy_from(f, 'hist_data', sep=",")
conn.commit()

print("copy_from_file() done")
cur.close()






result = df_new.to_json()
parsed = json.loads(result)
with open('data2.json', 'w') as f:
    json.dump(result, f)
