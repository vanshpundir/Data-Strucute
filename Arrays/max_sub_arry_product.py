class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxprod = float('-inf')
        p = 1

        for i in range(len(nums)):
            p = p * nums[i]
            maxprod = max(maxprod, p)
            if (p == 0): p = 1

        p = 1
        for j in range(len(nums) - 1, -1, -1):
            p = p * nums[j]

            maxprod = max(maxprod, p)
            if (p == 0): p = 1
        return maxprod



