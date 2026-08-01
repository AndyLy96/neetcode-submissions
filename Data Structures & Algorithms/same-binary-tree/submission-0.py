# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        resp = self.build(p)
        resq = self.build(q)

        return resp == resq


    def build(self, node : Optional[TreeNode]):
        res = []
        if not node:
            return res

        res.append(node.val)

        res.append(self.build(node.left))
        res.append(self.build(node.right))

        return res
        

        


