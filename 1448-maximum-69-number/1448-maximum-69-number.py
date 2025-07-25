class Solution:
    def maximum69Number (self, num: int) -> int:
        converted_str = str(num)
        converted_list = list(converted_str)
        for i in range(len(converted_str)):
            if converted_list[i] == '6':
                converted_list[i] = '9'
                break
        return int("".join(converted_list))
        #return int(converted_list)



        