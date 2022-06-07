class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # condition: eat all bananas, by random order
        # least k such that condition is satisfied        
   
        left, right = 1, max(piles)
        while left < right:
            mid = left + (right - left) // 2
            if sum((bnn + mid - 1) // mid for bnn in piles) <= h:
                right = mid
            else:
                left = mid + 1
                
        return left
        
        