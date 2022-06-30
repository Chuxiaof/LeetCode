class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if not arr:
            return []
        
        idx = self.find_position(arr, x)
        left, right = idx-1, idx+1
        for _ in range(k-1):
            if left == -1: 
                right += 1
            elif right == len(arr):
                left -= 1
            elif x - arr[left] > arr[right] - x:
                right += 1
            elif x - arr[left] <=  arr[right] - x:
                left -= 1
                
        return arr[left + 1 : right]
        
    def find_position(self, arr, x):
        left, right = 0, len(arr) - 1
        while(left + 1 < right):
            mid = (left + right) // 2
            if arr[mid] < x:
                left = mid
            else:
                right = mid
            
        if x - arr[left] > arr[right] - x:
            return right
        else: 
            return left
        
        