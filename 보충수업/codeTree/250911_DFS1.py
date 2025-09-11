n, m = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]


def in_range(x, y):
    return 0 <= x
def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] or grid[x][y] == 0:

def dfs(x, y):
    dxs = [0, 1, 0, -1, 1, -1]
    dys = [1, 0, -1, 0, 1, 1 ]


visited[0][0] = 1
dfs(0, 0)

print(visited[n-1][m-1])
