import json

import requests

url = 'http://0.0.0.0:8080/predict'
data = {'sentence': 'i am very bored and this api is bad'}
response = requests.post(url, data=json.dumps(data))
print(response.json())
