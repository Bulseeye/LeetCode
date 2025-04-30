class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # create new list and fill them with negative values to simulate a max heap
        maxStones = []
        for s in stones:
            s = -s
            maxStones.append(s)
        heapq.heapify(maxStones)
        print(maxStones)

        # as long as we have more then 1 value crush stones
        while len(maxStones) > 1:
            # pop the 2 biggest stones 
            x = heapq.heappop(maxStones)
            y = heapq.heappop(maxStones)

            # [-8, -7, -4, -1, -2, -1]
            #  is - 7 bigger then -8 yes so 8 - 7 = 1 and pus that on the heap
            if y > x:
                heapq.heappush(maxStones, x - y)
        # if all stones are broken we add 0 tot the empty list
        maxStones.append(0)
        return abs(maxStones[0])