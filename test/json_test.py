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
                "altText": "おすすめレストラン",
                "template": {
                    "type": "carousel",
                    "columns": [
                        {
                            "thumbnailImageUrl": "https://s3-us-west-2.amazonaws.com/lineapitest/hamburger_240.jpeg",
                            "title": "ジャンク・バーガー",
                            "text": "誰が何と言おうとジャンクフードの王様は、今も昔も変わらずハンバーガー。",
                            "actions": [

                                {
                                    "type": "uri",
                                    "label": "詳細を見る",
                                    "uri": "http://example.com/page/222"
                                }
                            ]
                        },
                        {
                            "thumbnailImageUrl": "https://s3-us-west-2.amazonaws.com/lineapitest/pizza_240.jpeg",
                            "title": "pizza cap",
                            "text": "本場ナポリの味を早く、安く。都内に17店舗展開するピザ専門店です。",
                            "actions": [

                                {
                                    "type": "uri",
                                    "label": "詳細を見る",
                                    "uri": "http://example.com/page/222"
                                }
                            ]
                        },
                        {
                            "thumbnailImageUrl": "https://s3-us-west-2.amazonaws.com/lineapitest/bread_240.jpeg",
                            "title": "本格パン工房 たけよし",
                            "text": "パンにとって一番大事だと思うものはなんですか？たけよしは、表面の焼き上がりこそが命であると考えています。",
                            "actions": [

                                {
                                    "type": "uri",
                                    "label": "詳細を見る",
                                    "uri": "http://example.com/page/222"
                                }
                            ]
                        },
                        {
                            "thumbnailImageUrl": "https://s3-us-west-2.amazonaws.com/lineapitest/harumaki_240.jpeg",
                            "title": "ヴェトナムTokyo",
                            "text": "東池袋にあるしたベトナム料理の老舗。40年以上人々に愛され続けてきたベトナム料理をご提供します。",
                            "actions": [

                                {
                                    "type": "uri",
                                    "label": "詳細を見る",
                                    "uri": "http://example.com/page/222"
                                }
                            ]
                        },

                    ]
                }
            }
        ]
    }
    print(requests.post(REPLY_ENDPOINT, headers=header, data=json.dumps(data)))


post_text(user_id, 'debug')
