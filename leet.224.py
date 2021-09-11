class Solution:
    def calculate(self, s: str) -> int:
        n = len(s)
        sign = 1
        totalSum = 0
        stack = []

        i = 0
        while i < n:
            if s[i].isnumeric():
                num = 0
                while i < n and s[i].isnumeric():
                    num = num*10 + int(s[i])
                    i += 1
                totalSum += num*sign
                print(num)
                i -= 1
            elif s[i] == "+":
                sign = 1
            elif s[i] == "-":
                sign = -1
            elif s[i] == "(":
                stack.append(totalSum)
                stack.append(sign)
                totalSum = 0
                sign = 1
            elif s[i] == ")":
                totalSum = stack.pop() * totalSum
                totalSum += stack.pop()
            i += 1
        return totalSum
