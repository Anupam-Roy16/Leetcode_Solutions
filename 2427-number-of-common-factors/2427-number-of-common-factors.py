class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        x = max(a,b)
        y = min(a,b)
        count = 0
        for i in range(1,int(x**.5)+1):
            if x %i==0:
                if x/i == i:
                    if y%i==0:
                        #print(i)
                        count+=1
                else:
                    if y%i==0 and y%(x//i)==0:
                        count+=2
                        #print(i,x//i)
                    elif y%i==0 or y%(x//i)==0:
                        count += 1
                        #print("qwe")
                    
        return count
            
            
        