import datetime
import os
import random
import sys
import time
import re
from io import BytesIO

from lib.LineApp import line_bot_api

sys.path.append(os.getcwd().replace('/src', ''))
from lib import LineApp

from linebot import (
    LineBotApi, WebhookHandler, WebhookParser
)
from linebot.exceptions import (
    InvalidSignatureError
)
from line_bot_api.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageSendMessage, ImageMessage,
)
app = LineApp.LineApp()

userID = 'U444d8a9ca45523b6fcda0226769d9983'


def main():
    while True:
        if not len(app.get_msgs()) == 0:
            event = app.get_msgs().pop(0)[1]

            print("handle_image:", event)

            message_id = event.message.id
            message_content = line_bot_api.get_message_content(message_id)

            image = BytesIO(message_content.content)
        # if not len(app.get_msgs()) == 0:
        #    app.push_msgs(userID, app.get_msgs().pop(0)[1])
        time.sleep(1)
        # exam_schedule([[8, 10], [12, 20], [21, 30]])
        # option()
        # time.sleep(1)


if __name__ == '__main__':
    main()
