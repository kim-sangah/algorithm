6075
a = int(input())
n = 0
while n<=a:
    print(n)
    n += 1

6076
n = int(input())
for i in range(n+1):
    print(i)

6077
n = int(input())
s = 0
for i in range(1, n+1) :
  if i%2==0 :
    s += i
print(s)

6078
a = ""
while a!="q":
    a = input()
    print(a)

6079
n = int(input())
s = 0
for i in range(1, n+1):
    s += i
    if s >= n:
        print(i)
        break

6080
n, m = input().split()
n = int(n)
m = int(m)
for i in range(1, n+1):
    for j in range(1, m+1):
        print(i,j)
