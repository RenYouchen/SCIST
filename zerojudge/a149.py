n = int(input())
for i in range(n):
    temp = input()
    ans = 1
    for j in temp:
        ans *= int(j)
    print(ans)
