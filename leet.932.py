from typing import List


class Solution(object):
    def beautifulArray(self, n: int) -> List[int]:
        ans = [1]
        while len(ans) < n:
            tmp1 = []
            tmp2 = []
            for i in ans:
                aux = i*2-1
                if aux <= n:
                    tmp1.append(aux)
                aux = i*2
                if aux <= n:
                    tmp2.append(aux)
            ans = tmp1 + tmp2
        return ans

sol = Solution()
print(sol.beautifulArray(4))
