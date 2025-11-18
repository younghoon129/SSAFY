dx = ()
dy = ()

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

bombs = []

for y in range(n):
    for x in range(n):
        if grid[y][x] == 1:
            bombs.append((y, x))

dy = [
    [],
    [-2, -1, 0, 1, 2],
    [-1, 0, 1, 0],
    [-1, 0, 1, 0],
    [-1, -1, 0, 0]
]
dx = [
    [],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, -1],
    [0, 0, 1, 1, 0],
]

bombs_num = [0 for _ in range(len(bombs))]



def recur(idx):
    
    if idx == len(bombs):
        area = set()
        for i, (y, x) in enumerate(bombs):
            num = bombs_num[i]
            for k in range(4):
                ny = y + dy[num][k]
                nx = x + dx[num][k]

                area.append((ny, nx))
        
        return len(area)
    
    bombs_num[idx] = 1
    v1 = recur(idx + 1)

    bombs_num[idx] = 2
    v2 = recur(idx + 1)

    bombs_num[idx] = 3
    v3 = recur(idx + 1)
    
    return max(v1, v2, v3)

recur(0)