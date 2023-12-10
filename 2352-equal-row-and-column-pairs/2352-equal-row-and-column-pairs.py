class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        length = len(grid)
        col_dic = {}
        row_dic = {}
        count = 0
        for i in range(length):
            temp_list = []
            row_dic[i]=grid[i]
            for j in range(length):
                temp_list.append(grid[j][i])
            col_dic[i] = temp_list
        for i in range(length):
            for j in range(length):
                if row_dic[i] == col_dic[j]:
                    count += 1
        return count   
       