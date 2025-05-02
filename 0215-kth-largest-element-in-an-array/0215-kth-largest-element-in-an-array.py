class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxheap = []
        for n in nums:
            maxheap.append(-n)

        heapq.heapify(maxheap)
        # test print(maxheap)

        while k > 1:
            heapq.heappop(maxheap)
            # print(d)
            k -= 1
            
        num = heapq.heappop(maxheap)
        num = - num
        return num