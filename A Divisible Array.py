t = int(input())
for i in range(t):
    n = int(input())
    l = []
    store = 0
    s = 1
    total = 0
    for j in range(n):
        store = n*s
        s+=1
        total+=store
        l.append(store)
    print(' '.join(map(str, l)))