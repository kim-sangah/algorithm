# 윈도우창의 제목 설정 : t.title('제목')
# 그림 그릴 선의 굵기를 지정 : t.pensize(10)
# 터틀 머리 방향 설정 : t.setheading(0)
# 그래픽창이 키보드 입력을 기다림 : t.listen()
# onkeypress(함수명, '키이름') : 키보드 방향키를 입력하면 함수 실행
#            키이름 : 'Left', 'Right', 'Up', 'Down'
# 함수 : 반복적으로 사용되는 코드를 하나의 기능으로 묶어 함수로 만드는 것
# def 함수이름(매개변수):


import turtle as t

def right():    
    t.setheading(0)
    t.forward(10)

def up():    
    t.setheading(90)
    t.forward(10)

def left():    
    t.setheading(180)
    t.forward(10)

def down():    
    t.setheading(270)
    t.forward(10)

t.title('방향키를 활용한 그림 그리기')
t.shape('turtle')
t.pensize(10)

t.onkeypress(right, "Right")
t.onkeypress(up, "Up")
t.onkeypress(left, "Left")
t.onkeypress(down, "Down")
t.listen()
