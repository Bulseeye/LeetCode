class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # create a new row of 1s
        prevRow = [1] * n
        col = m
        
        # go through all the rows except last one
        for i in range(m - 1):
            # create new row
            newRow = [1] * n
            # start from second to last element
            for j in range(n - 2, -1, -1):
                #           right     +      down
                newRow[j] = newRow[j + 1] + prevRow[j]
                # update the row to the current
            prevRow = newRow
        # return value from top left
        return prevRow[0]


