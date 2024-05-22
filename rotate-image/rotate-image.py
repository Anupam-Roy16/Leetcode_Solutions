class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        size = len(matrix)
        i = 0 
        while 1:
            r = size -(i*2)
            if r <=1:
                break
            v1 = []
            v2 =[]
            v3 =[]
            for p in range(r):
                v1.append(matrix[i][i+p])
                matrix[i][i+p] = matrix[size-1-i-p][i]
                if p==r-1:
                    matrix[i][i+p]=v1[0]
                #print(matrix[i][i+p])
            #print(v1)
            for p in range(r):
                v2.append(matrix[i+p][size-1-i])
                matrix[i+p][size-1-i] = v1[p]
                #print(matrix[i+p][size-1-i])
            v2[0] = v1[-1]
            print(v2)
            v2 = v2[::-1]
            for p in range(r):
                v3.append(matrix[size-1-i][i+p])
                matrix[size-1-i][i+p] = v2[p]
                print(matrix[size-1-i][i+p])
            v3[-1] = v2[0]
            print(v3)
            for p in range(r):
                matrix[i+p][i] = v3[p]
                print(matrix[i+p][i])
            i+=1