h,w = list(map(int,input("H W: ").split()))
r,c = list(map(int,input("R C: ").split()))
a = r+1
b = r-1
d = c+1
e = c-1 
squre = 0
for i in range(h*w):
    if a<=h:
        if abs((a-r)+(c-c))==1:
            squre+=1
        elif abs((b-r)+(c-c))==1:
            squre+=1
    if d<=w:
        if abs((r-r)+(d-c))==1:
            squre+=1
        elif abs((r-r)+(e-c))==1:
            squre+=1
    break
print(squre)
            
