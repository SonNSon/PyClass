"""
sap xep tong cac chu so
"""
def sum1(n):
    s = 0
    for i in str(n):
        s += int(i)
    return s
t = int(input())

while t > 0:
    n = int(input())
    a = list(int(x) for x in input().split())
    a.sort(key = sum1)
    for i in a:
        print(i, end = ' ')
        if i == a[-1]:
            print('') 
    t -= 1