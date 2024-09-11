"""
vd input : 1 xau ki tu "12ads34dasd123" => output: 12
"""
t = int(input())


while t>0:
    s = input()
    temp = ""
    result = []
    for i in s:
        if i.isdigit():
            temp += i
        else:
            if temp:
                result.append(int(temp))
                temp = ""
    if temp:
        result.append(int(temp))

    if result:
        print(max(result))
    else:
        print("No exist")
    t -= 1
