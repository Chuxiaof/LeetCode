class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        arr.append(-inf)
        left, right = 0, len(arr) - 2
        while(left + 1 < right):
            print(left, right)
            mid = (left + right) // 2
            if arr[mid] < arr[mid + 1]:
                left = mid
            else:
                right = mid

        if arr[left] > arr[left + 1]:
            return left
        else:
            return right
