# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def dfs(p, q):
            if p == None and q == None:
                return True

            if p == None and q is not None or p is not None and q == None:
                return False

            if p.val == q.val:
                left = dfs(p.left,q.left)
                right = dfs(p.right, q.right)

                if left == True and right == True:
                    return True
                elif left == True and right != True or left != True and right == True:
                    return False
            return False

            
        return dfs(p,q)
