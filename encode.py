"""
Cho một xâu ký tự có thể có các ký tự chữ cái và chữ số. Người ta thực hiện một phép mã hóa đơn giản, trong đó đếm từ trái qua phải các ký tự giống nhau liên tiếp và viết số đếm trước ký tự đó.

Ví dụ: AACDDPQ được mã hóa thành 2A1C2D1P1Q

           11111147g được mã hóa thành 6114171g

Viết chương trình thực hiện thao tác mã hóa như trên.
"""

t = int(input())

while t>0:
    s = input()
    tmp = s[0]
    count = 1
    result = ""
    for i in range(1, len(s)):
        if s[i] == tmp:
            count += 1
        else:
            result += str(count) + tmp
            tmp = s[i]
            count = 1
    result += str(count) + tmp
    print(result)
    t -= 1