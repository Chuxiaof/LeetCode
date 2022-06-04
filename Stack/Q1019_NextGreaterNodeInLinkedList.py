# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        if not head: return []
        
        index = 0
        stack, ans = [[index, head.val]], []
        head = head.next
        
        while head:
            ans.append(0)
            while stack and head.val > stack[-1][1]:
                ans[stack[-1][0]] = head.val
                stack.pop()
            index += 1
            stack.append([index, head.val])
            head = head.next

        ans.append(0)
  
        return ans
      
        