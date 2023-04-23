s = input()
odd = ["R", "U", "D"]
even = ["L", "U", "D"]
c = 0
for i in range(0,len(s),2):
    if s[i] not in odd:
        c+=1
for j in range(1,len(s),2):
    if s[j] not in even:
        c+=1
if c == 0:
    print("Yes")
else:
    print("No")