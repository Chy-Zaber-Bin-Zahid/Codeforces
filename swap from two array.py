for i in range(int(input())):
    n, k = list(map(int,input().split()))
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    if k != 0:
        if n != 1:
            for j in range(k):
                if j == (k-1):
                    if min(a) < max(b):
                        a[a.index(min(a))], b[b.index(max(b))] = b[b.index(max(b))], a[a.index(min(a))]
                        print(sum(a))
                    else:
                        print(sum(a))
                else:
                    if min(a) < max(b):
                        a[a.index(min(a))], b[b.index(max(b))] = b[b.index(max(b))], a[a.index(min(a))]
        else:
            if a[0]<b[0]:
                a[0], b[0] = b[0], a[0]
                print(a[0])
            else:
                print(a[0])
    else:
        print(sum(a))