t = int(input())
def factorial(n):
    return 1 if (n==1 or n==0) else n*factorial(n - 1)


while t>0:
    n = int(input())
    sum1 = 0
    for i in str(n):
        sum1 += factorial(int(i))
    print("Yes" if sum1 == n else "No")