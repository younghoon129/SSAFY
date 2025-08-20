class Stack:
    def __init__(self, capacity = 10):  # 클래스 스택 실행하면 가장먼저 하는 기본적인 설정?
        self.capacity = capacity  # 초기 용량 설정
        self.items = [None]*capacity  # 저장공간 확보
        # top : 가장 마지막 원소의 위치를 가리킨다.
        self.top = -1  # 초기에는 데이터가 없으니까, -1로 설정


    # 스택이 가득찼는 지 확인하는 메서드
    def is_full(self):
        # 가장 마지막 원소의 위치가 ... 내가 초기에 설정한 크기 -1 과 같으면 가득 찬거
        return self.top == self.capacity -1  #

    # 스택의 마지막 위치에 데이터를 삽입하는 메서드
    def push(self, item):
        if self.is_full():  # 만약 가득찼다면?
            raise IndexError("Stack if Full")
        # 가득차지 않았다면, top 위치의 +1에 데이터를 삽입
        self.top += 1
        self.items[self.top] = item

    # 스택에서 가장 마지막원소를 빼고, 반환하는 작업
    def pop(self):
        # 비어있는 지 확인
        if self.is_empty():
            raise IndexError("Stack is Empty")
        # 스택 pop 은 데이터를 삭제뿐만 아니라, 반환도 함 -> 반환하며 삭제
        item = self.items[self.top]  # item 넣고
        # 기존에 들어있던 데이터를 제거
        self.items[self.top] = None  # 빈자리로 만들기
        #맨 마지막 원소가 사라졌으니, 그 밑에 있는 친구가 마지막 원소가 된다.
        self.top -= 1  # 마지막 원소 포인터 이동
        return item
    
    #pop이랑은 다르게, 데이터를 지우는게 아니고 출력만 하는거다... 마지막 원소를
    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is Empty")
        return self.items[self.top]

    def is_empty(self):
        return self.top == -1

stack = Stack(3)

stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())
print(stack.pop())
print(stack.pop())
