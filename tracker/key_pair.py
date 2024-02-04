# User function Template for python3
class Solution:
    def hasArrayTwoCandidates(self, arr, x):
        hashSet = set()
        for i in arr:
            if i in hashSet:
                return "Yes"
            hashSet.add(i)

        return "No"


arr = list(map(int,
               "335 501 170 725 479 359 963 465 706 146 282 828 962 492 996 943 828 437 392 605 903 154 293 383 422 717 719 896 448 727 772 539 870 913 668 300 36 895 704 812 323 334".split()))
target = 468
obj = Solution()
res = obj.hasArrayTwoCandidates(arr, target)
print(res)

