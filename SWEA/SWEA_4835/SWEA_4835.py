Test_case = int(input())

for test in range(1, Test_case+1):
    A = 0
    N, M = map(int, input().split())
    Num_list = list(map(int, input().split()))
    max_num = sum(Num_list[0:M])
    min_num = sum(Num_list[0:M])
    for n in range(N+1):
        if(n>=M):
            A+=1
            # print(A, "AAA")
            num = 0

            for m in range(M):
                num += (Num_list[(n-1)-m])
                # print(Num_list[(n-1)-m], "넘 리스트")
            max_num = max(num , max_num)
            # print(max_num)
            min_num = min(num, min_num)
            # print(min_num)

    print(f"#{test} {max_num-min_num}")