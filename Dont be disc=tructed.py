for i in range(int(input())):
    l = int(input())
    s = input()
    if l == 2 or l == 1:
        print("YES")
    else:
        list1 = []
        list2 = []
        list3 = []
        for n in s:
            if n not in list3:
                list3.append(n)
        count = 0
        j = 0
        for m in list3:
            list2.append(s.count(m))
        for k in range(l):
            if s[k] == s[j]:
                if k == l-1:
                    count+=1
                    list1.append(count)
                else:
                    count+=1
            else:
                if k == l-1:
                    list1.append(count)
                    list1.append(1)
                else:
                    list1.append(count)
                    j = k
                    count = 1
        if list1 == list2:
            print("YES")
        else:
            print("NO")