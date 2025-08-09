class Solution:
    def find_avg(self,i,j,img):
        row = i - 1
        col = j - 1
        ans,count = 0,0
        for i in range(row,row+3):
            for j in range(col,col+3):
                if 0<=i<len(img) and 0<=j<len(img[0]):
                    ans += img[i][j]
                    count +=1
        return ans//count

        

    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        row = len(img)
        col = len(img[0])
        ans = []
        for i in range(row):
            tmp = []
            for j in range(col):
                tmp.append(self.find_avg(i,j,img))
            ans.append(tmp)
        return ans

        