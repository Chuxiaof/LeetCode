class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1: return x
        
        left, right = 0, x
        while left < right:
            mid = left + (right - left) // 2
            if mid * mid > x:
                right = mid
            else:
                left = mid + 1
                
        return left-1
                