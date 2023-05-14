n, m = list(map(int,input().split()))
store = n+m
count = 0
for i in range(n+m):
    if store-2 >= 0:
        count+=1
        store-=2
    
if (count%2==0 and store == 0) or (count%2==0 and store == 1):
    print("Malvika")
else:
    print("Akshat")