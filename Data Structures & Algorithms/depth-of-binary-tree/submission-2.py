# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        dept = 1

        if root == None:
            return 0

        def go(node: TreeNode, depth) -> int:
            leftdept, rightdept = 0,0

            if node.left == None and node.right == None:
                return depth
            if node.left != None:
                leftdept = go(node.left, depth+1)
            if node.right != None:
                rightdept = go(node.right, depth+1)
            
            return max(leftdept,rightdept)

        return go(root, dept)

  
