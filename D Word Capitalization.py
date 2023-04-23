s = input()
u = s[0]
if len(s) > 1:
    s = f"{u.upper()}{s[1:]}"
    print(s)
else:
    print(u.upper())
