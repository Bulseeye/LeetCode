class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        print(n)
        for i in range(32):
            # if n = 1 and 1 == 1 if n = 0 and 1 == 0
            bit = n & 1
            # result = result shift by 1 or return the bit
            print(result) 
            result = (result << 1) | bit
            # each itteration shift to the right
            n >>= 1
        return result