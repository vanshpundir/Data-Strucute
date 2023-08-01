def two_sum(nums, target):
    num_dict = {}  # Dictionary to store numbers and their indices

    for i, num in enumerate(nums):
        complement = target - num

        # Check if the complement (target - num) is in the dictionary
        if complement in num_dict:
            return [num_dict[complement], i]

        # If not found, add the current number and its index to the dictionary
        num_dict[num] = i

    return None  # If no such pair is found, return None

# Example usage:
nums = [0, 2, 4,5,7,9,12]
target = 9
result = two_sum(nums, target)
if result:
    print(f"The two numbers at indices {result[0]} and {result[1]} add up to the target.")
    print(f"The numbers are {nums[result[0]]} and {nums[result[1]]}.")
else:
    print("No two numbers found that add up to the target.")
