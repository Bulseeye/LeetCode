class Solution:
    def climbStairs(self, n: int) -> int:
        def dfs(i, cache):
            # if i is bigger or equal to n
            if i >= n:
                # check if it's the same then return true or 1
                return i == n
            # check if we already encountered the same before
            if i in cache:
                return cache[i]

            # true + true = 2 true + false = 1
            # then cache the current i and return it 
            cache[i] = dfs(i + 1, cache) + dfs(i + 2, cache)
            return cache[i]

        return dfs(0, {})
