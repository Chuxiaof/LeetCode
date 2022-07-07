# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.flatten_btree(root)
        
    def flatten_btree(self, root):
        if not root:
            return None
        
        left_end = self.flatten_btree(root.left)
        right_end = self.flatten_btree(root.right)
        
        if left_end:
            left_end.right = root.right
            root.right = root.left
            root.left = None
        
        return right_end or left_end or root
        
        
        