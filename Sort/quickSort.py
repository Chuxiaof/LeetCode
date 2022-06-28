class Solution:
    def sortIntegers(self, s):
        if not s: 
            return
        self.quickSort(s, 0, len(s) - 1)
        

    def quickSort(self, s, start, end):
        if start >= end:
            return
        left, right = start, end
        pivot = start + (end - start) / 2
        while(left <= right):
            while(left <= right and s[left] < s[pivot]):
                left += 1

            while(left <= right and s[right] > s[pivot]):
                right -= 1

            if left <= right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

        self.quickSort(s, start, right)
        self.quickSort(s, left, end)



            

    
