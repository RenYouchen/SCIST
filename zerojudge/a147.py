n = 10000
while n != 0:
    n = int(input())
    for i in range(n):
        if i % 7 != 0:
            print(i,end=' ')
    print()