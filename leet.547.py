from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [ False ] * n
        count = 0
        i = 0
        while i < n:
            if not visited[i]:
                count += 1
                stack = [i]
                while stack:
                    curr = stack.pop()
                    visited[curr] = True
                    for j in range(n):
                        if isConnected[curr][j] == 1 and not visited[j]:
                            stack.append(j)
            i += 1
        return count

sol = Solution()
print(sol.findCircleNum([[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]))