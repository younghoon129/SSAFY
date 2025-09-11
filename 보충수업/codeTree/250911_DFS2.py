n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]



vil_count = 0
men_count = []

def can_go(x, y):
    if(x < 0 and y < 0 and x >= n and y >= n):
        return False
    
    if(grid[x][y] != 1):
        return False
    return True

def dfs(x, y):
    grid[x][y] = 0
    men_count = 1

    # for dx, dy in zip(dx, dy):
    for i in range(0, 4):
        nx, ny = x + dx[i], y + dy[i]
        if (can_go(nx, ny)):
            men_count += dfs(nx, ny)
    return men_count


for i in range(n):
    for j in range(n):
        if(grid[i][j] == 1):
            vil_count += 1
            men_count.append(dfs(i, j))

print(vil_count)
for i in men_count.sort():
    print(i)