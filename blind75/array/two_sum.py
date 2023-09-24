"""
https://leetcode.com/problems/two-sum/description/
"""


class Solution(object):
    def twoSum(self, nums, target):
        hashMap = {}
        for i in range(len(nums)):
            if target - nums[i] in hashMap:
                return [hashMap[target - nums[i]], i]
            hashMap[nums[i]] = i


print(Solution().twoSum([2,7,11,15], 9))