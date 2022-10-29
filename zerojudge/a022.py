s = input()
ans = 0
for i in range(len(s)//2):
    if (s[i] == s[len(s)-1-i]):
        ans = 1
    else:
        ans = 0
        break
if len(s) == 1:
    ans = 1
if ans == 1:
    print("yes")
else:
    print("no")
