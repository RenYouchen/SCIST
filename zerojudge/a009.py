k = ord("1") - ord("*")

inputString = input()

for i in inputString:
    print(chr(ord(i) - k), end='')