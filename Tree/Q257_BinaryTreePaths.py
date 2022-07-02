# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        path, paths = [root], []
        self.dfs(root, path, paths)
        return paths

        if not root:
            return
        if not root.left and not root.right:
            paths.append("->".join(str(node.val) for node in path))

        path.append(root.left)
        self.dfs(root.left, path, paths)
        path.pop()

        path.append(root.right)
        self.dfs(root.right, path, paths)
        path.pop()
