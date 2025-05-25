class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}
        biggest = 0
        
        def dfs(i):
            if i >= len(nums):
                return 0
            if i in cache:
                return cache[i]

            # loops 1, 3, 5 etc
            # then 0 + 2, 4 then return the highest count in the cache
            cache[i] = max(dfs(i + 1), nums[i] + dfs(i + 2))
            return cache[i]

        return dfs(0)

        