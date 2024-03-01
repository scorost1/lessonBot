import requests
import pprint

with open('token.txt') as f:
    token = f.read()

# endpoint = f'https://api.telegram.org/bot{token}/getMe'
# res = requests.get(endpoint).json()
# pprint.pprint(res)

# endpoint = f'https://api.telegram.org/bot{token}/getUpdates'
# param = {'timeout': 60, 'offset': -1}
# response = requests.get(endpoint, params=param).json()['result']
# pprint.pprint(response)

offset = -2
import time
while True:
    endpoint = f'https://api.telegram.org/bot{token}/getUpdates'
    param = {'timeout': 60, 'offset': offset + 1}
    response = requests.get(endpoint, params=param).json()
    if response['result']:
        offset = response['result'][0]['update_id']
        userText = response['result'][0]['message']['text']
        chatID = response['result'][0]['message']['chat']['id']
        pprint.pprint(response)

        endpoint = f'https://api.telegram.org/bot{token}/sendMessage'
        params = {'chat_id': chatID, 'text': userText}
        res = requests.get(endpoint, params=params)
    time.sleep(1)


# usersInfo = dict()
# for i in res:
#     chatID = i['message']['chat']['id']
#     userName = i['message']['chat']['first_name']
#     if 'text' in i['message']:
#         userText = i['message']['text']
#     usersInfo[chatID] = [userName, userText]
# print(usersInfo)
#
# endpoint = f'https://api.telegram.org/bot{token}/sendMessage'
# for user in usersInfo:
#     mes = f'Привет, {usersInfo[user][0]}!'
#     params = {'chat_id': user, 'text': mes}
#     res = requests.get(endpoint, params=params).json()
