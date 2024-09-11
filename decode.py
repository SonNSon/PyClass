"""
Cho một xâu ký tự độ dài không quá 100 chỉ bao gồm các chữ cái in hoa. Người ta thực hiện mã hóa bằng cách đếm các ký tự cạnh nhau giống nhau và viết số lượng phía sau các chữ cái đó.

Ví dụ xâu AAECCCCGGGD thì được mã hóa thành A2E1C4G3D1

Với giả thiết không có ký tự nào xuất hiện nhiều hơn 9 lần liên tiếp.

Cho trước xâu kết quả mã hóa. Hãy khôi phục xâu ký tự ban đầu tương ứng.
"""

t = int(input())
while t>0:
    s = input()
    rs = ""
    tmp = s[0]
    for i in range(1,len(s)):
        if s[i].isdigit():
            rs += tmp*int(s[i])
        else:
            tmp = s[i]
    print(rs)
    t -= 1