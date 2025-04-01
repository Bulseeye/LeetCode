class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        maxvalue = 0
        for i in piles:
            if i > maxvalue:
                maxvalue = i
        
        print(maxvalue)
        l, r = 1, maxvalue

        while l <= r:
            mid = (l + r) // 2

            k = 0
            for p in piles:
                # check if the pile / number of piles per hour round up
                # example 3 / 1 = 3hours
                k += math.ceil(p / mid)

            #        m
            # [1, 2, 3, 4, 5, 6]
            # example k = 3 would be number / 3
            # if k perhour smaller than given hour increase k
            # you do this by decreasing k range 
            if k <= h:
                r = mid - 1
            else:
                l = mid + 1
        return l