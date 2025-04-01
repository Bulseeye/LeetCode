# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n

        while l <= r:
            m = (l + r) // 2
            # if the version is bad it means it should go back.
            if isBadVersion(m):
                res = m
                r = m - 1
            # if the version is ok keep going forward until find the first bad one.
            else:
                l = m + 1
        return res
            
            