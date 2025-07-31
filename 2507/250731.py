# data = [1,2,3,4,5]
# # print(data)

# def custom_len(items):
#     print(items)
#     cnt = 0
#     for _ in items:
#         cnt += 1
#     return cnt


# print(custom_len(data), "길이") #5

# print(max(data),"가장 큰 값")

# def custom_max(items):
#     max_value = items[0]
#     for item in items[1:]:
#         if max_value < item:
#             max_value = item 
#     return max_value
# print(custom_max(data))

# def custom_sum(items):
#     total = 0
#     for item in items:
#         total+= item
#     return total
# print(custom_sum(data))

# L = [10,20,30,20,40]

# def custom_index(items, value):
#     for idx,item in enumerate(items):
#         if item == value:
#             return idx
#     return -1

# print(custom_index(L, 30))

# reversed_new = [1,2,3,4,5,6]
# def custom_reverse_new(items):
#     new_list = []
#     for i in range(len(items)-1,-1,-1):
#         new_list.append(items[i])
#     return new_list

# print(custom_reverse_new(reversed_new))

# 은행 이자율 클래스? 인스턴스?

class BankAccount:
    interest_rate = 0.02

    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >=amount:
            self.balance -= amount
        else:
            print("잔액 부족")
    
    @classmethod
    def set_interest_rate(cls, rate):
        cls.interest_rate = rate

    @staticmethod
    def is_positive(aomunt):
        return amount > 0
    
account = BankAccount("김영훈", 500)
print(account.balance)
account.deposit(500)
print(account.balance)
account.withdraw(200)

BankAccount.set_interest_rate(0.83)
print(BankAccount.interest_rate)
print(BankAccount.is_positive)