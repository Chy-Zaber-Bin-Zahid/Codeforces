t = int(input())
for i in range(t):
  n = int(input())
  list1 = list(map(int,input().split()))
  total = sum(list1)
  if (total % 2) == 0:
    print("Bob")
  else:
    print("Alice")