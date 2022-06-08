# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # recursive
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        self.helper(root, ans)
        return ans
        
    def helper(self, root, ans):
        if root:
            ans.append(root.val)
            self.helper(root.left, ans)
            self.helper(root.right, ans)

    # iterative
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack, ans = [root], []
        while stack:
            root = stack.pop()
            if root:
                ans.append(root.val)
                stack.append(root.right)
                stack.append(root.left)
        return ans
        

        
            
        