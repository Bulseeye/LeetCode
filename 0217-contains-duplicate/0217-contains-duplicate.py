class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        countMap = {}

        for num in nums:
            if num not in countMap:
                countMap[num] = 1 
            else:
                return True
        return False