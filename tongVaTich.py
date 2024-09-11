"""
nhap 1 day so, tim tong cac chu so o vi tri chan va tich cac chu so o vi tri le cua so do
gap chu so 0 thi bo qua, neu toan bo idx le = 0 thi in ra 0 o tich
"""

t = int(input())
while t>0:
    n = input()
    tong = 0
    tich = 1
    NonZero = False
    for i in range(len(n)):
        if i%2 == 0:
            tong += int(n[i])
        else:
            if n[i] != '0':
                tich *= int(n[i])
                NonZero = True

    if NonZero == False:
        tich = 0
    print(tong, tich)
    t -= 1
    
    
