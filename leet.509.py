class Solution:
    def fib(self, n: int) -> int:
        # tail recursion
        def go(n, a, b):
            if n == 1:
                return b
            else:
                return go(n-1, b, a+b)
        if n == 0:
            return 0
        return go(n,0,1)