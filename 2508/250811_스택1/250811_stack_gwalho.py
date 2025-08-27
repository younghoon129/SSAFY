
# 괄호가 제대로 짝이 맞는 지를 확인하는 함수
def check_match(expression):
    # 짝이 맞는 지를 볼 때는 어떤 자료구조를 쓴다?
    #->Stack => 후입 선출
    stack = [] # 빈 리스트로 초기화
    # key = 닫힌 괄호
    # value = 열린 괄호
    # key 로 접근하면, 그거에 매칭되어야 할 value를 반환해준다.
    matching_dict = {
        ')' : '(',
        '}' : '{',
        ']' : '['
    }
    # 주어진 문자열(expression)을 순회하면서, 괄호의 종류에 따라 push, pop을 진행하면서 비교
    for char in expression:
        # 여는 괄호가 나오면, 바로 스택에 넣는다.
        if char in matching_dict.values():
            stack.append(char)
        # 닫힌 괄호가 나오면, 스택에 pop 하고 같은 괄호인 지 비교한다.
        elif char in matching_dict.keys():
            # 스택에서 꺼내고 비교한다.
            # 스택이 비어있으면 끝낸다. -> 괄호 비교해야되는데 할게 없으면

            if not stack:
                return False


            # 비어있지 않으면 꺼냄.
            # 짝이 맞는지 확인해햐함.
            # 현재 char = 닫힌 괄호 -> key 값으로 넣으면
            # -> 이 닫힌 괄호에 매칭되어야 하는 여는 괄호가 나옵니다.
            if stack[-1] != matching_dict[char]:
                # -> 스택의 마지막(비교할 괄호)이 문장의 첫 괄호랑 다르면
                return False


            #스택이 비어있지도 않고, 짝도 맞는 경우
            stack.pop()
    if stack:  # 스택이 안 비었으면 열린 괄호가 없다는 뜻.
        return False
    return True
    # -> 괄호 비교해서







examples = ["(a(b)", "a(b)c)", "a{b(c[d]e)f}"]
for ex in examples:
    if check_match(ex):
        print(f"{ex} 는 올바른 괄호")
    else:
        print(f"{ex} 는 올바르지 않은 괄호")





# #전치 (행과 열을 바꿈) -> 개중요***************************
# origin_matrix = [[1,2,3], [4,5,6], [7,8,9]]
# reverse_matrix = list(map(list, zip(*origin_matrix)))
# # zip 같은 열끼리 묶는 것
#
# # 회전
# # 이거 중요하고 암기라도 하자********************************
# rotate_90_clockwise_matrix = list(zip(*origin_matrix[::-1]))
#
# # 1) 행을 뒤집는 건
# # (i,j) -> (j, n-1-i)
