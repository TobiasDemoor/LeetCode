from typing import List


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        maxSize = 1
        current = 1
        less = True
        i = 1
        while i < n:
            if (less and arr[i-1] < arr[i]) or (not less and arr[i-1] > arr[i]):
                less = not less
                current += 1
            else:
                maxSize = max(maxSize, current)
                while i < n and arr[i-1] == arr[i]:
                    i += 1
                if i < n:
                    less = arr[i-1] > arr[i]
                    current = 2
            i += 1
        maxSize = max(maxSize, current)
        return maxSize
