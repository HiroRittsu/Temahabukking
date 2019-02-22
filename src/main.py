import datetime
import os
import random
import sys
import time
import re
from io import BytesIO

sys.path.append(os.getcwd().replace('/src', ''))
from lib import LineApp

app = LineApp.LineApp()

userID = 'U444d8a9ca45523b6fcda0226769d9983'

history_msgs = []


def emotion_analysis():
    return random.random()


def template(thumbnail, link, text):
    # 60文字超える場合
    if len(text) >= 60:
        text = text[0:53] + '\n詳細はタップ'

    data = {
        'to': userID,
        "messages": [
            {
                "type": "template",
                "altText": "This is a buttons template",
                "template": {
                    "type": "buttons",
                    "thumbnailImageUrl": thumbnail,
                    "imageAspectRatio": "rectangle",
                    "imageSize": "cover",
                    "imageBackgroundColor": "#FFFFFF",
                    "title": "レシピ",
                    "text": text,
                    "defaultAction": {
                        "type": "uri",
                        "label": "View detail",
                        "uri": link
                    },
                    "actions": [
                        {
                            "type": "postback",
                            "label": "注文します",
                            "data": "yes"
                        },
                        {
                            "type": "postback",
                            "label": "注文しません",
                            "data": "no"
                        }
                    ]
                }
            }
        ]
    }
    return data


def main():
    game_flag = False
    sorry_flag = False
    angry_flag = False
    work_flag = False
    tired_flag = False

    while True:
        if not len(app.get_msgs()) == 0:
            msg = app.get_msgs().pop(0)[1]
            history_msgs.append(msg)
            if '今日のご飯' in msg:
                app.push_msgs(userID, 'ご飯を提案します')

                # case1
                if game_flag == True:
                    # カツ丼
                    thumbnail = 'https://t4.ftcdn.net/jpg/01/46/63/19/240_F_146631973_bHTvB7Djehzsz1DW6U1TK4Rl3ZQLTA0v.jpg'
                    link = 'https://sites.google.com/view/migly-sample/%E3%83%9B%E3%83%BC%E3%83%A0'
                    text = '牡蠣 - 酒 - 玉ねぎ - にんじん - バター - にんにく - しょうが'
                    app.push_json(template(thumbnail, link, text))

            if '試合' in msg:
                game_flag = True
            if 'ごめん' in msg:
                sorry_flag = True
            if '怒' in msg:
                angry_flag = True
            if '仕事' in msg:
                work_flag = True
            if '疲れ' in msg:
                tired_flag = True
        time.sleep(0.1)


if __name__ == '__main__':
    main()
