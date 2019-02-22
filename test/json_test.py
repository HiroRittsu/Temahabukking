# -*- coding:utf-8 -*-
import urllib.request
import json
import requests

url = 'https://api.line.me/v2/bot/message/push'
channel_access_token = '/07Z+OlPxitHyS23cLdU+jdE7XOhZJ8ABueC4ctVy/chTD3sxn3qUTRN66UoUH/weuD3MkL7twkVGs9Ik3tjAcD+NHBXU7t9HcRi+ebCcwuJq+RAG77Ad3P7WplaOgCx8qovCfUON3LiV5OZndRLtgdB04t89/1O/w1cDnyilFU='
user_id = 'U444d8a9ca45523b6fcda0226769d9983'

REPLY_ENDPOINT = 'https://api.line.me/v2/bot/message/push'


def post_text(user_id, text):
    header = {
        "Content-Type": "application/json",
        "Authorization": "Bearer {" + channel_access_token + "}"
    }
    data = {
        'to': user_id,
        'messages': [
            {
                "type": "template",
                "altText": "this is a buttons template",
                "template": {
                    "type": "buttons",
                    "actions": [
                        {
                            "type": "message",
                            "label": "アクション 1",
                            "text": "アクション 1"
                        },
                        {
                            "type": "message",
                            "label": "アクション 2",
                            "text": "アクション 2"
                        },
                        {
                            "type": "message",
                            "label": "アクション 3",
                            "text": "アクション 3"
                        }
                    ],
                    "thumbnailImageUrl": "SPECIFY_YOUR_IMAGE_URL",
                    "title": "タイトルです",
                    "text": "テキストです"
                }
            }
        ]
    }
    print(requests.post(REPLY_ENDPOINT, headers=header, data=json.dumps(data)))


post_text(user_id, 'debug')
