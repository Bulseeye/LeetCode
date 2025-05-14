class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        # if out of bounds or no path
        if grid[rows-1][cols-1] == 1 or grid[0][0] == 1:
            return -1
        
        q = deque([(0, 0, 1)])
        visited = set((0, 0))
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        

        while q:
            r, c,length = q.popleft()
            
            # when we reach the ending return length
            if r == rows -1 and c == cols -1:
                return length
            
            for dr, dc in directions:
                row, col = r + dr, c + dc
                
                # check if the combined direction and row bigger or equal to 0
                # check if the combined direction not out of bounds
                # check if the cell is a 0 and not visited.
                if (row >= 0 and row < rows and 
                    col >= 0 and col < cols and 
                    grid[row][col] == 0 and (row, col) not in visited):
                
                   
                    q.append((row, col, length + 1))
                    visited.add((row, col))
        return -1