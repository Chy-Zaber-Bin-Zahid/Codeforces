def run(a):
  dic1 = {}
  list1 = []
  check = 0
  key = ""
  tup = ()
  for i in range(a):
    c,b = input("Enter player name and run with a space: ").split()
    dic1[c] = int(b)
  for j in dic1:
    if dic1[j] > check:
      check = dic1[j]
      key = j
  list1.append(list(dic1).index(key))
  list1.append(dic1[key])
  return tuple(list1)


print(run(int(input("Enter how many player to add: "))))