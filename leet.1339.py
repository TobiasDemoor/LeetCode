from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        totals = []
        def defineTotals(node: TreeNode) -> int:
            auxSum = node.val
            if node.left != None:
                auxSum += defineTotals(node.left)
            if node.right != None:
                auxSum += defineTotals(node.right)
            totals.append(auxSum)
            return auxSum
        treeTotal = defineTotals(root)
        aux = treeTotal/2.0
        # find partial sum closest to totalSum/2
        partialTotal =  min(totals[:-1], key= lambda n: abs(aux-n))
        return ((treeTotal-partialTotal) * partialTotal) % (10**9 + 7)
