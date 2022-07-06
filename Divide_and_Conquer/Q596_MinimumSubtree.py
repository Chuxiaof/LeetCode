# Given a binary tree, find the subtree with minimum sum. 
# Return the root of the subtree.

class Solution:
    def findSubtree(self, root):
        
        return

    def find_min_subtree(self, root):
        if not root:
            return
        left_sum = self.find_min_subtree(root.left)
        right_sum = self.find_min_subtree(root.left)
        root_sum = left_sum + right_sum + root.val
        return root_sum
