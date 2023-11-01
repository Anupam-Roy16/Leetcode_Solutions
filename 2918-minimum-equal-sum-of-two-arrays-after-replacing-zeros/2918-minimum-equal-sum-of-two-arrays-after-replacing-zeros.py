class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum1,sum2,p,q,d=0,0,0,0,0
        for i in range(len(nums1)):
            if nums1[i]==0:
                p+=1
            sum1+=nums1[i]
        for i in range(len(nums2)):
            if nums2[i]==0:
                q+=1
            sum2+=nums2[i]
        print(sum1,  sum2)
        if sum1==sum2:
            if (p==0 and q!=0) or (q==0 and p!=0):
                return -1
            else:
                p=max(p,q)
                return sum1+p
        elif sum1>sum2:
            d=p+(sum1-sum2)
            if q==0:
                return -1
            elif d<q:
                if p==0:
                    return -1
                else:
                    return q+sum2
            else:
                return sum1+p
                
        else:
            d=q+(sum2-sum1)
            if p==0:
                return -1
            elif d<p:
                if q==0:
                    return -1
                else:
                    return p+sum1
            else:
                return sum2+q
                
            
            