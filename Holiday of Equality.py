n = int(input())
if n == 1:
    a = int(input())
    print(a-a)
else:
    list1 = list(map(int,input().split()))
    max1 = max(list1)
    count = 0
    for j in list1:
        if j != max1:
            count+=(max1-j)
    print(count)