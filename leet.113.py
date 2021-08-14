from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def recursive(self, node, acum, path, target, result):
        if node != None:
            acum += node.val
            newPath = path + [node.val]
            if acum == target and node.left == None and node.right == None:
                result.append(newPath)
            else:
                self.recursive(node.left, acum, newPath, target, result)
                self.recursive(node.right, acum, newPath, target, result)

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        self.recursive(root, 0, [], targetSum, result)
        return result
