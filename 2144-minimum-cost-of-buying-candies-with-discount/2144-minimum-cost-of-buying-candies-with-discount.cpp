class Solution {
public:
    int minimumCost(vector<int>& cost) {
        sort(cost.begin(),cost.end());
        int q=0,p=0,l=cost.size(),i;
        for(i=l-1-2;i>=0;i-=3)
        {
            p+=cost[i];
        }
        for(i=0;i<l;i++)
        {
            q+=cost[i];
        }
        return q-p;
    }
};