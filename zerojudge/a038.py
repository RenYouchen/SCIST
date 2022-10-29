s = input()
zero = False
for i in range(len(s), 0, -1):
    if (int(s[i-1]) != 0 or zero == True):
        zero = True
        print(s[i-1], end='')
if (zero == False):
    print(0, end='')
