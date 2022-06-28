class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        if not nums1:
            return 0
        
        counter = {}
        ans = 0
        
        for a in nums1:
            for b in nums2:
                counter[a + b] = counter.get(a + b, 0) + 1
            
        for c in nums3:
            for d in nums4:
                target = - c - d
                ans += counter.get(target, 0)
                
        return ans