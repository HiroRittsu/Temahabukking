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

# userID = 'U444d8a9ca45523b6fcda0226769d9983'
userID = 'Ce768ea847f6963afa3f73a7d63d8e080'

history_msgs = []


def emotion_analysis():
    return random.random()


def select_template():
    data = {
        'to': userID,
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
    return data


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
                            "label": "別の料理",
                            "data": "no"
                        },
                        {
                            "type": "postback",
                            "label": "キャンセル",
                            "data": "cancel"
                        }
                    ]
                }
            }
        ]
    }
    return data


def response_wait():
    app.get_msgs().clear()
    while True:
        if not len(app.get_postback()) == 0:
            return app.get_postback().pop(0)
        time.sleep(0.1)


def message_wait():
    app.get_msgs().clear()
    while True:
        if not len(app.get_msgs()) == 0:
            return app.get_msgs().pop(0)[1]
        time.sleep(0.1)


def main():
    game_flag = False
    sorry_flag = False
    angry_flag = False
    work_flag = False
    tired_flag = False

    app.push_msgs(userID, 'bot起動')

    while True:
        if not len(app.get_msgs()) == 0:
            msg = app.get_msgs().pop(0)[1]
            history_msgs.append(msg)
            if '今日のご飯' in msg:
                # case1
                if game_flag == True:
                    app.push_msgs(userID, 'ピッタリの料理をご提案します')
                    # カツカレー
                    thumbnail = 'https://img.cpcdn.com/recipes/4939420/m/49983e0dd58f3dc9ee5438c29c7d40be.jpg?u=20307638&p=1518680840'
                    link = 'https://sites.google.com/view/temahabokking0003/%E3%83%9B%E3%83%BC%E3%83%A0'
                    title = 'カツカレー　628円'
                    text = 'とんかつ（チキンでも可） - じゃがいも - 人参 - 玉ねぎ - 福神漬け - オリーブオイル（食材炒め用） - バーモントカレー中辛 - こくまろ甘口 - ゴールデンカレー甘口 - S&Bカレーパウダー - 塩・胡椒 - 醤油 - オイスターソース - かつおダシ'
                    app.push_json(template(thumbnail, link, title, text))

                    wait = response_wait()
                    if wait == 'no':
                        app.push_msgs(userID, '別の料理を提案します')
                        # 牡蠣カレー
                        thumbnail = 'https://image.walkerplus.com/lettuce/img/dish/1/S20140210031001A_000.png?x=450'
                        link = 'https://sites.google.com/view/temahabokking0005/%E3%83%9B%E3%83%BC%E3%83%A0'
                        title = '牡蠣カレー　840円'
                        text = '牡蠣 - 酒 - 玉ねぎ - にんじん - バター - にんにく - しょうが'
                        app.push_json(template(thumbnail, link, title, text))

                        if response_wait() == 'yes':
                            app.push_json(select_template())
                            # 待機
                            wait = message_wait()
                            if wait == '店舗':
                                app.push_msgs(userID, 'かしこまりました。')
                                app.push_msgs(userID, '材料を準備いたします。')
                            else:
                                app.push_msgs(userID, 'かしこまりました。')
                                app.push_msgs(userID, 'ご自宅にお届けします。')
                        else:
                            app.push_msgs(userID, '提案できる料理がありません')
                    elif wait == 'cancel':
                        app.push_msgs(userID, 'キャンセルしました。')
                    else:
                        app.push_json(select_template())
                        # 待機
                        wait = message_wait()
                        if wait == '店舗':
                            app.push_msgs(userID, 'かしこまりました。')
                            app.push_msgs(userID, '材料を準備いたします。')
                        else:
                            app.push_msgs(userID, 'かしこまりました。')
                            app.push_msgs(userID, 'ご自宅にお届けします。')

                    game_flag = False

                # case2
                if sorry_flag == True or angry_flag == True:
                    app.push_msgs(userID, 'ピッタリの料理をご提案します')
                    # 手巻き寿司
                    thumbnail = 'https://park.ajinomoto.co.jp/wp-content/uploads/2018/03/705987.jpeg'
                    link = 'https://sites.google.com/view/temahabokking0002/%E3%83%9B%E3%83%BC%E3%83%A0'
                    title = '手巻き寿司　1,740円'
                    text = 'イカ - サーモン - いくら - はまち - 鯛 - まぐろ - キュウリ - カイワレ大根 - 大葉'
                    app.push_json(template(thumbnail, link, title, text))

                    wait = response_wait()
                    if wait == 'no':
                        app.push_msgs(userID, '別の料理を提案します')
                        # ナッツサラダ
                        thumbnail = 'https://image.walkerplus.com/lettuce/img/dish/1/7013_0_0.jpg?x=450'
                        link = 'https://sites.google.com/view/temahabokking0006/%E3%83%9B%E3%83%BC%E3%83%A0'
                        title = 'ナッツサラダ　802円'
                        text = '牛ももステーキ用肉 - 塩 - ・粗びき黒こしょう - 春菊 - 紫玉ねぎ - ミックスナッツ'
                        app.push_json(template(thumbnail, link, title, text))

                        if response_wait() == 'yes':
                            app.push_json(select_template())
                            # 待機
                            wait = message_wait()
                            if wait == '店舗':
                                app.push_msgs(userID, 'かしこまりました。')
                                app.push_msgs(userID, '材料を準備いたします。')
                            else:
                                app.push_msgs(userID, 'かしこまりました。')
                                app.push_msgs(userID, 'ご自宅にお届けします。')
                        else:
                            app.push_msgs(userID, '提案できる料理がありません')
                    elif wait == 'cancel':
                        app.push_msgs(userID, 'キャンセルしました。')
                    else:
                        app.push_json(select_template())
                        # 待機
                        wait = message_wait()
                        if wait == '店舗':
                            app.push_msgs(userID, 'かしこまりました。')
                            app.push_msgs(userID, '材料を準備いたします。')
                        else:
                            app.push_msgs(userID, 'かしこまりました。')
                            app.push_msgs(userID, 'ご自宅にお届けします。')

                    sorry_flag = False
                    angry_flag = False

                # case3
                if work_flag == True or tired_flag == True:
                    app.push_msgs(userID, 'ピッタリの料理をご提案します')
                    # すっぽん鍋
                    thumbnail = 'https://imgfp.hotp.jp/IMGH/10/40/P022821040/P022821040_238.jpg'
                    link = 'https://sites.google.com/view/temahabokking0004/%E3%83%9B%E3%83%BC%E3%83%A0'
                    title = 'すっぽん鍋　2,460円'
                    text = 'すっぽん様 - はくさい - 豆腐 - 長ネギ - がんもどき、お豆腐 - お好きな野菜 - 水 - 出し昆布 - 酒 - 醤油'
                    app.push_json(template(thumbnail, link, title, text))

                    wait = response_wait()
                    if wait == 'no':
                        app.push_msgs(userID, '別の料理を提案します')
                        # ムニエル
                        thumbnail = 'https://img.cpcdn.com/recipes/5516497/m/d8bfff3490f57def01e4ed004f190e07.jpg?u=27736998&p=1550589458'
                        link = 'https://sites.google.com/view/temahabokking0001/%E3%83%9B%E3%83%BC%E3%83%A0'
                        title = '鯛のムニエル　1,280円'
                        text = '鯛 - 塩・コショウ - 薄力粉 - セロリ茎 - トマト - 玉ねぎ - カシューナッツ - 乾燥スライスニンニク - パセリ(みじん切り) - バター - オリーブ油'
                        app.push_json(template(thumbnail, link, title, text))

                        if response_wait() == 'yes':
                            app.push_json(select_template())
                            # 待機
                            wait = message_wait()
                            if wait == '店舗':
                                app.push_msgs(userID, 'かしこまりました。')
                                app.push_msgs(userID, '材料を準備いたします。')
                            else:
                                app.push_msgs(userID, 'かしこまりました。')
                                app.push_msgs(userID, 'ご自宅にお届けします。')
                        else:
                            app.push_msgs(userID, '提案できる料理がありません')
                    elif wait == 'cancel':
                        app.push_msgs(userID, 'キャンセルしました。')
                    else:
                        app.push_json(select_template())
                        # 待機
                        wait = message_wait()
                        if wait == '店舗':
                            app.push_msgs(userID, 'かしこまりました。')
                            app.push_msgs(userID, '材料を準備いたします。')
                        else:
                            app.push_msgs(userID, 'かしこまりました。')
                            app.push_msgs(userID, 'ご自宅にお届けします。')

                    work_flag = False
                    tired_flag = False

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
