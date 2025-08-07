T = int(input())
for t in range(1, T+1): # t케이스
    N = int(input()) # 비교할 정수 갯수
    # for n in range(N): # 갯수만큼 수노히
    ai = list(map(int, input().split())) # 비교할 정수들 받고
    min_num = ai[0] # 한개의 값
    max_num = ai[0]
    for a in ai[1:]: # 정수 리스트 순회
        if(min_num>a):
            min_num = a
        if(max_num<a):
            max_num = a
    print(f"#{t} {max_num-min_num}")
