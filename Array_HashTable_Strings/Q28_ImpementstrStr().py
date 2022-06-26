class Solution:
    # Approach1: Rabin Karp
    # Time: O(n)
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack is None or needle is None: 
            return -1
        if needle == "": 
            return 0
      
        BASE = 1000000
        m = len(needle)
        power = 1
        for i in range(m):
            power = (power * 31) % BASE
            
        hash_needle = 0
        for j in range(m):
            hash_needle = (hash_needle * 31 + ord(needle[j])) % BASE
            
        hash_haystack = 0
        for k in range(len(haystack)):
            hash_haystack = (hash_haystack * 31 + ord(haystack[k])) % BASE
          
            if k >= m:
                hash_haystack = hash_haystack - (ord(haystack[k - m]) * power) % BASE
                if hash_haystack < 0:
                    hash_haystack += BASE
                
            if hash_haystack == hash_needle:
                if haystack[k - m + 1 : k + 1] == needle:
                    return k - m + 1
                
        return -1      

    # Approach2: Naive
    # Time: O(n^2)
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack is None or needle is None: 
            return -1
        if needle == "": 
            return 0
      
        for i in range(len(haystack) - len(needle) + 1):
            for j in range(len(needle)):
                if haystack[i+j] != needle[j]:
                    break
            else:
                return i
        return -1 