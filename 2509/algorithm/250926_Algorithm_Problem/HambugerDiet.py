

T = int(input())
for test_case in range(1, T+1):
    topping_cnt, limit_k = map(int, input().split())
    # [5, 1000]
    toppings = [list(map(int, input().split())) for _ in range(topping_cnt)]
    # [[100, 200], [300, 500]]
    result = 0


    def dfs(depth, total_score, total_calorie):
        global result

        if limit_k < total_calorie:
            print('###########')
            return

        if depth == topping_cnt:
            result = max(result, total_score)
            print('@@@@@@@@@@@@')
            return

        dfs(depth+1, total_score + toppings[depth][0], total_calorie + toppings[depth][1])

        dfs(depth+1, total_score, total_calorie)
    dfs(0,0,0)
    print(result)


# 1
# 5 1000
# 100 200
# 300 500
# 250 300
# 500 1000
# 400 400