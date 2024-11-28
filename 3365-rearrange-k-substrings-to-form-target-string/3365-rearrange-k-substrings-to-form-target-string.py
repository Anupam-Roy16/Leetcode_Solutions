class Solution:
    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:
        if len(s)%k!=0:
            return False
        temp_list1,temp_list2 = [],[]
        size = len(s)//k
        for i in range(0,len(s),size):
            temp = s[i:i+size]
            temp_list2.append(t[i:i+size])
            temp_list1.append(temp)
        temp_list1.sort()
        temp_list2.sort()
        print(temp_list1,temp_list2)
        if temp_list1 == temp_list2:
            return True
        else:
            return False
        
        
        