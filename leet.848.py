from typing import List

class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        n = len(shifts)
        result = ""
        base = ord('a')
        acum = -base
        for i in range(n-1, -1, -1):
            acum += shifts[i]
            result = chr((ord(s[i]) + acum) % 26 + base) + result
        return result

