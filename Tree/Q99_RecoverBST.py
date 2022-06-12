# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        """
        Algorithm
        ----------
        step1. inorder travers  e the bst --> almost ordered array
        step2. find two swapped items in linear time
        step3. find the swapped items in the bst, ans swapped it
        """
        arr = self.inorderTrav(root)
        print(arr)
        val1, val2 = self.findSwap(arr)
        print(val1, val2)
        self.recover(root, val1, val2)
         
    def inorderTrav(self, root):
        if root:
            return self.inorderTrav(root.left) + [root.val] + self.inorderTrav(root.right)
        else: return []
        
    def findSwap(self, arr):
        maxx = arr[0]
        minn = None
        for i in range(len(arr)):
            if minn == None and arr[i] > maxx: 
                maxx = arr[i]
            elif minn == None and arr[i] < maxx:
                minn = arr[i]
            elif minn != None and arr[i] < minn:
                minn = arr[i]
        return minn, maxx
            
        
    def recover(self, root, val1, val2):
        if root is None:
            return
        
        self.recover(root.right, val1, val2)
        if root.val == val1:
            root.val = val2
        elif root.val == val2:
            root.val = val1
        self.recover(root.left, val1, val2)
        
                    
        