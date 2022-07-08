class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if nums is None:
            return []

        result = []
        nums.sort()
        self.dfs(nums, 0, [], result)
        return result

    def dfs(self, nums, start_index, subset, result):
        result.append(subset[:])

        for i in range(start_index, len(nums)):
            if i > start_index and nums[i] == nums[i - 1]:
                continue
            subset.append(nums[i])
            self.dfs(nums, i + 1, subset, result)
            subset.pop()
