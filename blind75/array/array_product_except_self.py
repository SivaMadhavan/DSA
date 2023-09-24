class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        result = [1] * n
        prefix = postfix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]
        for i in range(n-1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]
        return result