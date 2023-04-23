a, b = list(map(int,input().split()))
if (a == b) or ((a-1) == b) or (a == (b-1)):
    print(a+b)
else:
    if a>b:
        print(a+(a-1))
    else:
        print(b+(b-1))