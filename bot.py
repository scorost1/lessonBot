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

def givePhoto(date: str) -> (str, str):
    endpoint = 'https://api.nasa.gov/planetary/apod'
    params = {'api_key': 'DEMO_KEY', 'date': date}
    res = requests.get(endpoint, params=params).json()
    explanation = res['explanation']
    urlPhoto = res['url']
    return (urlPhoto, explanation)



# def numDay(month):
#     if month == '2' and int(year) % 4 == 0 and int(year) % 100 != 0 or int(year) % 400 == 0:
#         return '29'
#     elif month == '2' and int(year) % 4 != 0 and int(year) % 100 == 0 or int(year) % 400 != 0:
#         return '28'
#     elif month == '4' or month == '6' or month == '9' or month == '11':
#         return '30'
#     else:
#         return '31'
#
#
#
#
# def chekDate(date: str) -> bool:
#   d = (dataX.split('-'))
#   year = d[0]
#   if len(year) != 4 or int(year) > 2024 or int(year) < 1980:
#       return False
#   month = d[1]
#   if len(month) == 0 or len(month) > 2 or int(month) < 1 or int(month) > 12:
#       return False
#   day = d[2]
#   if len(day) == 0 or len(day) > 2 or int(day) < 1 or int(day) > int(numDay(month)):
#       return False



import time

offset = -2
while True:
    endpoint = f'https://api.telegram.org/bot{token}/getUpdates'
    param = {'offset': offset + 1}
    response = requests.get(endpoint, params=param).json()
    if response['result']:
        offset = response['result'][0]['update_id']
        userText = response['result'][0]['message']['text']
        chatID = response['result'][0]['message']['chat']['id']

        photoUrl, photoExp = givePhoto(userText)
        pprint.pprint(chatID)
        endpoint = f'https://api.telegram.org/bot{token}/sendPhoto'
        params = {'chat_id': chatID, 'photo': photoUrl}
        resul = requests.get(endpoint, params=params)

        endpoint = f'https://api.telegram.org/bot{token}/sendMessage'
        params = {'chat_id': chatID, 'text': photoExp}
        res = requests.get(endpoint, params=params)
        pprint.pprint(res)
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
