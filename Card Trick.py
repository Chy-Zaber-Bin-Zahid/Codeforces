# for i in range(int(input())):
#     n = int(input())
#     list1 = list(map(int,input().split()))
#     m = int(input())
#     list2 = list(map(int,input().split()))
#     for j in list2:
#         for k in range(j):
#             store = list1.pop(0)
#             list1.append(store)
#     print(list1[0])

for i in range(int(input())):
    n, list1, m, list2 = int(input()), list(map(int,input().split())), int(input()), list(map(int,input().split()))
    for j in list2:
        list1 = list1[j:] + list1[:j]
    print(list1[0])

for t in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    m_len = int(input())
    m = list(map(int,input().split()))
    s = sum(m)%n
    print( l[s])