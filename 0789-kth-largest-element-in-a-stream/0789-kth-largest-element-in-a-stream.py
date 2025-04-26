class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        # turn nums in a minheap so [4,5,8,2] = [2, 4, 8, 5]
        heapq.heapify(self.nums)
        # as long as the heap is bigger then given k pop the smallest value
        while len(self.nums) > k:
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        # push the val to the heap in the correct place
        heapq.heappush(self.nums, val)
        # check if the len heap succeeds k 
        # if it does pop again 
        if len(self.nums) > self.k:
             heapq.heappop(self.nums)

        return self.nums[0]



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)