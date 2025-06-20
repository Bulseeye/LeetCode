class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # the end connects to the beginning
        globalMax, globalMin = nums[0], nums[0]
        curMax, curMin = 0, 0
        total = 0

        for n in nums:
            # have a min and max and update them both
            curMax = max(curMax + n, n)
            curMin = min(curMin + n, n)
            # count the total of all
            total += n
            # then check if current > global and update as well
            globalMax = max(globalMax, curMax)
            globalMin = min(globalMin, curMin)

        # check if globMax > then 1 if it is check if globmax else just return max 
        # or the total + smallest is bigger 
        if globalMax > 0:
            return max(globalMax, total - globalMin)
        else:
            return globalMax   