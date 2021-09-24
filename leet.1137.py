class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        a = 0
        b = 1
        c = 1
        for _ in range(2, n):
            tn = a + b + c
            a, b, c = b, c, tn
        return tn
            