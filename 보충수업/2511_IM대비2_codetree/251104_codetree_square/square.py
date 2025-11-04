import sys
sys.stdin = open('C:\\Users\\user\\Desktop\\코딩폴더 깃허브\\김영훈\\SSAFY\\보충수업\\2511_IM대비2_codetree\\251104_codetree_square\\codetree_square_input.txt', 'r')
from pprint import pprint
# x1, y1, x2, y2 = [], [], [], []
# for _ in range(n):
#     a, b, c, d = map(int, input().split())
#     x1.append(a)
#     y1.append(b)
#     x2.append(c)
#     y2.append(d)
n = int(input())

box = [[0] * 200 for _ in range(200)]
for _ in range(n):
    a, b, c, d = map(int, input().split())
    for i in range((b+ 99), (d + 99)):
        for j in range((a + 99), (c + 99)):
            box[i][j] = 1
result = 0
for i in range(len(box)):
    result += sum(box[i])
# print(box)
print(result)