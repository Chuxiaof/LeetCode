# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # recursion
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if p and q and p.val == q.val:
                return self.isSameTree(p.left, q.left) and self.isSameTree(p.right,q.right)
        
        if not p and not q: return True
        return False