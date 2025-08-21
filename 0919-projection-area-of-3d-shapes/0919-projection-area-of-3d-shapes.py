class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        ans = 0
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    count +=1
        ans +=(len(grid)**2-count)

        for arr in grid:
            ans += max(arr)
        
        for i in range(len(grid[0])):
            maxx = -1
            for j in range(len(grid)):
                if maxx < grid[j][i]:
                    maxx = grid[j][i]
            ans += maxx
        return ans


        