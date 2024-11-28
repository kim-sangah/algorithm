6068
a = int(input())
if a>=90:
    print('A')
elif a>=70:
    print('B')
elif a>=40:
    print('C')
else:
    print('D')

6069
s = input()
if s=="A":
    print("best!!!")
elif s=="B":
    print("good!!")
elif s=="C":
    print("run!")
elif s=="D":
    print("slowly~")
else:
    print("what?")

6070
n = int(input())
if n//3==1:
    print("spring")
elif n//3==2:
    print("summer")
elif n//3==3:
    print("fall")
else:
    print("winter")

6071
n = 1
while n!=0:
    n = int(input())
    if n!=0:
        print(n)

6072
n = int(input())
while n!=0:
    print(n)
    n = n - 1

6073
n = int(input()) - 1
while n > -1:
    print(n)
    n = n - 1

6074
c = ord(input())
t = ord("a")
while t<=c:
    print(chr(t),end=" ")
    t += 1
