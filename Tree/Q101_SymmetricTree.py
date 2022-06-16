class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root, root)
        
    def helper(self, l, r):
        if l and r:
            return l.val == r.val and self.helper(l.left, r.right) and self.helper(l.right, r.left)
        elif l or r: 
            return False
        else: return True