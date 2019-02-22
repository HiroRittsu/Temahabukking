# -*- coding:utf-8 -*-
import urllib.request
import json
import requests

url = 'https://api.line.me/v2/bot/message/push'
channel_access_token = '/07Z+OlPxitHyS23cLdU+jdE7XOhZJ8ABueC4ctVy/chTD3sxn3qUTRN66UoUH/weuD3MkL7twkVGs9Ik3tjAcD+NHBXU7t9HcRi+ebCcwuJq+RAG77Ad3P7WplaOgCx8qovCfUON3LiV5OZndRLtgdB04t89/1O/w1cDnyilFU='
user_id = 'U444d8a9ca45523b6fcda0226769d9983'

REPLY_ENDPOINT = 'https://api.line.me/v2/bot/message/reply'


def post_text(reply_token, text):
    header = {
        "Content-Type": "application/json",
        "Authorization": "Bearer {" + channel_access_token + "}"
    }
    payload = {
        "replyToken": reply_token,
        "messages": [
            {
                "type": "text",
                "text": text
            }
        ]
    }
    requests.post(REPLY_ENDPOINT, headers=header, data=json.dumps(payload))


post_text(user_id, 'debug')
