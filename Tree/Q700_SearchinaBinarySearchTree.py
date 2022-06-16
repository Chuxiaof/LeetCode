# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Interatve
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        while(root.val != val):
            if val < root.val:
                if root.left:
                    root = root.left
                else:
                    return None
            if val > root.val:
                if root.right:
                    root = root.right
                else:
                    return None

        return root

    # recursive
