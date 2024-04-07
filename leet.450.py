from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None: return None

        # first we need to find the element
        parent = None
        node = root
        while node and node.val != key:
            parent = node
            if node.val > key:
                node = node.left
            else:
                node = node.right

        if node is None: return root

        # we have the element so we need to get it's replacement
        replacement = None
        if node.right is not None:
            # we need to get the smallest element of the right subtree
            prev = node
            replacement = node.right
            while replacement.left:
                prev = replacement
                replacement = replacement.left

            replacement.left = node.left
            prev.left = replacement.right
            if replacement != node.right:
                replacement.right = node.right           
        elif node.left is not None:
            # we need to find the biggest element of the left subtree
            prev = node
            replacement = node.left
            while replacement.right:
                prev = replacement
                replacement = replacement.right

            replacement.right = node.right
            prev.right = replacement.left
            if replacement != node.left:
                replacement.left = node.left

        if parent is None: return replacement
        
        if parent.val > key:
            parent.left = replacement
        else:
            parent.right = replacement
            
        return root 

def pre(root: Optional[TreeNode]) -> List[int]:
    if root is None: return []
    queue = [root]
    result = []
    while queue:
        curr = queue.pop(0)
        result.append(curr.val)
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)
    return result

sol = Solution()
result = sol.deleteNode(TreeNode(50, TreeNode(30, None, TreeNode(40)), TreeNode(70, TreeNode(60), TreeNode(80))), 50)
print(pre(result))
