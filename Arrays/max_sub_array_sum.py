def max_sub_array_sum(nums):
    maxSum = float("-inf")
    c = 0

    for i in range(len(nums)):
        c = max(nums[i], c+nums[i])
        maxSum = max(maxSum,  c)


    return maxSum
list1 = [5,4,-1,7,8]
list12 = [4,9,8,-1, 0,2,3]

print(max_sub_array_sum(list1))