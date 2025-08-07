# 지그재그 (행 우선순위)

n = 3
m = 4
list_2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
for i in range(n):
    for j in range(m):
        print(list_2[i][j + (m-1-(2*j))* (i % 2)], end = " ")


# 델타 탐색

for row in materix:
    for num in row:
        sorted_List.append(num)

sorted_List.sort()

result = [0*N for _ in range(N)]
print(result)

dx = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

start_x, start_y = 0, 0
direction = 0

for value in sorted_List:
    reslut[x][y] = value
    nx = x + dx[direction]
    ny = y + dx[direction]
    if not (0 <= nx < N and 0 <= ny < N and result[nx][ny] == 0):
        direction = (direction +1)%4
        nx, ny = x + dx[direction], y + dy[direction]

    x, y =nx, ny

print(result)