class Solution:
    def search(self, nums, target):
        l, r = 0, len(nums)-1
        while l<=r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid -1
        return -1


inp = [-1,0,3,5,9,12]
obj = Solution()
res = obj.search(inp, 2)

print(res)