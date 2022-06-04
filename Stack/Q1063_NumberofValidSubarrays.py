class Solution:
    def validSubarrays(self, nums: List[int]) -> int:        
        stack = []
        count = 0
        
        for idx, num in enumerate(nums):
            while stack and num < nums[stack[-1]]:
                count += idx - stack.pop()

            stack.append(idx)
            
        while stack:
            count += idx+1-stack.pop()
            
        return count
        