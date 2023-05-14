for i in range(int(input())):
    a, q= list(map(int,input().split()))
    store = sum(list(map(int,input().split())))
    for j in range(q):
        f,l,s = list(map(int,input().split()))
        for k in range(l):
            if f<=k and k<=l:
                store[k-1] = s
                print(store)
                