t = input()
zero = list(filter(None, t.split("1")))
one = list(filter(None, t.split("0")))
c = 0
for i in zero:
  if len(i)>=7:
    c+=1
for i in one:
  if len(i)>=7:
    c+=1
if c>0:
  print("YES")
else:
  print("NO")