"""
bo chuyen doi tu he co so 10 sang he co so bat ky
"""
def convert(n,base):
    storage = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = ""
    while n > 0:
        res += storage[n%base]
        n //= base
    return res[::-1]

t = int(input())

while t>0:
    n,b = map(int,input().split())
    print(convert(n,b))
    t -= 1