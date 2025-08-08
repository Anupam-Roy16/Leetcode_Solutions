class Solution:
    def splitNum(self, num: int) -> int:
        converted_str = list(str(num))

        converted_str.sort()
        size = len(converted_str)
        first_num = []
        sec_num = []
        left , right = 0,1
        flag = 0
        while right<size:
            
            first_num.append(converted_str[left])
            sec_num.append(converted_str[right])
            left+=2
            right+=2
            
        if size %2!=0:
            first_num.append(converted_str[-1])
        first_num  = int("".join(first_num))
        sec_num = int("".join(sec_num))
        print(first_num, sec_num)
        return first_num + sec_num 



        