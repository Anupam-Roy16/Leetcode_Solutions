class Solution:
    def binary_search(self,matrix,target):
        left , right = 0,len(matrix)-1
        while left <= right:
            mid = (left+right)//2

            print(matrix[mid])
            
            if matrix[mid] == target:
                return True
            elif matrix[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False


    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        new_linear_matrix = []
        row_size = len(matrix)
        for row in range(row_size):
            new_linear_matrix += matrix[row]
        

        return self.binary_search(new_linear_matrix,target)

     



        