n, m = list(map(int,input().split()))
store = n+m
count = 0
for i in range(store):
    if n != 0 and m != 0:
        count+=1
        n-=1
        m-=1
        store-=2
    if n==0 or m == 0:
        break

if count%2==0 and(store!=0 or store!=1):
    print("Malvika")
else:
    print("Akshat")