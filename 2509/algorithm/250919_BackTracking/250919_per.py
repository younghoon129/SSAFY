def find_subsets(idx, num_sum, num_sum_list):
    global result
    if num_sum == target_sum:
        result.append(num_sum_list)
        return
    if num_sum >= target_sum: return
    if idx == len(nums):
        return
    find_subsets(idx+1, num_sum + nums[idx], num_sum_list + [nums[idx]])
    find_subsets(idx+1, num_sum, num_sum_list)


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target_sum = 10
result= []

find_subsets(0, 0, [])
print(result)