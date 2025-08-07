Test = int(input())
for test in range(1, Test+1):
    cards = int(input())
    num_card = list(map(int, input())) #49679
    # num_list = [0]*cards
    max_num = 0
    max_nl = 0
    num_list = [0]*int((max(num_card))+1)
    # print(num_card, " 카드들")


    for n_list in num_card:
        num_list[n_list] += 1
        # print(num_list[n_list-1])
    
    max_num = max(num_list)
    max_nl = len(num_list) - 1 - num_list[::-1].index(max_num) 
    for idx, nl in enumerate(num_list):
        if(nl == max()):
            
            # max_nl = max(max_nl, nl)
            # print(nl, max_num)


    print(f"#{test} {max_num} {max_nl}")


        


    #     num_list[n_card]+= 1
    # print(num_list)