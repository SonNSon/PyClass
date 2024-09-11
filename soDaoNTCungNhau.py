"""
neu so dao cua n va n co uoc chung lon nhat = 1
"""

t = int(input())

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a%b)

def rvsr(n):
    return int(str(n)[::-1])

while t>0:
    n = int(input())
    if(gcd(n, rvsr(n)) == 1):
        print("YES")
    else:
        print("NO")
    t-=1