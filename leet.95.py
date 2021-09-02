from typing import List, Optional
from functools import lru_cache


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    @lru_cache
    def generateTrees(self, n: int, offset: int = 0) -> List[Optional[TreeNode]]:
        if n == 0:
            return [None]

        result = []
        nums = list(range(1+offset, n+1+offset))
        for i in range(n):
            val = nums[i]
            for left in self.generateTrees(i):
                for right in self.generateTrees(n-i-1):
                    result.append(TreeNode(val, left, right))
        
        return result


