class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if nums is None:
            return []
 
        res = []
        nums.sort()
        self.dfs(nums, 0, [], res)
        return res
        
    def dfs(self, nums, index, subset, res):
        if index == len(nums):
            res.append(subset[:])
            return

        subset.append(nums[index])
        self.dfs(nums, index + 1, subset, res)
        
        subset.pop()
        self.dfs(nums, index + 1, subset, res)
