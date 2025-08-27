# from dollections import deque
# -> 큐를 써야된다, .pop(0) 써야된다 하면 무조건 이거 써라
# -> .pop(0)는 굉장히 비효율적이니까 이거 말고 .popleft(): 왼쪽에서 쏙 빼오는 거 써라
# -> appendleft 도 있음 (유용)
# -> rotate(n=1)
    # -> n단계 오른쪽으로 회전 -> [1,2,3,4] -> [4,1,2,3]
        # -> 음수이면 왼쪽으로 회전

# 선형 큐

# class Queue:
#     # 생성자 메서드
#     # 인스턴스가 생성될 때, 무조건 실행되는 메서드
#     # 초기화하는 용도로 사용된다.
#     def __init__(self, capacity=10):
#         self.capacity = capacity
#         self.items = [None] * capacity # -> 용량
#         self.front = -1  # 큐의 맨 앞의 요소를 가리키는 인덱스
#         self.rear = -1  # 큐의 맨 뒤의 요소를 가리키는 인덱스
#
#     # 큐가 비어있는 지 확인하는 메서드
#     def is_empty(self):
#         return self.front == self.rear
#
#     # 큐가 가득찼는지 확인하는 메서드
#     def is_full(self):
#         # 맨 뒤를 가리키는 rear 포인터를 활용해서 확인한다.
#         return self.rear == self.capacity -1
#
#     #  큐에 데이터를 삽입하는 메서드
#     def enqueue(self, item):
#         # 큐가 가득 찼는지부터 확인해야 됨
#         if self.is_full():
#             raise IndexError("큐가 가득참!")
#
#         #rear의 다음 칸에 데이터를 집어넣고, 그 다음에 rear 의 위치를 +1 한다.
#         self.rear += 1
#         # self.rear = self.rear + 1
#         self.items[self.rear] = item
#
#     # 큐에서 데이터를 꺼내는 메서드
#     def dequeue(self):
#         # 비어있는 지 먼저 확인 해야 됨
#         if self.is_empty():
#             raise IndexError("큐가 비어있음!")
#         # front 포인터 다음 위치의 데이터를 꺼내야 한다.
#         self.front += 1
#         item = self.items[self.front]
#         self.items[self.front] = None  # None으로 초기화를 해주는건데 사실 안해도 됨(이동하며 기존 데이터 None으로)
#         return item                    # 왜냐면 front가 옆 칸으로 이동하면서 기존 칸의 데이터에 접근할
#                                        # 방법이 없어서임. 삭제하지 않고, 포인터만 옮기고 기존 위치의 데이터는
#                                        # 덮어써도 문제없음.
#
#
#     # 맨 앞의 요소만 가져오는 것
#     def is_empty(self):
#         if self.is_empty():
#             raise IndexError("비어있음!")
#         return self.items[self.front + 1]
#
#
#     # 현재 큐에 들어있는 데이터의 개수
#     def get_size(self):  # rear + front  ex) 0 - (-1) = 1
#         return self.rear - self.front


#===============================================================================================

# 마이쭈

total_candy = 20  # 총 주어진 마이쮸 개수

queue = []  # 사람들이 줄 서는 큐

next_person = 1
# queue에다가 어떤 데이터가 필요한지?
# 누가 받을지(사람 번호)
# 몇 개 받을지(받을 개수)
queue.append((next_person, 1))  # 튜플로 되어있지만, 리스트 형식도 상관없음
last_person = None  # 마지막으로 마이쮸를 받을 사람의 번호를 저장할 변수

while total_candy > 0:
    # 캔디를 나눠주는 로직
    # queue에 있는 애들은 캔디를 받으려고 줄을 선 친구들
    # pop(0)을 이용해서 가장 앞의 데이터를 가져온다.
    # person: 받을 사람의 번호, cnt : 받을 사탕의 개수
    # 언패킹을 이용해서 한 번에 할당
    person, cnt = queue.pop(0)

    # 남아있는 캔디의 수가 "사람이 받아가야하는 캔디의 수" 보다 많아야 나눠줄 수 있다.
    if total_candy - cnt <= 0:
        print('total candy.', total_candy)
        print('몇개를 가져갈까?', cnt)
        last_person = person
        break

    # 받아야하는 개수만큼 총 캔디에서 차감
    total_candy -= cnt

    # 캔디를 받은 사람은 다시 줄을 선다. 대신 받는 캔디의 수 + 1
    queue.append((person, cnt + 1))


    # 다음 사람의 번호를 1 추가 한다.
    next_person +=1
    # 캔디를 받으면 => 새로운 사람이 다시 줄을 선다. (받는 캔디의 수: 1)
    queue.append((next_person, 1))


#===============================================================================================

# 원형 큐

class CircularQueue:
    def __init__(self, capacity = 10):
        # 실제 용량은 +1
        # 한 칸은 항상 비워둘라고
        self.capacity = capacity + 1
        self.items = [None] * capacity  # 원형큐 리스트 초기화
        self.front = 0  # 원형 큐의 맨 앞 요소를 가리키는 포인터
        self.rear = 0 # 원형 큐의 맨 뒤 요소를 가리키는 포인터

    def is_empty(self):
        # 서로의 포이터의 위치가 같으면 비어있는 거다.
        return self.front == self.rear

    # 원형큐가 가득찼는 지 확인하는 메서드
    def is_full(self):
        # rear의 +1 에 front가 있으면 큐가 가득찬거다
        # 논리적 순환을 위해서 % 연산자의 나머지를 이용
        return (self.rear + 1) % self.capacity == self.front

    # 원형 큐에 데이터를 삽입하는 메서드
    def enqueue(self, item):
        # 삽입하기 전에 가득찼는 지부터 확인해야 한다.
        if self.is_full():
            raise IndexError("가득참")
        self.rear = (self.rear + 1) % self.capacity
        self.items[self.rear] = item

    # 원형 큐에서 데이터를 추출하는 메서드
    def dequeue(self):
        if self.is_empty():
            raise IndexError("데이터 없음")
        self.front = (self.front + 1) % self.capacity
        item = self.items[self.front]
        self.items[self.front] = None
        return item

    def peek(self):
        if self.is_empty():
            raise IndexError("값이 없다.")
        return self.items[(self.rear + 1) % self.capacity]

    # 현재 원형 큐에 남아있는 항목의 개수를 반환
    def get_size(self):
        return (self.rear - self.front + self.capacity + 1) % self.capacity
