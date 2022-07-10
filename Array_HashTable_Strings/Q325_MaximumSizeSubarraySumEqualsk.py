class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0

        result = -1
        prefix_sum = 0
        sum_to_index = {0: 0}
        for i in range(len(nums)):
            prefix_sum += nums[i]
            subtract = prefix_sum - k
            if subtract in sum_to_index:
                result = max(result, i - sum_to_index[subtract] + 1)
            if prefix_sum not in sum_to_index:
                sum_to_index[prefix_sum] = i + 1

        return result if result != -1 else 0
