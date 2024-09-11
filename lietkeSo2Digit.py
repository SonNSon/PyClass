"""
nhap xau, liet ke cac so co 2 chu so theo thu tu tang dan
"""

a = input()
myset = set()


for i in range(0, len(a) - 1, 2):
    myset.add(a[i:i+2])

l = list(myset)
l.sort()
print(" ".join(l))