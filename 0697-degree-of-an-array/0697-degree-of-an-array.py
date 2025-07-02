class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        d = {}
        tmp = {}
        maxx1 , maxx2 = -1,-1
        for i in range(len(nums)):
            if nums[i] in d:
                if len(d[nums[i]]) == 1:
                    d[nums[i]].append(i)
                else:
                    d[nums[i]][1] = i
            else:
                d[nums[i]] = [i]
            if nums[i] in tmp:
                tmp[nums[i]] +=1
            else:
                tmp[nums[i]] = 1
        print(tmp)
        def f(x):
            return -x[1]
        tmp = sorted(tmp.items(),key = f)
        flag = -1
        tmp = dict(tmp)
        print(tmp)
        for x in tmp.keys():
            flag = tmp[x]
            break
        minn = 100000000000000000000
        print(flag)
        print(d)
        for x in tmp.keys():
            if flag == tmp[x]:
                #print(x)
                print(d[x][1]-d[x][0])
                if minn>(d[x][1]-d[x][0]):
                    minn = d[x][1]-d[x][0]+1
        print(minn)
        return minn


