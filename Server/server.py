from flask import Flask, request
from flask_cors import CORS
import logging
import pyautogui
import time
import threading
from urllib.parse import unquote
import json
import keyboard
import pydirectinput

app = Flask(__name__)
werkzeug_logger = logging.getLogger('werkzeug')
werkzeug_logger.setLevel(logging.ERROR)

keyList = []

pyautogui.FAILSAFE = False

CORS(app)

speed =10
currentKey = ""

mouseDirX = 0
mouseDirY = 0

pydirectinput.PAUSE = 0.03

with open('./Server/keymap.json', 'r') as file:
    json_data = json.load(file)

def PressKey():
    print("thread")
    while True:
        for i in keyList:
            # pyautogui.press(i)
            # keyboard.press_and_release(i)
            pydirectinput.keyDown(i)

tr = threading.Thread(target=PressKey)
tr.start()

@app.route('/')
def hello():
    return 'Hello Flask!'

@app.route('/checkConnect', methods=['POST'])
def Check():
    data = request.data
    data = unquote(data.decode('utf-8'))
    return "connected"


@app.route('/key', methods=['POST'])
def Key():
    global currentKey 
    data = request.data
    data = unquote(data.decode('utf-8'))
    data = json.loads(data)

    keyName = json_data.get(data.get("keyName", None))
    status = data.get("status", 0)
    if(status == 0):
        # while keyName in keyList:
        #     keyList.remove(keyName)
        pydirectinput.keyUp(keyName)
    else:
        # if keyName not in keyList:
        #     keyList.append(keyName)
        pydirectinput.keyDown(keyName)
    print(keyName)
    return "connected"




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)


