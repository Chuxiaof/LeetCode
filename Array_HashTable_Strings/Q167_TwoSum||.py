class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = {}
        for idx, num in enumerate(numbers):
            if target - num in d.keys():
                return [d[target - num] + 1, idx + 1]
            if num not in d.keys():
                d[num] = idx
