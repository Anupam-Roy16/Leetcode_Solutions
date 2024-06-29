class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans=""
        x,y = len(a),len(b)
        carry = 0
        if y>x: 
            for i in range(min(x,y)-1,-1,-1):
                if a[i] == '1' and b[i+abs(x-y)] =='1':
                    if carry == 1:
                        ans +='1'
                        carry = 1
                    else:
                        ans+='0'
                        carry = 1
                elif a[i] == '1' and b[i+abs(x-y)] =='0':
                    if carry == 1:
                        ans +='0'
                        carry = 1
                    else:
                        ans+='1'
                        print("asd")
                        carry = 0
                elif a[i] == '0' and b[i+abs(x-y)] =='1':
                    if carry == 1:
                        ans +='0'
                        carry = 1
                    else:
                        ans+='1'
                        carry = 0
                elif a[i] == '0' and b[i + abs(x-y)] =='0':
                    if carry == 1:
                        ans +='1'
                        carry = 0
                    else:
                        ans+='0'
                        carry = 0
        else:
            for i in range(min(x,y)-1,-1,-1):
                if a[i+abs(x-y)] == '1' and b[i] =='1':
                    if carry == 1:
                        ans +='1'
                        carry = 1
                    else:
                        ans+='0'
                        carry = 1
                elif a[i+abs(x-y)] == '1' and b[i] =='0':
                    if carry == 1:
                        ans +='0'
                        carry = 1
                    else:
                        ans+='1'
                        print("asd")
                        carry = 0
                elif a[i+abs(x-y)] == '0' and b[i] =='1':
                    if carry == 1:
                        ans +='0'
                        carry = 1
                    else:
                        ans+='1'
                        carry = 0
                elif a[i+abs(x-y)] == '0' and b[i] =='0':
                    if carry == 1:
                        ans +='1'
                        carry = 0
                    else:
                        ans+='0'
                        carry = 0
            
        #print(carry)
        if x==y:
            if carry == 1:
                ans +='1'
        else:
            p = max(x,y)-min(x,y)
            if x>y:
                #print(carry)
                for i in range(p-1,-1,-1):
                    if a[i]=='1':
                        #print(carry)
                        if carry == 1:
                            #print("u")
                            ans +='0'
                            carry = 1
                            print("as")
                        else:
                            ans +='1'
                            #print("asq")
                    else:
                        if carry == 1:
                            ans+='1'
                            carry =0
                            #print("ws")
                        else:
                            ans +='0'
                if carry==1:
                    ans+='1'
                #print(ans)
            else:
                for i in range(p-1,-1,-1):
                    if b[i]=='1':
                        if carry == 1:
                            ans +='0'
                            carry = 1
                        else:
                            ans +='1'
                    else:
                        if carry == 1:
                            ans+='1'
                            carry =0
                        else:
                            ans +='0'
                if carry==1:
                    ans+='1'
                        
        return ans[::-1]   
            
                