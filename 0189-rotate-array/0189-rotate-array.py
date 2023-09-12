class Solution:
    def invert(self,nms,i,j):
        while i<j:
            temp=nms[i]
            nms[i]=nms[j]
            nms[j]=temp
            i+=1
            j-=1
            
            
        
    def rotate(self, nums: List[int], k: int) -> None:
        k=k%len(nums)
        n=len(nums)-k-1
        m=len(nums)-k
        self.invert(nums,0,n)
        self.invert(nums,m,len(nums)-1)
        self.invert(nums,0,len(nums)-1)