class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_product = 1
        post_product = 1
        output = [1] * len(nums)

        for i in range(len(nums)):
            output[i] *= pre_product
            pre_product *= nums[i]

        for j in range(len(nums) - 1, -1, -1):
            output[j] *= post_product
            post_product *= nums[j]

        return output
