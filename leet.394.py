class Solution:
    def decodeString(self, s: str) -> str:
        n = len(s)
        stack = []
        memo = ['']
        i = 0
        while i < n:
            if s[i] in ['1','2','3','4','5','6','7','8','9']:
                numberStr = s[i]
                i += 1
                while s[i] != '[':
                    numberStr += s[i]
                    i += 1
                stack.append(int(numberStr))
                memo.append('')
            elif s[i] == ']':
                string = memo.pop() * stack.pop()
                memo[-1] += string
            else:
                memo[-1] += s[i]
            i += 1
        return memo[0]

sol = Solution()
print(sol.decodeString("3[a]2[bc]"))
print(sol.decodeString("2[abc]3[cd]ef"))