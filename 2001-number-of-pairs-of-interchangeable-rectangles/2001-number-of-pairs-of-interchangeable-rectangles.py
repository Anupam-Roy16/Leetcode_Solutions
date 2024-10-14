class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        temp = []
        for i in range(len(rectangles)):
            temp.append(rectangles[i][0]/rectangles[i][1])
        
        temp_dict1,temp_dict2 ={},{}
        for i in range(len(temp)):
            if temp[i] not in temp_dict1:
                temp_dict1[temp[i]] =1
                temp_dict2[(temp[i],i)] = 1
            else:
                temp_dict1[temp[i]] +=1
                temp_dict2[(temp[i],i)] = temp_dict1[temp[i]]
        ans  =0
        for i in range(len(temp)):
            ans += (temp_dict1[temp[i]]-temp_dict2[(temp[i],i)])
        return ans
                
        
        
        
        