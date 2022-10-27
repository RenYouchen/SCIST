n = input()
for i in range(int(n)):
    temp = input().split()
    if int(temp[1]) - int(temp[0]) == int(temp[2]) - int(temp[1]):
        temp.append(int(temp[3])+(int(temp[1]) - int(temp[0])))
        for j in range(5):
            print(temp[j],end = ' ')
    else:
        temp.append(int(int(temp[3]) * (int(temp[1]) / int(temp[0]))))
        for j in range(5):
            print(temp[j], end=' ')
    print()
