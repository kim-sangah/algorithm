# 터틀을 활용하여 파이썬 문법 다지기
# 터틀 각도 지정해서 움직이기
# 터틀 색 지정하기 : t.color('green')
# 터틀 모양 지정하기 : t.shape('turtle')
# 터틀 머리 방향 설정 : t.setheading(270)
# 터틀 각도 설정 : t.right(90)
# 반지름 r인 원 그리기 : t.circle(r)
# 다각형을 채우는 색상 설정 : t.fillcolor('yellow')
# 채워진 다각형을 시작 : t.begin_fill()
# 채워진 다각형을 닫기 : t.end_fill()
# 펜올림 / 그림이 그려지지 않음 : t.penup()
# 펜내림 / 그림이 그려짐 : t.pendown()
# (x,y)위치로 이동 : t.goto(x,y)
# 윈도우창의 배경 색상을 변경 : t.bgcolor('lightblue')
# for 반복문
# for i in range(3):

import turtle as t

t.shape('turtle')
t.color('green')
t.forward(100)
t.right(90)
t.forward(100)

for i in range(3):
    t.forward(100)
    t.left(120)


