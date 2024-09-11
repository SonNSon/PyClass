"""
Viết chương trình kiểm tra xem số nguyên dương N có thỏa mãn tính chất: nếu ta lấy hai chữ số đầu và hai chữ số cuối của nó thì sẽ tạo ra số có hai chữ số giống nhau hay không
"""
t = int(input())
while t>0:
    n = input()
    if n[0:2] == n[-2:]:
        print("YES")
    else:
        print("NO")
    t -= 1