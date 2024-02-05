from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        minSubStr = s
        minLen = len(s)
        for i in range(len(s) - len(t) + 1):
            for j in range(len(t) + i, len(s) + 1):
                curSubStr = s[i:j]
                if len(curSubStr) < minLen and all(char in curSubStr for char in t):
                    minSubStr = curSubStr if len(curSubStr) < len(minSubStr) else minSubStr
                    minLen = len(minSubStr)
                    break
        return minSubStr if all(char in minSubStr for char in t) else ""


s = 'bbaa'
t = 'bba'

res = Solution().minWindow(s, t)
print(res)
