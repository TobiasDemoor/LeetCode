from collections import defaultdict, deque
from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends: return -1
        
        queue = deque([(0, "0000")])
        visited = defaultdict(lambda: False)
        visited["0000"] = True
        while queue:
            count, curr = queue.popleft()            
            if curr == target: return count
            count += 1
            for i in range(4):
                for d in [-1,1]:
                    nxt = curr[:i] + str((int(curr[i]) + d) % 10) + curr[i+1:]
                    if not visited[nxt] and nxt not in deadends:
                        visited[nxt] = True
                        queue.append((count, nxt))
        return -1

sol = Solution()
print(sol.openLock(["8888"], "0009"))