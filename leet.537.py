from typing import Tuple


class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        def strToComplx(num: str) -> Tuple[int, int]:
            aux = num[:-1].split("+")
            return int(aux[0]), int(aux[1])

        a, b = strToComplx(num1)
        c, d = strToComplx(num2)
        return f"{a*c-b*d}+{a*d+c*b}i"

sol = Solution()
print(sol.complexNumberMultiply("1+-1i", "1+-1i"))
