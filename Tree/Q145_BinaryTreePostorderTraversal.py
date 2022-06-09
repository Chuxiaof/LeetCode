# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # recursive
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        self.helper(root, ans)
        return ans

    def helper(self, root, ans):
        if root:
            self.helper(root.left, ans)
            self.helper(root.right, ans)
            ans.append(root.val)

    # iterative

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans, stack = [], []
        while(True):
            while root and root.left:
                stack.append(root)
