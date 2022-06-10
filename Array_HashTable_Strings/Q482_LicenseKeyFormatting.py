class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        count = 0
        res = []
        s = s.replace("-","").upper()
        
        for char in s:
            res.append(char)
            count += 1
            if (len(s) - count) % k == 0: 
                res.append("-")
        if res and res[-1] == "-": res.pop()    