"""
neu tong cac chu so la so thuan nghich thi YES
"""

def sum1(n):
    s = 0
    for i in str(n):
        s += int(i)
    return s
def rvsr(n):
    if n < 10: return False
    return str(n) == str(n)[::-1]
t = int(input())
while t > 0:
    n = int(input())
    if(rvsr(sum1(n))):
        print("YES")
    else:
        print("NO")
        
    t -= 1