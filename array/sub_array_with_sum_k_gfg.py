class Solution:

    @staticmethod
    def subArraySum(arr, n, s):
        curSum = left = right = 0
        while right < n or left < n:
            if curSum == s:
                return left+1, right
            elif curSum > s:
                curSum -= arr[left]
                left += 1
            else:
                curSum += arr[right]
                right +=1
        return [-1]
array = list(map(int," 100 36 95 104 12 123 134".split( )))
print(Solution.subArraySum(array, len(array), 468))

