for _ in range(int(input())):
    n, m, k = list(map(int,input().split()))
    a, b, c = input(), input(), ""
    for i in range(n+m):
        if a != [] or b != []:
            store = a[0]
            for j in range(k):
                c+=store
                a.removesuffix(store)
                print(a, c)