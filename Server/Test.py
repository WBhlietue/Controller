import math
def GetWASD(x, y):
    angle = math.atan2(x, -y)  
    directions = ['w', 'w,a', 'a', 'a,s', 's', 's,d', 'd', 'd,w']  
    index = round((angle + math.pi) / (math.pi / 4)) % 8
    return directions[index]

print(GetWASD(1, 0))
print(GetWASD(1, 1))
print(GetWASD(0, 1))
print(GetWASD(-1, 1))
print(GetWASD(-1, 0))
print(GetWASD(-1, -1))
print(GetWASD(0, -1))
print(GetWASD(1, -1))