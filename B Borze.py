code = input()
store = ""
l = len(code)
i=0
while i<l:
    if code[i] == ".":
        store+="0"
        i+=1
    elif code[i] == "-" and i!=l:
        if code[i+1] == ".":
            store+="1"
            i+=2
        else:
            store+="2"
            i+=2
print(store)