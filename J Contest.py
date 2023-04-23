a, b, c, d = list(map(int,input().split()))
m = max(((3*a)/10),(a-((a/250)*c)))
v = max(((3*b)/10),(b-((b/250)*d)))
if m > v:
    print("Misha")
elif m < v:
    print("Vasya")
else:
    print("Tie")
