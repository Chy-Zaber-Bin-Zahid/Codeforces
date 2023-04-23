sevenNumber = input().replace(" ","").split(",")
myList = []
for i in sevenNumber:
  myList.append(int(i))
maxNum = myList[0]
idx = 0
for i in range(1,len(myList)):
  if myList[i] > maxNum:
    maxNum = myList[i]
    idx = i

print(f"My list: {myList}\nLargest number in the list is {maxNum} which was found at index {idx}.")
