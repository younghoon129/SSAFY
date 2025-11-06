import sys
sys.stdin = open('C:\\Users\\user\\Desktop\\코딩폴더 깃허브\\김영훈\\SSAFY\\보충수업\\2511_IM대비2_codetree\\251104_codetree_square\\codetree_square_input.txt', 'r')
from pprint import pprint
# n = int(input())

# box = [[0] * 200 for _ in range(200)]
# for _ in range(n):
#     a, b, c, d = map(int, input().split())
#     for i in range((b+ 99), (d + 99)):
#         for j in range((a + 99), (c + 99)):
#             box[i][j] = 1
# result = 0
# for i in range(len(box)):
#     result += sum(box[i])
# # print(box)
# print(result)
OFFSET = 100

n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)

board = [[0 for _ in range(201)] for _ in range(201)]

# 주어진 사각형 마다
for i in range(len(x1)):
    
    # 사각형 범위 안을 색칠
    for j in range(x1[i], x2[i]):
        print(j)
        for k in range(y1[i], y2[i]):
            board[j][k] += 1
    
cnt = 0
for i in range(201):
    for j in range(201):
        if board[i][j] >= 1:
            cnt += 1

print(cnt)