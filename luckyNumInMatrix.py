n, m = map(int, input().split())
mt = []

for i in range(n):
    mt.append(list(map(int, input().split()))) 


max = mt[0][0]
min = mt[0][0]
for i in range(n):
    for j in range(m):
        if mt[i][j] > max:
            max = mt[i][j]
        if mt[i][j] < min:
            min = mt[i][j]


luckNum = max - min
positions = []
for i in range(n):
    for j in range(m):
        if mt[i][j] == luckNum:
            positions.append((i, j))


if positions:
    print(luckNum)
    for pos in positions:
        print(f"Vi tri [{pos[0]}][{pos[1]}]")
else:
    print("NOT FOUND")


