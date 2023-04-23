m = int(input())
list1 = []
thanos = {"green" : "Time","yellow" : "Mind","orange" : "Soul","purple" : "Power","red" : "Reality","blue" : "Space"}
if m!=0:
    for i in range(m):
        list1.append(input())
    print(len(thanos)-m)
    for j in thanos:
        if j not in list1:
            print(thanos[j])
else:
    print(6)
    for k in thanos:
        print(thanos[k])