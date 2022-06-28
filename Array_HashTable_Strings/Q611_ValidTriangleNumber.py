class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        nums.sort()
        count = 0
        for large in range(len(nums)):
            small, mid = 0, large - 1
            while(small < mid):
                if nums[small] + nums[mid] > nums[large]:
                    count += mid - small
                    mid -= 1
                else:
                    small += 1

        return count
