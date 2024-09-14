t = int(input())

def bieuthuc(s):
    tmp1 = []
    cnt = 0
    stack = []
    for char in s:
        if char == '(':
            cnt += 1
            stack.append(cnt)
            tmp1.append(cnt)
        elif char == ')':
            tmp1.append(stack.pop())
    return tmp1

while t > 0:
    s = input().strip().replace(' ', '')
    for char in s:
        if char.isalnum():
            s = s.replace(char, '')  
        elif char in ['+', '-', '*', '/']:
            s = s.replace(char, '')
    l = bieuthuc(s)
    l = ' '.join(str(i) for i in l)
    print(l)
    t -= 1