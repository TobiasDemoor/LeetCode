from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        reverse = [[] for _ in range(n)]
        for i, j in connections:
            graph[i].append(j)
            reverse[j].append(i)

        visited = [ False ] * n
        stack = [0]
        reverseCount = 0
        while stack:
            curr = stack.pop()
            visited[curr] = True

            for n in reverse[curr]:
                if not visited[n]:
                    stack.append(n)

            for n in graph[curr]:
                if not visited[n]:
                    stack.append(n)
                    reverseCount += 1

        return reverseCount
    
sol = Solution()
print(sol.minReorder(6, [[0,1],[1,3],[2,3],[4,0],[4,5]]))