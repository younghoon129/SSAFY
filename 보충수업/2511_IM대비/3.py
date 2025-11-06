# b = input()
# r = 0
# cnt = 0

# for i in b[::-1]:
#     r = r + (2**cnt)*int(i)
#     cnt+=1
# print(r)

binary = input()
num = 0
# Please write your code here.
for i in range(len(binary)):
    num = num * 2 + int(binary[i])
    print(num)
print(num)