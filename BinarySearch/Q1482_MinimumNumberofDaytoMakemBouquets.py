class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        # condition: make m bouquets
        # minimum days to make condition satisfied
        
        def feasible(day):
            bouquet = 0
            num = 0
            for flower in bloomDay:
                if flower <= day:
                    bouquet += 1
                if flower > day:
                    bouquet = 0
                    
                if bouquet == k:
                    bouquet = 0
                    num += 1
                if num >= m: return True
            
            return num >= m
            
        
        left, right = min(bloomDay), max(bloomDay)+1
        while left < right:
            mid = left + (right - left) // 2
            if feasible(mid):
                right = mid
            else:
                left = mid + 1
                
        return -1 if left == max(bloomDay) + 1 else left