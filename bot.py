import requests
import pprint


with open('token.txt') as f:
    token = f.read()
endpoint = f'https://api.telegram.org/bot{token}/getMe'
res = requests.get(endpoint).json()['result']
pprint.pprint(res)