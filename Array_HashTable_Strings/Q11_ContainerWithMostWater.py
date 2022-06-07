class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxx = 0
        s, f = 0, len(height)-1
        
        while f>s:
            maxx = max(maxx, (f-s) * min(height[f], height[s]))
            if height[f] >= height[s]:
                s += 1
            else:
                f -= 1
            
        return maxx
            