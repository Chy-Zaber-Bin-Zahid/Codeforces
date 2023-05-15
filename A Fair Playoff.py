t = int(input())
check = ""
for _ in range(t):
    a,b,c,d = list(map(int,input().split()))
    if (a<c and a<d) and (b<c and b<d):
        check="NO"
    elif (a>c and a>d) and (b>c and b>d):
        check="NO"


    if check == "NO":
        print("NO")
    else:
        print("YES")
    check = ""