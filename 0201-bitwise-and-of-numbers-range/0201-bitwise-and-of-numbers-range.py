class Solution:
    #intution is if one bit is 0 of nth bit then the resultant bit of that position is 0.  ist bit is changed by one position , 2nd bit is changed by two position , 3rd bit is changed by four position and 4rth bit is changed by 8 position. by this we find minimum diffrence . 
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        diff = right - left
        n = 1
        if diff == 0:
            return left
        while 1:
            if left <= 2**(n)-1:
                break
            else:
                n += 1
        m = 1
        while 1:
            if right <= 2**(m)-1:
                break
            else:
                m += 1
        i = 32
        while 1:
            if 2**(i) <= diff:
                break
            else:
                i -= 1
       # p  ,q  = n,m
        m = max(n,m)
       
        g = i+1
        #print(g,m)
        #print(m,g)
        if m <= g:
            return 0
        else:
            ans =0
            while 1:
                #print(p,q,g)
                print((left & 1<<g),(right & 1<<g))
                if (left & 1<<g) != (right & 1<<g):
                    ans +=0
                   # print('fhjsf')
                elif (left & 1<<g) !=0:
                    ans +=(2**g)
                   # print('hjsf')
                    
                #ans +=(2**g)
                g+=1
                if g == m:
                    break
            return ans
            

            
            
            
        
        
                
                
            

            
        