import datetime
import os
import random
import sys
import time
import re
from io import BytesIO

sys.path.append(os.getcwd().replace('/src', ''))
from lib import LineApp

game_flag = False
sorry_flag = False
angry_flag = False
work_flag = False
tired_flag = False
app = LineApp.LineApp()

userID = 'U444d8a9ca45523b6fcda0226769d9983'

history_msgs = []


def emotion_analysis():
    return random.random()


def main():
    while True:
        if not len(app.get_msgs()) == 0:
            msg = app.get_msgs().pop(0)[1]
            history_msgs.append(msg)
            if msg == '今日のご飯':
                app.push_msgs(userID, 'ご飯を提案します')

            if msg == '試合':
                game_flag = True
            if msg == 'ごめん':
                sorry_flag = True
            if msg == '怒':
                angry_flag = True
            if msg == '仕事':
                work_flag = True
            if msg == '疲れ':
                tired_flag = True
        time.sleep(1)


if __name__ == '__main__':
    main()
