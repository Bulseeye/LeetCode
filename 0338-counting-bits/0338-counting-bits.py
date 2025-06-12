class Solution:
    def countBits(self, n: int) -> List[int]:
        # create a bit array
        bitarr = [0] * (n + 1)
        # create an offset and increase when i matches
        offset = 1

        # count how many 1s are in the current number bit representation
        #             8421
        #              4 1 = 5
        # example 5 = 0101 = 2 (1s in there)
        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            bitarr[i] = 1 + bitarr[i - offset]
        return bitarr 
