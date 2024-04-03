import tornado.ioloop
import tornado.web
import tornado.websocket
import json
import pydirectinput
import threading
import math

def MouseMove():
    global mouseDirY
    global mouseDirX
    while True:
        pydirectinput.moveRel((int)(mouseDirX * speed), (int)(-mouseDirY * speed), relative=True)

def GetWASD(x, y):
    angle = math.atan2(x, -y)  
    directions = ['w', 'w,a', 'a', 'a,s', 's', 's,d', 'd', 'd,w']  
    index = round((angle + math.pi) / (math.pi / 4)) % 8
    return directions[index]

class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        self.write_message(json_data)
        print("connect")

    def on_message(self, message):
        Key(message)

    def on_close(self):
        print("dis connect")

    
def make_app():
    return tornado.web.Application([
        (r"/websocket", WebSocketHandler),
    ], websocket_ping_interval=30, websocket_ping_timeout=120)

def Key(data):
    global mouseDirY
    global mouseDirX
    global currentKey
    global currentWASD
    global test
    global ease
    data = json.loads(data)
    keyName = json_data.get(data.get("keyName", None))
    status = data.get("status", 0)
    if status == 0:
        if keyName == "click":
            pydirectinput.mouseUp(button=pydirectinput.PRIMARY)
        elif keyName == "rClick":
            pydirectinput.mouseUp(button=pydirectinput.SECONDARY)
        elif keyName == "mClick":
            pydirectinput.mouseUpd(button=pydirectinput.MIDDLE)
        elif keyName == "mouse":
            mouseDirX = 0
            mouseDirY = 0
        elif keyName == "wasd":
            letters = GetWASD(data.get("x", None),data.get("y", None))
            for i in letters.split(","):
                pydirectinput.keyUp(i)
            for l in test:
                for i in l.split(","):
                    pydirectinput.keyUp(i)
            currentWASD = ""

        else:
            for i in keyName.split(","):
                pydirectinput.keyUp(i)
    else:
        if keyName == "click":
            pydirectinput.mouseDown(button=pydirectinput.PRIMARY)
        elif keyName == "rClick":
            pydirectinput.mouseDown(button=pydirectinput.SECONDARY)
        elif keyName == "mClick":
            pydirectinput.mouseDown(button=pydirectinput.MIDDLE)
        elif keyName == "mouse":
            s = math.pow(data.get("length", None), ease)
            mouseDirX = data.get("x", None) * s
            mouseDirY = data.get("y", None) * s
        elif keyName == "wasd":
            if(data.get("length", None) > 0.3):
                letters = GetWASD(data.get("x", None),data.get("y", None))
                if(currentWASD != letters):
                    test.append(letters)
                    if(currentWASD in test):
                        test.remove(currentWASD)    
                    for i in currentWASD.split(","):
                        pydirectinput.keyUp(i)
                    currentWASD = letters
                    for i in letters.split(","):
                        pydirectinput.keyDown(i)
        else:
            for i in keyName.split(","):
                pydirectinput.keyDown(i)
    return "connected"

pydirectinput.FAILSAFE = False
speed = 30
currentKey = ""

mouseDirX = 0
mouseDirY = 0

test = []

pydirectinput.PAUSE = 0.03
with open("./Server/keymap.json", "r") as file:
    json_data = json.load(file)

ease = json_data.get("mouseEase")
speed=  json_data.get("mouseSpeed")


tr = threading.Thread(target=MouseMove)
tr.start()

currentWASD = ""

app = make_app()
app.listen(8000)
print("WebSocket 服务器已启动")
tornado.ioloop.IOLoop.current().start()
