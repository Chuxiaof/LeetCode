# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        return self.helper(root, low=-math.inf, high=math.inf)

    def helper(self, root, low, high):
        if not root:
            return True
        if low >= root.val or high <= root.val:
            return False
        else:
            return self.helper(root.left, low, root.val) and self.helper(root.right, root.val, high)
