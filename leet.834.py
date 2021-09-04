from typing import List


class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        count = [0] * n
        dist = [0] * n
        def postOrder(node: int, parent: int):
            for child in graph[node]:
                if child == parent:
                    continue
                postOrder(child, node)
                count[node] += count[child]
                dist[node] += dist[child] + count[child]
            count[node] += 1
            
        def preOrder(node: int, parent: int):
            for child in graph[node]:
                if child == parent:
                    continue
                dist[child] = dist[node] + n - count[child]*2
                preOrder(child, node)
        
        for e in edges:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])
        
        postOrder(0, -1)
        preOrder(0, -1)
        return dist

sol = Solution()
print(sol.sumOfDistancesInTree(6, [[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]))
