# 첫번째 풀이방법
# 자석의 회전방향을 모두 고려한 뒤, 회전방향에 따라서 한 번에 점수를 획득하는 방식

from collections import deque

# def rotate_magnet(mag, rot, visited):
#     if visited[mag] != 0: return
#
#     visited[mag] = rot
#
#     if mag == 0:
#         if magnet_list[mag][2] != magnet_list[mag+1][6]:
#             rotate_magnet(mag + 1, -rot, visited)
#
#     elif mag == 3:
#         if magnet_list[mag][6] != magnet_list[mag-1][2]:
#             rotate_magnet(mag - 1, -rot, visited)
#
#     else:
#         if magnet_list[mag][2] != magnet_list[mag+1][6]:
#             rotate_magnet(mag + 1, -rot, visited)
#         if magnet_list[mag][6] != magnet_list[mag-1][2]:
#             rotate_magnet(mag - 1, -rot, visited)
#
#
# T = int(input())
#
# for test_case in range(1, T + 1):
#     K = int(input())
#     n = 4
#     magnet_list = [deque(list(map(int, input().split()))) for _ in range(n)]
#     rotate_info_list = [list(map(int, input().split())) for _ in range(K)]
#     score_sum = 0
#
#     for rotate_info in rotate_info_list:
#         # print(rotate_info)
#         magnet_num, rotate_dir = rotate_info
#
#         visited = [0] * n
#
#         rotate_magnet(magnet_num-1, rotate_dir, visited)
#
#         for i, v in enumerate(visited):
#             # if v == 1:
#             #     pop_data = magnet_list[i].pop()
#             #     magnet_list[i].appendleft(pop_data)
#             # elif v == -1:
#             #     pop_data = magnet_list[i].popleft()
#             #     magnet_list[i].append(pop_data)
#             magnet_list[i].rotate(v)
#
#     score_list = [1, 2, 4, 8]
#     for i in range(n):
#         if magnet_list[i][0] == 1:
#             score_sum += score_list[i]
#
#     print(f"#{test_case} {score_sum}")

# ==========================================================================================

# 2번 풀이
# BFS? 느낌

# T = int(input())
#
# for test_case in range(1, T + 1):
#     K = int(input())
#     n = 4
#     magnet_list = [deque(list(map(int, input().split()))) for _ in range(n)]
#     rotate_info_list = [list(map(int, input().split())) for _ in range(K)]
#     score_sum = 0
#     RIGHT_POS, LEFT_POS, ARROW_POS = 2, 6, 0
#
#     for rotate_info in rotate_info_list:
#         magnet_num, rotate_dir = rotate_info
#         queue = deque()
#         queue.append([magnet_num-1, rotate_dir])
#         visited = [False] * n
#         visited[magnet_num - 1] = True
#         while queue:
#             mag_idx, rotate = queue.popleft()
#
#             if mag_idx != n-1:
#                 if magnet_list[mag_idx][RIGHT_POS] != magnet_list[mag_idx + 1][LEFT_POS]:
#                     if not visited[mag_idx + 1]:
#                         queue.append([mag_idx + 1, -rotate])
#                         visited[mag_idx+1] = True
#
#             if mag_idx != 0:
#                 if magnet_list[mag_idx][LEFT_POS] != magnet_list[mag_idx - 1][RIGHT_POS]:
#                     if not visited[mag_idx - 1]:
#                         queue.append([mag_idx - 1, -rotate])
#                         visited[mag_idx - 1] = True
#
#             magnet_list[mag_idx].rotate(rotate)
#
#     for idx, magnet in enumerate(magnet_list):
#         if not magnet[ARROW_POS]: continue
#         score_sum += (2 ** idx)
#
#     print(f"#{test_case} {score_sum}")

# ==========================================================================================

T = int(input())

def dfs(mag_idx, rot, visited):
    if mag_idx != n - 1:
        if magnet_list[mag_idx][RIGHT_POS] != magnet_list[mag_idx + 1][LEFT_POS]:
            if not visited[mag_idx + 1]:
                visited[mag_idx+1] = True
                dfs(mag_idx + 1, -rot, visited)

    if mag_idx != 0:
        if magnet_list[mag_idx][LEFT_POS] != magnet_list[mag_idx - 1][RIGHT_POS]:
            if not visited[mag_idx - 1]:
                visited[mag_idx - 1] = True
                dfs(mag_idx - 1, -rot, visited)

    magnet_list[mag_idx].rotate(rot)


for test_case in range(1, T + 1):
    K = int(input())
    n = 4
    RIGHT_POS, LEFT_POS, ARROW_POS = 2, 6, 0
    magnet_list = [deque(list(map(int, input().split()))) for _ in range(n)]
    rotate_info_list = [list(map(int, input().split())) for _ in range(K)]
    score_sum = 0
    for rotate_info in rotate_info_list:
        magnet_num, rotate_dir = rotate_info
        visited = [False] * n
        visited[magnet_num - 1] = True
        dfs(magnet_num - 1, rotate_dir, visited)

    for idx, magnet in enumerate(magnet_list):
        if not magnet[ARROW_POS]: continue
        score_sum += (2 ** idx)

    print(f"#{test_case} {score_sum}")