import requests
import pprint

with open('token.txt') as f:
    token = f.read()

# endpoint = f'https://api.telegram.org/bot{token}/getMe'
# res = requests.get(endpoint).json()
# pprint.pprint(res)

endpoint = f'https://api.telegram.org/bot{token}/getUpdates'
res = requests.get(endpoint).json()['result']
pprint.pprint(res)

usersInfo = dict()

for i in res:
    chatID = i['message']['chat']['id']
    userName = i['message']['chat']['first_name']
    if 'text' in i['message']:
        userText = i['message']['text']
    usersInfo[chatID] = [userName, userText]
print(usersInfo)

endpoint = f'https://api.telegram.org/bot{token}/sendMessage'
for user in usersInfo:
    mes = f'Привет, {usersInfo[user][0]}!'
    params = {'chat_id': user, 'text': mes}
    res = requests.get(endpoint, params=params).json()
