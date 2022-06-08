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
        ans, stack = [], [root]
        while stack:
            node = stack.pop()
            if node:
                ans.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
        return ans[::-1]

            