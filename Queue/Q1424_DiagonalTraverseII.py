class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        res = []
        for i, r in enumerate(nums):
            for j, c in enumerate(nums[i]):
                if len(res) > i+j:
                    res[i+j].append(c)
                else:
                    res.append([c])
                 
        ans = []
        
        for i, r in enumerate(res):
            for j, c in enumerate(reversed(res[i])):
                ans.append(c)
                
        return ans
                