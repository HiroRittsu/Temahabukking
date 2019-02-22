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


def main():
    while True:
        print(app.get_msgs())
        # if not len(app.get_msgs()) == 0:
        #    app.push_msgs(userID, app.get_msgs().pop(0)[1])
        time.sleep(1)
        # exam_schedule([[8, 10], [12, 20], [21, 30]])
        # option()
        # time.sleep(1)


if __name__ == '__main__':
    main()
