# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        new = TreeNode(root.val)
        self.helper(root, new)
        return new

    def helper(self, root, new):
        if root:
            if root.left:
                new.right = TreeNode(root.left.val)
            if root.right:
                new.left = TreeNode(root.right.val)
            self.helper(root.left, new.right)
            self.helper(root.right, new.left)
