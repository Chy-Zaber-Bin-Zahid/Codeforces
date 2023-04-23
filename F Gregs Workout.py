n = int(input())
list1 = list(map(int,input().split()))
ch, bi, ba = [0]*3
for i in range(0,len(list1),3):
    ch+=list1[i]
for i in range(1,len(list1),3):
    bi+=list1[i]
for i in range(2,len(list1),3):
    ba+=list1[i]
if ch > bi and ch > ba:
    print("chest")
elif bi > ch and bi > ba:
    print("biceps")
else:
    print("back")
# if n>=1:
# if n>=2:
#     for i in range(1,len(list1),3):
#         bi+=list1[i]
# if n>=3:
#     for i in range(2,len(list1),3):
#         ba+=list1[i]