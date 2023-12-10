class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        length = len(grid)
        count = 0
        for i in range(length):
            for j in range(length):
                flag = 0
                for k in range(length):
                    if grid[i][k] != grid[k][j]:
                        flag += 1
                        break
                if flag == 0:
                    count += 1
        return count 