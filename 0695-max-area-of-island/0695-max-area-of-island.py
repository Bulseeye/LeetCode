class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid: return 0

        max_area = 0
        visited = set()
        rows, cols = len(grid), len(grid[0])

        def bfs(r, c):
            q = collections.deque()
            visited.add((r, c))
            q.append((r, c))
            area = 1

            directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]

            while q:
                row, col = q.popleft()
                
                for dr, dc in directions:
                    r, c = dr + row, dc + col

                    # not out of bound or visited
                    if (r in range(rows) and
                    c in range(cols) and
                    (r, c) not in visited and
                    grid[r][c] == 1):

                        visited.add((r, c))
                        q.append((r, c))
                        area += 1

            return area

        for r in range(rows):
            for c in range(cols):
                # if land and if row not visited
                if grid[r][c] == 1 and (r, c) not in visited:
                    curr_area = bfs(r, c)
                    if max_area < curr_area:
                        max_area = curr_area
        return max_area