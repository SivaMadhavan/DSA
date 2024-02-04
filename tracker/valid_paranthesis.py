class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        for i in range(len(s)):
            currChar = s[i]
            if currChar in ['(', '[', '{']:
                stack.append(s[i])
            else:
                if stack:
                    top = stack.pop()
                    if (currChar == ']' and top != '[') or (currChar == ')' and top != '(') or (currChar == '}' and top != '{'):
                        return False
                    i += 1
        return not stack


input = "(]"
res = Solution().isValid(input)

print(res)