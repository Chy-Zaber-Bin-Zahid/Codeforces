s = input()
if len(s) == 4:
    list2 = []
    for i in s:
        if ord(i) not in list2:
            list2.append(ord(i))
    if len(list2) == 2:
        print("Yes")
    else:
        print("No")
else:
    print("No")