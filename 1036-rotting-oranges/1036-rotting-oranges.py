class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        time, fresh = 0, 0

        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r, c])

        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = dr+r, dc+c
                    # if out of range or or not fresh skip it
                    if (row < 0 or row > rows -1 or 
                        col < 0 or col > cols -1 or 
                        grid[row][col] != 1):
                        continue
                    # set fresh ones to rotten if in range
                    grid[row][col] = 2
                    q.append([row, col])
                    fresh -= 1
            time += 1
        return time if fresh == 0 else -1