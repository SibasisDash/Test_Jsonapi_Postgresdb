import requests
import json

response = requests.get('https://api.exchangeratesapi.io/history?start_at=2018-01-01&end_at=2020-10-31')

if response:

    data = response.json()
    with open('data.json', 'w') as f:
        json.dump(data, f)
else:
    print("Request returned an error.")

