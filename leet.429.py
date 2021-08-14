from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

        
class Solution(object):
    def recursive(self, node, level, result):
        if node != None:
            if len(result) == level:
                result.append([])
            result[level].append(node.val)
            level += 1
            for child in node.children:
                self.recursive(child, level, result)

    def levelOrder(self, root: 'Node') -> List[List[int]]:
        result = []
        self.recursive(root, 0, result)
        return result
