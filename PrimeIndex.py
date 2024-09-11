"""
1 so la nguyen to dung neu vi tri do la so nguyen to thi so tai do cung la nguyen to
"""

t = int(input())

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

while t>0:
    s = input()
    check = True
    for i in range(len(s)):
        if i<2 and isPrime(int(s[i])):
            check = False
            break
        else:
            if isPrime(i) and not isPrime(int(s[i])):
                check = False
                break
            elif not isPrime(i) and isPrime(int(s[i])):
                check = False
                break
    if check:
        print("YES")
    else:
        print("NO")
    t -= 1
    