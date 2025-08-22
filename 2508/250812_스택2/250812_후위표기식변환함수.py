# # 중위 표기식을 후위 표기식으로 변환하는 함수
# def infix_to_postfix(expression):
#     # 연산자의 우선순위
#     op_dict = {'+' : 1, '-': 1, '*': 2, '/': 2, '(': 0}
#     stack = []  # 연산자를 저장할 스택
#     postfix = []  # 후위 표기식을 저장할 리스트
#
#     # 주어진 입력값을 하나하나씩 순회하면서 보자
#     for ch in expression:
#         #