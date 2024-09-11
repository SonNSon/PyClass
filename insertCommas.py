"""
tinh tu chu so cuoi cung, moi 3 chu so thi them dau phay
"""
n = input()
n = n[::-1]
res = ""
for i in range(len(n)):
    if i%3 == 0 and i != 0:
        res += ","
    res += n[i]
print(res[::-1])