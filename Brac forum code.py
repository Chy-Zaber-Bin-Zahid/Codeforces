n = int(input())
list1 = []
for i in range(1, n+1):
    if i%3 == 0:
        list1.append(i)
print(sum(list1))