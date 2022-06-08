class Solution:

    # recursive O(n)
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        self.helper(root, ans)
        return ans
    
    def helper(self, root, ans):
        if root:
            self.helper(root.left, ans)
            ans.append(root.val)
            self.helper(root.right, ans)


    # iterative
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans, stack = [], []

        while(root or stack):
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            ans.append(root.val)
            root=root.right

        return ans

            