class Solution:
    def containsDuplicate(self, nums):
        hasSet = set()
        for i in nums:
            if i in hasSet:
                return True
            hasSet.add(i)
        return False


obj = Solution()
result = obj.containsDuplicate([2,3,4,5,6])
print(result)