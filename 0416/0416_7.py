# 램덤(random) 함수 : import random
# a<=N<=b 사이의 정수 N을 무작위로 선택 : random.randint(a,b)
# 펜올림 / 그림이 그려지지 않음 : t.penup()
# 펜내림 / 그림이 그려짐 : t.pendown()
# (x,y)위치로 이동 : t.goto(x,y)
# 현재 터틀 위치의 x좌표를 알림 : t.xcor()
# t.write(arg, move=False, align='left', font=('Arial,8,'normal'))
#         arg = 쓰여질 글씨  align = 'left', 'center', 'right'
#         font = (fontname, fontsize, fonttype)
#         fonttype = 'normal', 'bold'

import turtle as t
import random

t.title("거북이 경주 게임")

t1 = t.Turtle()
t2 = t.Turtle()

t1.shape("turtle")
t1.color("pink")
t2.shape("turtle")
t2.color("blue")

t1.penup()
t1.goto(-300,100)
t2.penup()
t2.goto(-300,-100)

for i in range(30):
    d1 = random.randint(1,30)
    t1.forward(d1)
    d2 = random.randint(1,30)
    t2.forward(d2)

##if t1.xcor() > t2.xcor():
##    t1.write("내가 이겼다", align="center", font=("굴림",20,"bold"))
##else:
##    t2.write("내가 승리", align="center", font=("굴림",20,"bold"))




