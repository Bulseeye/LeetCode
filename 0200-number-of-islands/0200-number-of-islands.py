class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
    grid = 
    [
    [0,0] ["1","1","1","1","0"],
    [1,0] ["1","1","0","1","0"],
    [2,0] ["1","1","0","0","0"],
    [3,0] ["0","0","0","0","0"]
    ]
        """
        # if not grid return 0
        if not grid: return 0
        
        # increase rows (up, down) increase cols (left, right)
        rows, cols = len(grid), len(grid[0])
        islands = 0
        visited = set()

        def bfs(r, c):
            # create a q and add item to the visited and q
            q = collections.deque()
            visited.add((r, c))
            q.append((r, c))

            # as long as we have items in the que
            while q:
                # pop from the q but remember the values
                row, col = q.popleft()

                # down, up, left, right
                directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]

                for drow, dcol in directions:
                    # if position + direction not out of bounds
                    # and we found land and we not yet visited
                    r, c = drow + row, dcol + col
                    if (r in range(rows) and
                        c in range(cols) and
                        grid[r][c] == "1" and
                        (r, c) not in visited):
                        q.append((r, c))
                        visited.add((r, c))

        for r in range(rows):
            for c in range(cols):
                # check if land and coords not yet in set
                if grid[r][c] == "1" and (r, c) not in visited:
                    # run bfs and increase island count after
                    bfs(r, c)
                    islands += 1
        return islands

        # time and space complexity
        # O(rows * cols)
