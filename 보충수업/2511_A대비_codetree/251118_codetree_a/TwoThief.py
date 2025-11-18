

n, m, c = map(int,input().split())

def overlap(point1, point2):
    y1, x1 = point1
    y2, x2 = point2
    if y1 != y2:
        return False
    return x1 <= x2 <= (x1 + m -1) or x2 <= x1 <= (x2 + m - 1)

def get_value(point):
    y, x = point
    tmp = []
    for i in range(x, x + m):
        tmp.append(box[y][i])
    picked = [0 for _ in range(len(tmp))]
    value = pick(tmp, picked, 0)
    return value

def pick(arr, picked, idx):
    if idx == len(arr):
        box = 0
        value = 0

        for i in range(len(arr)):
            box += arr[i] * picked[i]
            value += arr[i] * arr[i] * picked[i]
        if box <= c:
            return value
        return -1
    picked[idx] = 1
    w1 = pick(arr, picked, idx + 1)

    picked[idx] = 0
    w2 = pick(arr, picked, idx + 1)

    return max(w1, w2)


box = [list(map(int, input().split())) for _ in range(n)]
result = 0
for y1 in range(n):
    for x1 in range(n - m + 1):


        for y2 in range(y1, n):
            for x2 in range(n - m + 1):
                if y1 == y2 and x2 <= x1:
                    continue
                if overlap((y1, x1), (y2, x2)):
                    continue
                new_value = get_value((y1, x1)) + get_value((y2, x2))
                result = max(result, new_value)

print(result)