from typing import List

class Solution:
    def removeHeapRoot(self, heap):
        n = len(heap) - 1
        if n == 0:
            return heap.pop()
        result = heap[0]
        heap[0] = heap.pop()
        i = 0
        while i * 2 + 1 < n:
            left = heap[i * 2 + 1][2]
            if i * 2 + 2 < n:
                right = heap[i * 2 + 2][2]
            else:
                right = left + 1
            if left < right:
                if left < heap[i][2]:
                    heap[i], heap[i * 2 + 1] = heap[i * 2 + 1], heap[i]
                    i = i * 2 + 1
                else:
                    break
            else:
                if right < heap[i][2]:
                    heap[i], heap[i * 2 + 2] = heap[i * 2 + 2], heap[i]
                    i = i * 2 + 2
                else:
                    break
        return result

    def addToHeap(self, heap, element):
        n = len(heap) + 1
        heap.append(element)
        i = n - 1
        while i > 0:
            j = (i-1) // 2
            if heap[i][2] < heap[j][2]:
                heap[i], heap[j] = heap[j], heap[i]
                i = j
            else:
                break


    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        # bfs
        m = len(maze)     # max row value
        n = len(maze[0])  # max col value
        visited = [ [ False ] * n for _ in range(m)]
        priorityQueue = [(entrance[0], entrance[1], 0)]
        while priorityQueue:
            row, col, step = self.removeHeapRoot(priorityQueue)
            # check for success
            if row == 0 or row == m - 1 or col == 0 or col == n - 1:
                if row != entrance[0] or col != entrance[1]:
                    return step
            visited[row][col] = True
            step += 1
            if col > 0 and not visited[row][col-1] and maze[row][col-1] == '.':
                self.addToHeap(priorityQueue, (row, col-1, step))
            if col < n-1 and not visited[row][col+1] and maze[row][col+1] == '.':
                self.addToHeap(priorityQueue, (row, col+1, step))
            if row > 0 and not visited[row-1][col] and maze[row-1][col] == '.':
                self.addToHeap(priorityQueue, (row-1, col, step))
            if row < m-1 and not visited[row+1][col] and maze[row+1][col] == '.':
                self.addToHeap(priorityQueue, (row+1, col, step))
        return -1
    
sol = Solution()
print(sol.nearestExit(
    [[".","+","+","+",".",".",".","+","+"], # 0
     [".",".","+",".","+",".","+","+","."], # 1
     [".",".","+",".",".",".",".",".","."], # 2
     [".","+",".",".","+","+",".","+","."], # 3
     [".",".",".",".",".",".",".","+","."], # 4
     [".",".",".",".",".",".",".",".","."], # 5, 6->7->8
     [".",".",".","+",".",".",".",".","."], # 6
     [".",".",".",".",".",".",".",".","+"], # 7
     ["+",".",".",".","+",".",".",".","."]], [5,6]
    ))