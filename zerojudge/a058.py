n = int(input())
a = 0
b = 0
c = 0
for i in range(n):
    temp = int(input())
    if temp % 3 == 0:
        a += 1
    elif temp % 3 == 1:
        b += 1
    else:
        c += 1
print(a, b, c)
