from typing import List
import collections
import heapq


class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        e = collections.defaultdict(list)

        for u, v, cnt in edges:
            e[u].append((v,cnt))
            e[v].append((u,cnt))
        
        h = []
        heapq.heappush(h, (0,0))
        inf = float("inf")
        dist = [inf] * n
        dist[0] = 0

        while len(h) >0:
            d, node = heapq.heappop(h)

            if d > dist[node]:
                continue

            for v, cnt in e[node]:
                if dist[v] > d + cnt +1:
                    dist[v] = d + cnt +1
                    heapq.heappush(h, (dist[v], v))

        total = 0
        for i in range(n):
            if dist[i] <= maxMoves:
                total += 1

        for u, v, cnt in edges:
            fromU = max(maxMoves - dist[u],0)
            fromV = max(maxMoves - dist[v], 0)
            total += min(fromU + fromV, cnt)

        return total