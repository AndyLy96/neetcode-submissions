# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return self.helper(root, 1)

    def helper(self, node : Optional[TreeNode], depth : int ) -> int:
        if not node:
            return depth

        if node.left == None and node.right == None:
            return depth
        
        left = self.helper(node.left, depth +1 )
        right = self.helper(node.right, depth+1 )

        return max(left,right)
  
