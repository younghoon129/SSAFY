# b = int(input())
# b = bin(b)
# b= str(b)
# print(b[2:])

b= int(input())
bl = []
while True:

    if b < 2:
        bl.append(b)
        break

    bl.append(b%2)
    # print(bl)
    b = b // 2

bl = bl[::-1]
print(*bl, end="")
# for i in bl[::-1]:
#     print(i, end="")