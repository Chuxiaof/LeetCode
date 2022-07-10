class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0

        prefix_sum = 0
        sum_to_count = {0: 1}
        count = 0
        for i in range(len(nums)):
            prefix_sum += nums[i]
            subtract = prefix_sum - k
            count += sum_to_count.get(subtract, 0)
            sum_to_count[prefix_sum] = sum_to_count.get(prefix_sum, 0) + 1

        return count
