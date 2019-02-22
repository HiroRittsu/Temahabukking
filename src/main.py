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


def main():
    while True:
        if not len(app.get_msgs()) == 0:
            msg = app.get_msgs().pop(0)[1]
            history_msgs.append(msg)
            if msg == '今日のご飯':
                app.push_msgs(userID, 'ご飯を提案します')

        time.sleep(1)


if __name__ == '__main__':
    main()
