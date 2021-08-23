# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        valSet = set([])
        def recursive(node: Optional[TreeNode], k: int) -> bool:
            if node != None:
                compl = k- node.val
                if compl in valSet:
                    return True
                valSet.add(node.val)
                if recursive(node.right, k):
                    return True
                if recursive(node.left, k):
                    return True
            return False
        
        return recursive(root, k)