class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # if 1 (obstacle) return 0
        # if out of bounds return 0
        # if 0 move and set to down + right
        # stop at  -1, -1

        # rows and cols in grid
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        # map the ending coords key : value (memoization)
        mapping = {(rows -1, cols -1): 1}

        def dfs(r, c):
            if r == rows or c == cols or obstacleGrid[r][c] == 1:
                return 0
            if (r, c) in mapping:
                return mapping[(r, c)]
            #replace 0 with possible path and return right, down
            mapping[(r, c)] = dfs(r + 1, c) + dfs(r, c + 1)
            return mapping[(r, c)]

        return dfs(0, 0)
            
