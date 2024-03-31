from flask import Flask, request
from flask_socketio import SocketIO, emit
from flask_cors import CORS
import logging
import pyautogui
import time
from urllib.parse import unquote
import json
import pydirectinput
import threading

app = Flask(__name__)
socketio = SocketIO(app)
werkzeug_logger = logging.getLogger("werkzeug")
werkzeug_logger.setLevel(logging.ERROR)

keyList = []

pyautogui.FAILSAFE = False

CORS(app)

speed = 30
currentKey = ""

mouseDirX = 0
mouseDirY = 0

pydirectinput.PAUSE = 0.03

with open("./Server/keymap.json", "r") as file:
    json_data = json.load(file)

# def MouseMove():
#     global mouseDirY
#     global mouseDirX
#     while True:
#         pydirectinput.moveRel(mouseDirX * speed, mouseDirY * speed, relative=True)
# tr = threading.Thread(target=MouseMove)
# tr.start()

@socketio.on("connect")
def SocketConnect():
    print("connected")

@socketio.on("disconnect")
def SocketDisConnect():
    print("disconnect")

@socketio.on("message")
def SocketMessage(msg):
    print(msg)
print(socketio)
# @app.route("/")
# def hello():
#     return "Hello Flask!"


# @app.route("/checkConnect", methods=["POST"])
# def Check():
#     data = request.data
#     data = unquote(data.decode("utf-8"))
#     return "connected"


# @app.route("/key", methods=["POST"])
# def Key():
#     global mouseDirY
#     global mouseDirX
#     global currentKey
#     data = request.data
#     data = unquote(data.decode("utf-8"))
#     data = json.loads(data)

#     keyName = json_data.get(data.get("keyName", None))
#     status = data.get("status", 0)
#     if status == 0:
#         # while keyName in keyList:
#         #     keyList.remove(keyName)
#         if keyName == "click":
#             pass    
#         elif keyName == "rClick":
#             pass
#         elif keyName == "-right":
#             mouseDirX = 0
#             mouseDirY = 0
#         elif keyName == "-left":
#             mouseDirX = 0
#             mouseDirY = 0
#         elif keyName == "-up":
#             mouseDirX = 0
#             mouseDirY = 0
#         elif keyName == "-down":
#             mouseDirX = 0
#             mouseDirY = 0
#         else:
#             for i in keyName.split(","):
#                 pydirectinput.keyUp(i)
#     else:
#         # if keyName not in keyList:
#         #     keyList.append(keyName)
#         if keyName == "click":
#             pydirectinput.leftClick()
#         elif keyName == "rClick":
#             pydirectinput.rightClick()
#         elif keyName == "-right":
#             mouseDirX = 1
#             mouseDirY = 0
#         elif keyName == "-left":
#             mouseDirX = -1
#             mouseDirY = 0
#         elif keyName == "-up":
#             mouseDirX = 0
#             mouseDirY = -1
#         elif keyName == "-down":
#             mouseDirX = 0
#             mouseDirY = 1
#         else:
#             for i in keyName.split(","):
#                 pydirectinput.keyDown(i)

#     return "connected"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
