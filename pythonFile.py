"""
file hop le chua duoi .py
kh chua so
chi chua cac ki tu a-z, A-Z va _ va .
"""
s = input().strip()
check = True
if s.endswith(".py"):
    for i in s:
        if not i.isalpha() and i != "_" and i != ".":
            check = False
            break
    if check:
        print("yes")
    else:
        print("no")
else:
    print("no")