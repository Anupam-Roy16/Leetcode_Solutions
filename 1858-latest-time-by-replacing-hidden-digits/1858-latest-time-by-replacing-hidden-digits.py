class Solution:
    def maximumTime(self, time: str) -> str:
        converted_list  = list(time)
        if converted_list[0] =='?':
            if converted_list[1] >='0' and converted_list[1] <='3':
                converted_list[0] = '2'
            elif converted_list[1] == '?':
                converted_list[0] = '2'
            else:
                 converted_list[0] = '1'

        if converted_list[1] == '?':
            if converted_list[0] =='2':
                converted_list[1] = '3'
            else:
                converted_list[1] = '9'
        if converted_list[3] == '?':
            converted_list[3] = '5'
        if converted_list[4] == '?':
            converted_list[4] = '9'
        return "".join(converted_list)
        



        