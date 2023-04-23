n = int(input())
s = ""
for i in range(1,n+1):
    if i%2 == 0:
        if "it" in s:
            s = s.replace("it", "that")
            s+=" I love it"
    else:
        if "it" in s:
            s = s.replace("it", "that")
            s+=" I hate it"
        else:
            s+="I hate it"
print(s)

