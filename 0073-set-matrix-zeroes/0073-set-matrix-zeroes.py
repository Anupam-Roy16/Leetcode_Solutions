class Solution:
    def make_row_zero(self,matrix,i):
        for j in range(len(matrix[0])):
            if matrix[i][j] !=0:
                matrix[i][j] = 2**31
    def make_col_zero(self,matrix,j):
        for i in range(len(matrix)):
            if matrix[i][j] !=0:
                matrix[i][j] = 2**31

    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    self.make_row_zero(matrix,i)
                    self.make_col_zero(matrix,j)
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 2**31:
                    matrix[i][j]=0
        
                
                
        