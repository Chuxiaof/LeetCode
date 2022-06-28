class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums:
            return []
        nums.sort()
        ans = []
        pair = ()
        for first in range(len(nums)):
            if first > 0 and nums[first] == nums[first-1]:
                continue
            for second in range(first + 1, len(nums)):
                if second > first + 1 and nums[second] == nums[second-1]:
                    continue
                value = target - nums[first] - nums[second]
                self.twoSum(nums, first, second, value, ans)

        return ans

    def twoSum(self, nums, first, second, value, ans):
        find_set = set()
        pair = ()
        for i in range(second + 1, len(nums)):
            complement = value - nums[i]
            if complement in find_set:
                if (complement, nums[i]) != pair:
                    ans.append(
                        [nums[first], nums[second], complement, nums[i]])
                pair = (complement, nums[i])

            find_set.add(nums[i])
