miskha, chris, draw = [0]*3
for i in range(int(input())):
    m, c = list(map(int,input().split()))
    if m>c:
        miskha+=1
    elif m<c:
        chris+=1
    else:
        draw+=1
if miskha == chris or (miskha == 0 and chris == 0 and draw != 0):
    print("Friendship is magic!^^")
elif miskha > chris:
    print("Mishka")
else:
    print("Chris")