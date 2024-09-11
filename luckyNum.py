"""
Tong cac so 4, 7 bang 4 hoac 7 la so may man
"""
n = input()
cnt1 = n.count('4')
cnt2 = n.count('7')
if cnt1+cnt2 == 4 or cnt1+cnt2 == 7:
    print("YES")
else:
    print("NO")