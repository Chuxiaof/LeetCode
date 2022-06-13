class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        Algorithm
        ----------
        1. create an empty max-heap 
        2. add all stone weights to the heap
        3. while heap has 2 or more stones:
                extract top 2 stones
                destroy according to rules
                insert back the resulting stone if needed
        4. return 0 if heap is empty 
            else return last stone on heap
        """
        
        for i in range(len(stones)):
            stones[i] *= -1
        
        heapq.heapify(stones)
        while len(stones) > 1:
            stone_1 = heapq.heappop(stones)
            stone_2 = heapq.heappop(stones)
            if stone_1 != stone_2:
                heapq.heappush(stones, stone_1 - stone_2)
                
        return -heapq.heappop(stones) if stones else 0
        