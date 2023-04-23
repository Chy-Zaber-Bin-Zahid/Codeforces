for i in range(int(input())):
    aNum = int(input())
    list1 = list(map(int,input().split()))
    bNum = int(input())
    list2 = list(map(int,input().split()))
    #For Alice
    if max(list1) > max(list2):
        print('Alice')
    elif max(list1) == max(list2):
        print('Alice')
    else:
        print('Bob')
    #For Bob
    if max(list1) < max(list2):
        print('Bob')
    elif max(list1) == max(list2):
        print('Bob')
    else:
        print('Alice')