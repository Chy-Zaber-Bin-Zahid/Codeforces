for i in range(int(input())):
    s = input()
    if len(s) == 2:
        print(s)
    else:
        print(s[0:len(s)-2:2] + s[len(s)-2:len(s)])