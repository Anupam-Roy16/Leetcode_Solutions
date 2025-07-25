class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        summation = sum(arr)
        if summation%3!=0:
            return False
        else:
            summation /=3
            tmp = 0
            flag1 ,flag2,flag3= False ,-1,-1
            for i in range(len(arr)):
                tmp+=arr[i]
                if tmp == (summation):
                    flag2 = i
                    flag1 = True
                    #print("sddf")
                    break
           # print(flag1)
            if flag1 == False:
                print("sdf")
                return False
            else:
                tmp = 0
                for i in range(len(arr)-1,-1,-1):
                    tmp+=arr[i]
                    if tmp == (summation):
                        if i > flag2+1:
                            return True
                        else:
                            return False
                return False
            

                

        