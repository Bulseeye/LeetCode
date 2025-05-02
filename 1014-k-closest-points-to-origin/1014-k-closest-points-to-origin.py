class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []

        for point in points:
            x = point[0]
            y = point[1]

            distance = (x**2) + (y**2)
            # for each point append a list to the minheap list
            minheap.append([distance, x, y])

        # heapify to a minheap
        heapq.heapify(minheap)
        # add the k closest to another list
        res = []

        while k > 0:
            # remember the x and y and append them to the new list
            # this will pop the last elements from the heap and append it to the res
            # until k is 0
            dist, x, y = heapq.heappop(minheap)
            res.append([x, y])
            k -= 1
        return res