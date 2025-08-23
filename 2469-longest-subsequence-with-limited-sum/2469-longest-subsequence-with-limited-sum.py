class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:         
        nums.sort()
        prefix_sum_index_map = {}
        prefix_sum = []
        prefix_sum.append(nums[0])
        prefix_sum_index_map[prefix_sum[0]] = 0
        size = len(nums)

        for i in range(1,size):
            prefix_sum.append(nums[i]+prefix_sum[i-1])
            prefix_sum_index_map[prefix_sum[i]] = i
        ans = []
        print(prefix_sum)
        print(prefix_sum_index_map)
        queries1 = queries[:]
        queries1.sort()
        need_dic ={}
        for num in queries1:
            flag = 0
            root = num
           

            while num:
                if num in need_dic:
                    flag = 1
                    need_dic[root] = need_dic[num]
                    break
                if num in prefix_sum_index_map:
                    need_dic[root] = (prefix_sum_index_map[num] +1)
                    flag = 1
                    break
                else:
                    num -=1
                
            if flag ==0:
                need_dic[root] = 0
        print(need_dic)
        for x in queries:
            ans.append(need_dic[x])
        return ans



        