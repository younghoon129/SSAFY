import sys
sys.stdin = open('codetree_square_input.txt', 'r')
n = int(input())
from pprint import pprint
# x1, y1, x2, y2 = [], [], [], []
# for _ in range(n):
#     a, b, c, d = map(int, input().split())
#     x1.append(a)
#     y1.append(b)
#     x2.append(c)
#     y2.append(d)
box = [[0] * 200 for _ in range(200)]
for _ in range(n):
    a, b, c, d = map(int, input().split())
    for i in range(d-b + 99):
        for j in range(c-a + 99):
            box[i][j] = 1
result = 0
for i in range(len(box)):
    result += sum(box[i])
print(box)
print(result)