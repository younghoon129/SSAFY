class Stack:
    def __init__(self, capacity = 10):
        self.capacity = capacity
        self.items = [None]*capacity
        self.top = -1
    # 스택이 가득찼는 지 확인하는 메서드
    def is_full(self):
        # 가장 마지막 원소의 위치가 ... 내가 초기에 설정한 크기 -1 과 같으면 가득 찬거
        return self.top == self.capacity -1
        pass

    def push(self, item):
        if self.is_full():
            raise IndexError("Stack if Full")
        # 가득차지 않았다면, top 위치의 +1에 데이터를 삽입
        self.top += 1
        self.items[self.top] = item

    # 스택에서 가장 마지막원소를 빼고, 반환하는 작업
    def pop(self):
        #비어있는 지 확인
        if self.is_empty():
            raise IndexError("Stack is Empty")
        # 스택 pop 은 데이터를 삭제뿐만 아니라, 반환도 함
        item = self.items[self.top]
        # 기존에 들어있던 데이터를 제거
        self.items[self.top] = None
        #맨 마지막 원소가 사라졌으니, 그 밑에 있는 친구가 마지막 원소가 된다.
        self.top -= 1
        return item
    
    #pop이랑은 다르게, 데이터를 지우는게 아니고 출력만 하는거다... 마지막 원소를
    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is Empty")
        return self.items[self.top]

    def is_empty(self):
        return self.top == -1

# 괄호가 제대로 짝이 맞는 지를 확인하는 함수
def check_match(expression):
    # 짝이 맞는 지를 볼 때는 어떤 자료구조를 쓴다?
    #->Stack => 후입 선출
    stack = [] # 빈 리스트로 초기화
    # key = 여는 괄호
    # calue = 닫힌 괄호
    matching_dict = {
        ')' : '(',
        '}' : '{',
        ']' : '['
    }
    for char in expression:
        # 여는 괄호가 나오면, 바로 스택에 넣는다.
        if char in matching_dict.values():
            stack.append(char)
        # 닫힌 괄호가 나오면, 스택에 pop 하고 같은 괄호인 지 비교한다.
        elif char in matching_dict.keys():
            # 스택에서 꺼내고 비교한다.
            if not stack:
                return False
            
            # 비어있지 않으면 꺼냄
            # 짝이 맞는지 확인해햐함. 닫힌 괄호 -> 키 값으로 넣으면
            # 이 닫힌 괄호에 매칭되어야 하는 여는 괗고 나옵니다.
            if stack[-1] != matching_dict[char]
                return False
            
            #스택이 비어있지도 않고, 짝도 맞는 경우
            stack.pop()
            -1
            #???
            stack[-1] != matching_dict[char]
examples = ["(a(b)", "a(b)c)", "a{b(c[d]e)f}"]
for ex in examples:
    if check_match(ex):
        print(f"{ex} 는 올바른 괄호")
    else:
        print(f"{ex} 는 올바르지 않은 괄호")





#전치 (행과 열을 바꿈) -> 개중요***************************
origin_matrix = [[1,2,3], [4,5,6], [7,8,9]]
reverse_matrix = list(map(list, zip(*origin_matrix)))
# zip 같은 열끼리 묶는 것

# 회전
# 이거 중요하고 암기라도 하자********************************
rotate_90_clockwise_matrix = list(zip(*origin_matrix[::-1]))

# 1) 행을 뒤집는 건
# (i,j) -> (j, n-1-i)
