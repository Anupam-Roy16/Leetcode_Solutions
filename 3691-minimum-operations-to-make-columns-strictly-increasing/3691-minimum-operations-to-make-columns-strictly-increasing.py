class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        ans = 0
        for col in range(len(grid[0])):
            current = grid[0][col]
            for row in range(1,len(grid)):
                if current >= grid[row][col]:
                    ans += (current+1-grid[row][col])
                    current +=1
                else:
                    current = grid[row][col]
        return ans



        