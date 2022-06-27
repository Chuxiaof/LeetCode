class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s is None:
            return False

        left, right = self.findDiff(s, 0, len(s)-1)
        if left >= right:
            return True

        return self.isPalindrome(s, left+1, right) or self.isPalindrome(s, left, right-1)

    def findDiff(self, s, left, right):
        while(left < right and s[left] == s[right]):
            left += 1
            right -= 1
        return left, right

    def isPalindrome(self, s, left, right):
        left, right = self.findDiff(s, left, right)
        return left >= right
