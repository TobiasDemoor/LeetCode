class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        hashMap = {}
        for i in range(10):
            for j in range(i, 10):
                hashMap[(str(i), str(j))] = i+j

        m = len(num1)
        n = len(num2)
        result = ""
        if m < n:
            num1 = "0" * (n-m) + num1
        else:
            num2 = "0" * (m-n) + num2
        i = max(n, m) - 1
        carry = False
        while i >= 0:
            aux = tuple(sorted((num1[i], num2[i])))
            val = hashMap[aux] + (1 if carry else 0)
            if val > 9:
                carry = True
                val %= 10
            else:
                carry = False
            result = str(val) + result
            i -= 1
        if carry:
            result = "1" + result
        return result


sol = Solution()
print(sol.addStrings("11", "123"))
print(sol.addStrings("456", "77"))
