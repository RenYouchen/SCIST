n = int(input())
h = list(map(int,input().split()))
ans = 0
size = len(h)
if h[0] == 0:
        ans += h[1]
if h[size-1] == 0:
        ans += h[size-2]
for i in range(1,size-1,1):
    if h[i] == 0:
        if h[i+1] < h[i-1]:
            ans += h[i+1]
        else :
            ans += h[i-1]
print(ans)