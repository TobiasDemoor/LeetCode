from typing import List


class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        n = len(releaseTimes)
        maxTime = 0
        maxChar = ""
        i = 0
        last = 0
        while i < n:
            curr = releaseTimes[i] - last
            if curr == maxTime:
                maxChar = max(keysPressed[i], maxChar)
            elif curr > maxTime:
                maxTime = curr
                maxChar = keysPressed[i]
            last = releaseTimes[i]
            i += 1
        return maxChar