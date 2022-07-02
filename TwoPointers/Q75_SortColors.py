class Solution:
    # approach 1: partition twice
    # time: O(n)
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return []
        end = self.partition(nums, 0, len(nums) - 1, 1)
        self.partition(nums, 0, end, 0)
        
    def partition(self, nums, start, end, mid):
        left, right = start, end
        while left <= right:
            while left <= right and nums[left] <= mid:
                left += 1
            while left <= right and nums[right] > mid:
                right -= 1
                
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
                
        return right


    # approach 2: partition once
    # time: O(n)
    def sortColors(self, nums: List[int]) -> None:
        if not nums:
            return nums
        left, idx, right = 0, 0, len(nums)-1
        while(idx <= right):
            if nums[idx] == 0:
                nums[idx], nums[left] = nums[left], nums[idx]
                left += 1
            if nums[idx] == 2:
                nums[idx], nums[right] = nums[right], nums[idx]
                right -= 1
            else: 
                idx += 1
                
                