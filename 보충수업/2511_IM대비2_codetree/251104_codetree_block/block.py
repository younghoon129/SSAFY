import sys
sys.stdin = open('codetree_block_input.txt', 'r')

n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]
box = list([0]*n)
for i in range(len(commands)):
    for j in range(commands[i][0]-1, commands[i][1]):
        box[j] += 1
print(max(box))
