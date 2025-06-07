class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        # check if we still have a 1 remaining
        while n > 0:
            # only if n digit is 1 increase count
            if n % 2 == 1:
                count += 1
                # bit shift
            n = n >> 1
        return count



