for i in range(int(input())):
    n = int(input())
    list1 = list(map(int,input().split()))
    c = 0
    for j in range(n):
        store = list1.pop(j)
        if (sum(list1)/len(list1)) == store:
            print("YES")
            break
        list1.insert(j,store)
        c+=1
    if c == n:
        print("NO")