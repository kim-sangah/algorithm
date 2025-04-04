6056
a, b = input().split()
c = bool(int(a))
d = bool(int(b))
print((c and (not d)) or ((not c) and d))

6057
a, b = input().split()
c = bool(int(a))
d = bool(int(b))
print((c and d) or ((not c)and(not d)))

6058
a, b = input().split()
c = bool(int(a))
d = bool(int(b))
print(not(c or d))

6059
a = int(input())
print(~a)

6060
a, b = input().split()
c = int(a)
d = int(b)
print(c & d)

6061
a, b = input().split()
c = int(a)
d = int(b)
print(c|d)

6062
a, b = input().split()
c = int(a)
d = int(b)
print(c ^ d)

6063
a, b = input().split()
c = int(a)
d = int(b)
e = (c if (c>=d) else d)
print(e)

6064
a1, b1, c1 = input().split()
a = int(a1)
b = int(b1)
c = int(c1)
d = (a if (a<b) else b) if (b<c) else c
print(d)

6065
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
if a%2==0:
    print(a)
if b%2==0:
    print(b)
if c%2==0:
    print(c)

6066
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
print("even" if a%2==0 else "odd")
print("even" if b%2==0 else "odd")
print("even" if c%2==0 else "odd")

6067
a = int(input())
if a<0:
    print("A" if a%2==0 else "B")
else:
    print("C" if a%2==0 else "D")
