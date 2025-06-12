class Solution:
    def countBits(self, n: int) -> List[int]:
        # create a bit array
        bitarr = [0] * (n + 1)
        # create an offset
        offset = 1

        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            bitarr[i] = 1 + bitarr[i - offset]
        return bitarr 
