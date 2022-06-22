class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def profit(x, y):
            return (x+1)/(y+1) - x/y
        
        ratio = []
        
        for a, b in classes:
            heapq.heappush(ratio, (-profit(a,b), a, b))
                  
        for i in range(extraStudents):
            val, a, b = heapq.heappop(ratio)
            heapq.heappush(ratio, (-profit(a+1,b+1), a+1, b+1) )
            
        result = statistics.mean(a/b for d,a,b in ratio)
        # result = sum(a / b for d, a, b in ratio) / len(ratio)       
        return result
            
        