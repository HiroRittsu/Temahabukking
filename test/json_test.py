# -*- coding:utf-8 -*-
import urllib.request
import json
import requests

url = 'https://api.line.me/v2/bot/message/push'
channel_access_token = 'DvNsKeKTNGDsPDAHmEdzgifwYLtPdg1BV1+YAvz0a3TQmP7LCXbaZF6up4XHpR1Ye8XMItPbX8HB5zsuQLKe5m0YHWlNlp6EAZ73xJCoXZLyarr4HLikG2ZAobqAyn0Ay3ObOoIKHGgbCCL5eAwQUwdB04t89/1O/w1cDnyilFU='
user_id = 'U444d8a9ca45523b6fcda0226769d9983'

REPLY_ENDPOINT = 'https://api.line.me/v2/bot/message/push'


def post_text(user_id, text):
    header = {
        "Content-Type": "application/json",
        "Authorization": "Bearer {" + channel_access_token + "}"
    }
    data = {
        'to': user_id,
        "messages": [
            {
                "type": "template",
                "altText": "this is a confirm template",
                "template": {
                    "type": "confirm",
                    "text": "材料の受け取りはどちらにしますか？",
                    "actions": [
                        {
                            "type": "message",
                            "label": "店舗で",
                            "text": "店舗"
                        },
                        {
                            "type": "message",
                            "label": "自宅で",
                            "text": "自宅"
                        }
                    ]
                }
            }
        ]
    }
    print(requests.post(REPLY_ENDPOINT, headers=header, data=json.dumps(data)))


post_text(user_id, 'debug')
