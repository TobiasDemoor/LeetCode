# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def recursive(node: TreeNode, branchMax: int) -> int:
            if node == None:
                return 0
            branchMax = max(branchMax, node.val)
            return (1 if branchMax == node.val else 0) + \
                recursive(node.left, branchMax) + \
                recursive(node.right, branchMax)

        return 1 + recursive(root.left, root.val) + recursive(root.right, root.val)
