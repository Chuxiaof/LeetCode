# O(n**2)
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if nums1 is None or nums2 is None:
            return None
        if not nums1 or not nums2:
            return []

        ans = []
        for num in nums1:
            idx = nums2.index(num)

            for i in range(idx, len(nums2)):
                if nums2[i] > num:
                    ans.append(nums2[i])
                    break
                elif i == len(nums2)-1:
                    ans.append(-1)

        return ans


# O(n)
def nextGreaterElement2(self, nums1: List[int], nums2: List[int]) -> List[int]:
    if nums1 is None or nums2 is None:
        return None
    if not nums1 or not nums2:
        return []

    ans, stack = [], []
    record = {}
    stack.append(nums2[0])

    for num in nums2:
        while stack and num > stack[-1]:
            record[stack.pop()] = num
        stack.append(num)

    while stack:
        record[stack.pop()] = -1

    for num in nums1:
        ans.append(record[num])

    return ans
