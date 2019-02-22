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
        "messages": [
            {
                "type": "template",
                "altText": "This is a buttons template",
                "template": {
                    "type": "buttons",
                    "thumbnailImageUrl": "https://www.dinos.co.jp/kp/defaultMall/images/goods/D20/9154/etc/FD1734c1.jpg?Mode=main1s",
                    "imageAspectRatio": "rectangle",
                    "imageSize": "cover",
                    "imageBackgroundColor": "#FFFFFF",
                    "title": "レシピ",
                    "text": "ご飯\n"
                            "ケチャップ\n"
                            "たまごぉ\n",
                    "defaultAction": {
                        "type": "uri",
                        "label": "View detail",
                        "uri": "https://www.dinos.co.jp/kp/defaultMall/images/goods/D20/9154/etc/FD1734c1.jpg?Mode=main1s"
                    },
                    "actions": [
                        {
                            "type": "postback",
                            "label": "注文します",
                            "data": "action=buy&itemid=123"
                        },
                        {
                            "type": "postback",
                            "label": "注文しません",
                            "data": "action=add&itemid=123"
                        }
                    ]
                }
            }
        ]
    }
    print(requests.post(REPLY_ENDPOINT, headers=header, data=json.dumps(data)))


post_text(user_id, 'debug')
