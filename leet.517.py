from collections import defaultdict

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        n = len(ring)
        m = len(key)
        memo = {}
        # pregenerate map
        mpp = defaultdict(lambda: [])
        for i, c in enumerate(ring): mpp[c].append(i)

        def recursiveImpl(curr: int, target: int) -> int:
            if target == m: return 0
            if (curr, target) in memo: return memo[(curr, target)]
            minSteps = float('inf')
            for i in mpp[key[target]]:
                a, b = curr, i
                if a < b: a, b = b, a
                steps = min((b - a) % n, a - b)
                minSteps = min(minSteps, steps + recursiveImpl(i, target + 1))
            memo[(curr, target)] = minSteps + 1
            return minSteps + 1

        return recursiveImpl(0, 0)



sol = Solution()
assert(sol.findRotateSteps("godding", "gd") == 4)
assert(sol.findRotateSteps("pqwcx", "cpqwx") == 13)