n, m = map(int, input().split())  # Nhập số hàng và số cột
mt = []

# Nhập ma trận
for i in range(n):
    mt.append(list(map(int, input().split())))  # Nhập mỗi hàng với m số nguyên

# Tìm giá trị lớn nhất và nhỏ nhất
max_val = mt[0][0]
min_val = mt[0][0]
for i in range(n):
    for j in range(m):
        if mt[i][j] > max_val:
            max_val = mt[i][j]
        if mt[i][j] < min_val:
            min_val = mt[i][j]

luckNum = max_val - min_val

# Lưu tất cả các vị trí của luckNum
positions = []
for i in range(n):
    for j in range(m):
        if mt[i][j] == luckNum:
            positions.append((i, j))

# In số luckNum và tất cả các vị trí
if positions:
    print(f"Số {luckNum}")
    for pos in positions:
        print(f"Vi tri [{pos[0]}][{pos[1]}]")
else:
    print("NOT FOUND")
