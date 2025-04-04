6081
n = input()
n = int(n, 16)
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

for i in list:
    print('%X'%n, '*%X'%i, '=%X'%(n*i), sep='')

6082
n = int(input())
for i in range(1, n+1):
    if i%10==3:
        print("X", end=" ")
    elif i%10==6:
        print("X", end=" ")
    elif i%10==9:
        print("X", end=" ")
    else:
        print(i, end=" ")

6083
r, g, b = input().split()
r = int(r)
g = int(g)
b = int(b)
c = 0
for i in range(0, r):
    for j in range(0, g):
        for k in range(0, b):
            print(i, j, k)
            c += 1
print(c)

6084
h, b, c, s = input().split()
h = int(h)
b = int(b)
c = int(c)
s = int(s)
size = (h*b*c*s)/8/1024/1024
print(format(size, ".1f"), "MB")

6085
w, h, b = input().split()
w = int(w)
h = int(h)
b = int(b)
size = (w*h*b)/8/1024/1024
print(format(size, ".2f"), "MB")

6086
n = int(input())
c = 0
s = 0
while True:
    s += c
    c += 1 
    if s>=n:
        break
print(s)

6087
n = int(input())
for i in range(1, n+1):
    if i%3==0:
        continue
    print(i, end=" ")

6088
a, d, n = input().split()
a = int(a)
d = int(d)
n = int(n)
print(a+(n-1)*d)

6089
a, r, n = input().split()
a = int(a)
r = int(r)
n = int(n)
print(a*r**(n-1))

6090
a, m, d, n = input().split()
a = int(a)
m = int(m)
d = int(d)
n = int(n)
for i in range(1, n):
    a = (a*m) + d
print(a)

6091
a, b, c = map(int, input().split())
d = 1 
while d%a!=0 or d%b!=0 or d%c!=0:
    d += 1 
print(d)

6092
n = int(input())
a = input().split()

for i in range(n):
    a[i] = int(a[i])
    
d = []
for i in range(24):
    d.append(0)
    
for i in range(n):
    d[a[i]] += 1

for i in range(1, 24):
    print(d[i], end=" ")

6093
n = int(input())
a = input().split()
d = []

for i in range(n):
    a[i] = int(a[i])
    d.append(a[i])

for i in range(n-1, -1, -1):
    print(d[i], end=" ")

6094
n = int(input())
a = input().split()

d = []
for i in range(n):
    a[i] = int(a[i])
    d.append(a[i])

for i in d:
    min_num = i
    for j in d:
        if min_num > j:
            min_num = j

print(min_num)

6095
d = []
for i in range(20):
    d.append([])
    for j in range(20):
        d[i].append(0)
        
n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    d[x][y] = 1 
    
for i in range(1, 20):
    for j in range(1, 20):
        print(d[i][j], end=" ")
    print()
  
