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


def template(thumbnail, link, title, text):
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
                    "title": title,
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


def response_wait():
    while True:
        print("debug")
        if not len(app.get_postback()) == 0:
            return app.get_postback().pop(0)


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
                    thumbnail = 'https://image.walkerplus.com/lettuce/img/dish/1/S20140210031001A_000.png?x=450'
                    link = 'https://sites.google.com/view/migly-sample/%E3%83%9B%E3%83%BC%E3%83%A0'
                    title = 'カツ丼'
                    text = '牡蠣 - 酒 - 玉ねぎ - にんじん - バター - にんにく - しょうが'
                    app.push_json(template(thumbnail, link, title, text))
                    game_flag = False

                # case2
                if sorry_flag == True and angry_flag == True:
                    # 手巻き寿司
                    thumbnail = 'https://park.ajinomoto.co.jp/wp-content/uploads/2018/03/705987.jpeg'
                    link = 'https://sites.google.com/view/migly-sample/%E3%83%9B%E3%83%BC%E3%83%A0'
                    title = '手巻き寿司'
                    text = 'イカ - サーモン - いくら - はまち - 鯛 - まぐろ - キュウリ - カイワレ大根 - 大葉'
                    app.push_json(template(thumbnail, link, title, text))

                    if response_wait() == 'no':
                        # ムニエル
                        thumbnail = 'https://img.cpcdn.com/recipes/5516497/m/d8bfff3490f57def01e4ed004f190e07.jpg?u=27736998&p=1550589458'
                        link = 'https://sites.google.com/view/migly-sample/%E3%83%9B%E3%83%BC%E3%83%A0'
                        title = '鯛のムニエル　野菜＆ナッツのバターソース'
                        text = '鯛 - 塩・コショウ - 薄力粉 - セロリ茎 - トマト - 玉ねぎ - カシューナッツ - 乾燥スライスニンニク - パセリ(みじん切り) - バター - オリーブ油'
                        app.push_json(template(thumbnail, link, title, text))

                    sorry_flag = False
                    angry_flag = False

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
