from collections import defaultdict


class Solution:
    def firstUniqChar(self, s: str) -> int:
        mapper = defaultdict(int)
        for c in s:
            mapper[c] += 1

        for i, char in enumerate(s):
            if mapper.get(char) == 1:
                return i

        return -1


inp = "dddccdbba"
res = Solution().firstUniqChar(inp)
print(res)
