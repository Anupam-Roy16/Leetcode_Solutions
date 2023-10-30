class Solution {
public:
    bool check_set(int n,int i)
    {
        int p=1<<i;
        int ans=p&n;
        if (ans)
        {
            return true;
        }
        else{
            return false;
        }
    }
   
    int findKOr(vector<int>& nums, int k) {
        string s="";
        for(int j=0;j<32;j++)
        {
            int u=0;
            for(int i=0;i<nums.size();i++)
            {
                if(check_set(nums[i],j))
                {
                    u++;
                     
                }
            }
           
            if (u>=k)
            {
                s+='1';
            }
            else
            {
                s+='0';
            }
        }
        int r=0;
       
        for(int i=0;i<32;i++)
        {
            if(s[i]=='1')
            {
                r+=(1<<i);
            }
        }
        return r;
            
    }
};