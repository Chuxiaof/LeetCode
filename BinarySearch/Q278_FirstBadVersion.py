# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # left, right = min(search_space), max(search_space)
        # could be [0, n], [1, n] etc. Depends on problem
        left, right = 1, n
        # while left < right:
        while left < right:
            # mid = left + (right - left) // 2
            mid = left + (right - left) // 2
            # if condition(mid):
            # right = mid
            if isBadVersion(mid):
                right = mid

            # else:
                # left = mid + 1
            else:
                left = mid + 1
        # return left
        return left
