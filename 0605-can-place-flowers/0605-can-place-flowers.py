class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed_size = len(flowerbed)
        count = 0
        for i in range(flowerbed_size):
            if flowerbed[i] == 0:
                flag = True
                if (i-1)>=0 and flowerbed[i-1] ==1:
                    flag = False
                if (i+1) < flowerbed_size and flowerbed[i+1] ==1:
                    flag = False
                if flag == True:
                    count+=1
                    flowerbed[i] = 1
            elif (i+1)<flowerbed_size and flowerbed[i+1] ==1:
                return False
        print(count)
        if count>=n:
            return True
        else:
            return False


             
        