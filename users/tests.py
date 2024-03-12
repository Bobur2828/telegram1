from telegram import Bot
import requests
def get_chat_id(bot_token):
    url = f"https://api.telegram.org/bot{bot_token}/getUpdates"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data['result'] :
            chat_id = data['result'][0]['message']['chat']['id']
            print(chat_id)
        else:
            print('No update found')
    else:
        print(f'{response.status_code}')

chat_id = get_chat_id('7199036679:AAHBM6wDGLha-6Kyb-PojeuSsFyKiDqn500')
print(chat_id)