n, m = list(map(int,input().split()))
list1 = list(map(int,input().split()))
min = 0
for i in range(m-1):
    store1 = list1.pop(i)
    store2 = list1.pop(i)
    j = 0
    for k in range(len(list1)):
        first = list1[k]
        if 