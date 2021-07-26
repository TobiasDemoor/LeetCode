class Solution(object):
    def findIntegers(self, n):
        iMax = len("{0:b}".format(n))
        f = [1, 2]
        for i in range(2, iMax):
            f.append(f[i-1] + f[i-2])

        count = 0
        prebit = 0
        i = iMax - 1
        while i >= 0:
            if n & 1 << i:
                count += f[i]
                if prebit == 1:
                    return count
                prebit = 1
            else:
                prebit = 0
            i -= 1

        return count + 1


sol = Solution()
assert sol.findIntegers(5) == 5
assert sol.findIntegers(9) == 7
assert sol.findIntegers(12) == 8
assert sol.findIntegers(1000000000) == 2178309
