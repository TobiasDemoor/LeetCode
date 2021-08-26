class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        nums = preorder.split(",")
        stack = []
        for n in nums:
            while len(stack) >= 2 and n == "#" and stack[-1] == "#":
                stack.pop()
                if stack.pop() == "#":
                    return False
            stack.append(n)

        return len(stack) == 1 and stack[-1] == "#"


sol = Solution()
assert sol.isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#") == True
assert sol.isValidSerialization("1,#") == False
assert sol.isValidSerialization("9,#,#,1") == False
assert sol.isValidSerialization("1,#,#,#,#") == False
