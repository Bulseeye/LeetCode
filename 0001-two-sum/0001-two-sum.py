class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        curMap = {}

        for i in range(len(nums)):
            lookingfor = target - nums[i]

            if lookingfor in curMap:
                return [i, curMap[lookingfor]]
            
            curMap[nums[i]] = i

        