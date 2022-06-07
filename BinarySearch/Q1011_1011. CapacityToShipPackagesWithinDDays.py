class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # condition: ship all within 'days' days
        # find least k such that the condition is satisfied
        
        def feasible(capacity):
            day = 1
            carry = weights[0]
            for i in range(1, len(weights)):
                if weights[i] + carry > capacity:
                    carry = weights[i]
                    day += 1
                else:
                    carry += weights[i]
            return day <= days
        
        left, right = max(weights), sum(weights)
        
        while left < right:
            mid = left + (right-left) // 2
            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
    
    
        
            
        
        
        
        
        