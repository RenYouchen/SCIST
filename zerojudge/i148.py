try:
    while True:
        s = input().split()
        total = 0
        for i in range(len(s)):
            s[i] = int(s[i])
        for j in range(s[0]):
            total += s[j+1]
        if (total / s[0] > 59):
            print("no")
        else:
            print("yes")
except EOFError:
    pass