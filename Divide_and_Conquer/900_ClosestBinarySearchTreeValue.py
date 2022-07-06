from lintcode import (
    TreeNode,
)

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """

    def closest_value(self, root: TreeNode, target: float) -> int:
        # write your code here
        lower_bound = self.get_lower_bound(root, target)
        upper_bound = self.get_upper_bound(root, target)

        if lower_bound is None:
            return upper_bound
        if upper_bound is None:
            return lower_bound

        if target - lower_bound <= upper_bound - target:
            return lower_bound
        return upper_bound

    def get_lower_bound(self, root, p):
        if not root:
            return None

        if root.val > p:
            return self.get_lower_bound(root.left, p)
        closer = self.get_lower_bound(root.right, p)

        return closer if closer else root.val

    def get_upper_bound(self, root, p):
        if not root:
            return None

        if root.val < p:
            return self.get_upper_bound(root.right, p)
        closer = self.get_upper_bound(root.left, p)

        return closer if closer else root.val
