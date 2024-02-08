from collections import Counter, defaultdict


class Solution:
    def frequencySort(self, s):
        count = Counter(s)
        bucket = defaultdict(list)

        for char, cnt in count.items():
            bucket[cnt].append(char)
        res = ""
        for i in range(len(s), 0, -1):
            for char in bucket.get(i,[]):
                res += char * i

        return res


s = "affadccae"
print(Solution().frequencySort(s))
