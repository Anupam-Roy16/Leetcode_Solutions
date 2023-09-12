class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        set<int>p;
        for(int i=0;i<nums.size();i++)
        {
            p.insert(nums[i]);
        }
        if(p.size()==nums.size())
        {
            return false;
        }
        else{
            return true;
        }
    }
};