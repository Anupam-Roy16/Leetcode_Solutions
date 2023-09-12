class Solution {
public:
    bool checkValid(vector<vector<int>>& matrix) {
        int i,l,m,j;
        l=matrix.size();
        for(i=0;i<l;i++)
        {
            int a[101]={0};
            for(j=0;j<l;j++)
            {
                if((matrix[i][j]>l)||(matrix[i][j]<1))
                {
                    return false;
                }
                else{
                    a[matrix[i][j]]++;
                }
            }
            for(int k=1;k<=l;k++)
            {
                if(a[k]==0)
                {
                     return false;
                }
            }
            
        }
        for(i=0;i<l;i++)
        {
            int a[101]={0};
            for(j=0;j<l;j++)
            {
                if((matrix[j][i]>l)||(matrix[j][i]<1))
                {
                    return false;
                }
                else{
                    a[matrix[j][i]]++;
                }
            }
            for(int k=1;k<=l;k++)
            {
                if(a[k]==0)
                {
                     return false;
                }
            }
            
        }
        return true;
    }
};