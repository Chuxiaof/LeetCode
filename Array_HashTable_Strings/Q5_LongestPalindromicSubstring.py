class Solution:
    # approach1: enumerate all possibilities
    # time: O(n^3)
    def longestPalindrome(self, s: str) -> str:
        if s is None: 
            return None
        
        for length in range(len(s), 0, -1):
            for start in range(0, len(s) - length + 1):
                end = start + length - 1
                print(end, start)
                if self.isPalindrome(s[start:end+1]):
                      return s[start:end+1]
        return ""
                 
    def isPalindrome(self, s):
        left, right = 0, len(s) - 1
     
        while(left < right and s[left].lower() == s[right].lower()):
            left += 1
            right -= 1
    
        return left >= right

    # approach2 : spand around centers
    # time: O(n^2)
    def longestPalindrome(self, s: str) -> str:
        if s is None: 
            return None
        
        longest = self.isPalindrome(s, 0, 0)
        for i in range(len(s)):
            longest = max(longest, self.isPalindrome(s, i, i))
            longest = max(longest, self.isPalindrome(s, i, i+1))
            
        return s[longest[1] : longest[1] + longest[0]]
        
    def isPalindrome(self, s, left, right):
        while(left > -1 and right < len(s) and s[left] == s[right]):
            left -= 1
            right += 1
        
        return (right - left - 1, left + 1)   
            


    
        
        