n1, n2 = sorted(input().split())
n1 = int(n1)
n2 = int(n2)
while n1 != 0 and n2 != 0:
    if n1 > n2: n1 %= n2
    elif n1 < n2: n2 %= n1
if n1 >= n2: print(n1)
else: print(n2)
print()
