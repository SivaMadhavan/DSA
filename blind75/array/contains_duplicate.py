class Solution:
    def containsDuplicateBrute(self, nums):
        n = len(nums)
        for i in range(n-1):
            for j in range(i+1, n):
                if nums[i] == nums[j]:
                    return True
        return False

    def containsDuplicate(self, nums):
        hasSet = set()
        for i in nums:
            if i in hasSet:
                return True
            hasSet.add(i)
        return False