# 램덤(random) 함수 : import random
# 0<=N<1 사이의 실수 N을 무작위로 선택 : random.random()
# 펜올림 / 그림이 그려지지 않음 : t.penup()
# 펜내림 / 그림이 그려짐 : t.pendown()
# (x,y)위치로 이동 : t.goto(x,y)
# 현재 위치에 거북이 모양을 남김 : t.stamp()
# 마우스를 클릭하면 입력된 함수 실행 : onscreenclick(함수명, 번호)
#                    (1=마우스왼쪽, 2=마우스가운데, 3=마우스오른쪽)
# 그래픽 창이 마우스 입력을 기다림 : t.done()

import turtle as t
import random

def LeftClick(x,y):
    ClickColor()
    t.pendown()
    t.goto(x,y)

def RightClick(x,y):
    ClickColor()
    t.penup()
    t.goto(x,y)

def MidClick(x,y):
    ClickColor()
    t.penup()
    t.goto(x,y)
    t.stamp()

def ClickColor():
    t.color((random.random(), random.random(), random.random()))   

t.title('거북이로 그림 그리기')
t.shape('turtle')
t.pensize(10)

t.onscreenclick(LeftClick,1)
t.onscreenclick(MidClick,2)
t.onscreenclick(RightClick,3)
t.done()
