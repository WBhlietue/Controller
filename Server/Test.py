import tornado.ioloop
import tornado.web
import tornado.websocket
import pyautogui
import time
from urllib.parse import unquote
import json
import pydirectinput
import threading

keyList = []
pyautogui.FAILSAFE = False
pydirectinput.FAILSAFE = False
speed = 30
currentKey = ""

mouseDirX = 0
mouseDirY = 0

pydirectinput.PAUSE = 0.03

with open("./Server/keymap.json", "r") as file:
    json_data = json.load(file)

def MouseMove():
    global mouseDirY
    global mouseDirX
    while True:
        pydirectinput.moveRel((int)(mouseDirX * speed), (int)(-mouseDirY * speed), relative=True)
tr = threading.Thread(target=MouseMove)
tr.start()

class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print("WebSocket 连接已建立")

    def on_message(self, message):
        print("接收到消息:", message)
        Key(message)
        self.write_message("服务器收到消息：" + message)

    def on_close(self):
        print("WebSocket 连接已关闭")

def make_app():
    return tornado.web.Application([
        (r"/websocket", WebSocketHandler),
    ], websocket_ping_interval=30, websocket_ping_timeout=120)






def Key(data):
    global mouseDirY
    global mouseDirX
    global currentKey
    # data = unquote(data.decode("utf-8"))
    data = json.loads(data)
    value = data.get("keyName", None)
    keyName = json_data.get(data.get("keyName", None))
    # print(value)
    status = data.get("status", 0)
    if status == 0:
        # while keyName in keyList:
        #     keyList.remove(keyName)
        if keyName == "click":
            pass    
        elif keyName == "rClick":
            pass
        elif keyName == "mouse":
            mouseDirX = 0
            mouseDirY = 0
        elif keyName == "wasd":
            mouseDirX = 0
            mouseDirY = 0
        else:
            for i in keyName.split(","):
                pydirectinput.keyUp(i)
    else:
        # if keyName not in keyList:
        #     keyList.append(keyName)
        if keyName == "click":
            pydirectinput.leftClick()
        elif keyName == "rClick":
            pydirectinput.rightClick()
        elif keyName == "mouse":
            mouseDirX = data.get("x", None)
            mouseDirY = data.get("y", None)
        elif keyName == "wasd":
            mouseDirX = 0
            mouseDirY = 0
        else:
            for i in keyName.split(","):
                pydirectinput.keyDown(i)

    return "connected"





if __name__ == "__main__":
    app = make_app()
    app.listen(8000)
    print("WebSocket 服务器已启动")
    tornado.ioloop.IOLoop.current().start()
