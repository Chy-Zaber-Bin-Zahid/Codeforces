for i in range(int(input())):
    n = int(input())
    s = input()
    count = 0
    for j in range(n):
        if j == 0:
            new = s[j+1:]
            if new == new[::-1]:
                count+=1
        elif j == n-1:
            new = s[:n-1]
            if new == new[::-1]:
                count+=1
        else:
            new = s[:j] + s[j+1:]
            if new == new[::-1]:
                count+=1
    print(count)
    
    
    
    
    
    
    
    
    # list1 = []
    # for i in range(n):
    #     list1.append(s[i])
    # c = 0
    # for j in range(n):
    #     temp = list1.pop(j)
    #     store = list(reversed(list1))
    #     if store == list1:
    #         c+=1
    #     list1.insert(j,temp)
    # print(c)