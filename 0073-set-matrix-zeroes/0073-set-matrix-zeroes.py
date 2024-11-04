class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        location = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    location.append([i,j])
        for x in location:
            for i in range(len(matrix[0])):
                matrix[x[0]][i] = 0
            for i in range(len(matrix)):
                matrix[i][x[1]] = 0
        
                
                
        