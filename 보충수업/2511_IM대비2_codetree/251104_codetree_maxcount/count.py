import sys
sys.stdin = open('codetree_count_input.txt', 'r')

n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

max_num = max(map(max, segments))
box = list([0] * 200)

for i in range(n):
    x = segments[i][0] +99
    y = segments[i][1] +99
    for j in range(x, y):
        box[j] += 1
print(max(box))