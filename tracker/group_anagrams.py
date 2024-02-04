from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs):
        result = defaultdict(list)

        for s in strs:
            temp_res = [0] * 26
            for char in s:
                temp_res[ord(char) - ord("a")] += 1
            result[tuple(temp_res)].append(s)

        return result.values()


strs = ["a"]
obj = Solution()
print(obj.groupAnagrams(strs))
