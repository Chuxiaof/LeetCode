"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        # print([r.val for r in root.children])
        ans = []
        self.helper(root, ans)
        return ans
    
    def helper(self, root, ans):
        if root:
            ans.append(root.val)
            for c in root.children:
                self.helper(c, ans)
       