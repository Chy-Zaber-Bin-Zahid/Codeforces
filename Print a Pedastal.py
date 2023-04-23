for _ in range(int(input())):
    n = int(input())
    a,b,c,=[0]*3
    count = 0
    for i in range(n):
        if count < n and b == 0:
            b+=1
            count+=1
            if count == n:
                break
        elif count < n and a == 0:
            count+=1
            b+=1
            if count == n:
                break
            a+=1
            count+=1
            if count == n:
                break
        else:
            b+=1
            count+=1
            if count == n:
                break
            a+=1
            count+=1
            if count == n:
                break
            c+=1
            count+=1
            if count == n:
                break
    print(a,b,c)