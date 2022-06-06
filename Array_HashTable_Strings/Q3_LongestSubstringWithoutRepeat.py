class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last = {}
        i, j, maxx = 0, 0, 0
        for idx, char in enumerate(s):
            if char in last.keys():
                i = max(i, last[char]+1)
                
            last[char] = idx
            print((i,j))
            maxx = max(maxx, j-i+1)
            j += 1
               
        return maxx
                
            
            