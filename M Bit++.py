c = 0
for _ in range(int(input())):
    store = input()
    if "+" in store:
        c+=1
    elif "-" in store:
        c-=1
print(c)