try:
    while True:
        n = int(input())
        s = input().split()
        for i in range(len(s)):
            s[i] = int(s[i])
        b = sorted(s)
        for j in b:
            print(j, end=' ')
        print()
except EOFError:
    pass
