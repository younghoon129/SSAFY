import sys
sys.stdin = open('C:\\Users\\user\\Desktop\\코딩폴더 깃허브\\김영훈\\SSAFY\\보충수업\\2511_IM대비2_codetree\\251104_codetree_square2\\codetree_square2_input.txt', 'r')
from pprint import pprint

box = [[0] * 2000 for _ in range(2000)]
for _ in range(2):
    a, b, c, d = map(int, input().split())
    for i in range((b+ 999), (d + 999)):
        for j in range((a + 999), (c + 999)):
            box[i][j] = 1
a, b, c, d = map(int, input().split())
for i in range((b+ 999), (d + 999)):
    for j in range((a + 999), (c + 999)):
        box[i][j] = 2
result = 0
for i in range(len(box)):
    for j in range(len(box)):
        if box[i][j] == 1:
            result += box[i][j]
# print(box)
print(result)