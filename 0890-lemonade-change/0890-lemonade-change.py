class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        freq_dic = {}
        for x in bills:
            if x == 5:
                if x in freq_dic:
                    freq_dic[x]+=1
                else:
                    freq_dic[x] = 1
            elif x == 10:
                if 5 in freq_dic and freq_dic[5]:
                    freq_dic[5]-=1
                    if 10 in freq_dic:
                        freq_dic[10]+=1
                    else:
                        freq_dic[10] =1 
                else:
                    return False
            else:
                if 10 in freq_dic and freq_dic[10]!=0 and 5 in freq_dic and freq_dic[5]!=0 :
                        freq_dic[10] -= 1
                        freq_dic[5] -= 1

                        if 20 in freq_dic:
                            freq_dic[20] +=1
                        else:
                            freq_dic[20] =1
                elif 5 in freq_dic and freq_dic[5]>2:
                        freq_dic[5] -=3
                        if 20 in freq_dic:
                            freq_dic[20] +=1
                        else:
                            freq_dic[20] =1
                else:
                    return False 
        return True   





        