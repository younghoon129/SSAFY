s1, b1, s2, b2 = map(int, input().split())
cnt = 0
while True:
    if s1 == s2 and b1 == b2:
        break
    b1 += 1
    cnt += 1
    
    if b1 >= 60:
        b1 -= 60
        s1 += 1
print(cnt)