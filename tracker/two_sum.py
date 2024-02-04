class Solution(object):
    def twoSum(self, nums, target):
        hashMap = {}
        for i in range(len(nums)):
            if target - nums[i] in hashMap:
                return [hashMap[target - nums[i]], i]
            hashMap[nums[i]] = i


obj = Solution()
print(obj.twoSum([2,3,4,5,7], 14))