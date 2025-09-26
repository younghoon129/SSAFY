# 첫번째 풀이방법
# 자석의 회전방향을 모두 고려한 뒤, 회전방향에 따라서 한 번에 점수를 획득하는 방식
T = int(input())

for test_case in range(1, T+1):
    K = int(input())
    n = 4
    magnet_list = [list(map(int, input().split())) for _ in range(n)]
    rotate_info_list = [list(map(int, input().split())) for _ in range(K)]
    score_sum = 0

    for rotate_info in rotate_info_list:
        magnet_num, rotate_dir = rotate_info
        
        visited = [0] * n

        rotate_magnet()



    print(f"#{test_case} {score_sum}")