import math 

def calcRadius(x, y):
    return (x**2 + y**2)**0.5

# angle between 2 lines from (0;0) to the corresponding point
def calcAngle(x1,y1,x2,y2):
    angle1 = math.atan2(y1, x1)
    angle2 = math.atan2(y2, x2)
    
    angle = math.degrees(angle1-angle2)
    
    return angle + 360 if angle < 0  else angle

def calcArcLength(angle, radius):
    return math.pi*radius*angle/180
    


xa, ya, xb, yb = map(int, input().split())

r1, r2 = calcRadius(xa, ya), calcRadius(xb, yb)

angle = calcAngle(xa, ya, xb, yb)
arc = calcArcLength(angle, min(r1,r2))
diff = abs(r1-r2)

res = min(r1+r2, arc+diff)
print(res)
