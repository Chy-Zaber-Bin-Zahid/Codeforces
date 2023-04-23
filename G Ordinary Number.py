n = int(input())
list1 = list(map(int,input().split()))
p1 = 0
p2 = 1
p3 = 2
c = 0
for i in range(n):
    if list1[p3] != list1[-1]:
        if (list1[p1] < list1[p2] < list1[p3]) or (list1[p1] > list1[p2] > list1[p3]):
            c+=1
            p1+=1
            p2+=1
            p3+=1
        else:
            p1+=1
            p2+=1
            p3+=1
    else:
        if (list1[p1] < list1[p2] < list1[p3]) or (list1[p1] > list1[p2] > list1[p3]):
            c+=1
        break
print(c)
     