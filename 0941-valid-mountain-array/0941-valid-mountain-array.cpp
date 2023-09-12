class Solution {
public:
    bool validMountainArray(vector<int>& arr) {
        int i,p=0,l=arr.size();
        if(l<3)
        {
            return false;
        }
        for(i=1;i<l;i++)
        {
            if(arr[i]==arr[i-1])
            {
                 return false;
            }
            else if((p==0)&&(arr[i]>arr[i-1]))
            {
                
            }
            else if(p==1)
            {
                if(arr[i]>=arr[i-1])
                {
                    return false;
                }
                else{
                    
                }
            }
            else{
                p++;
            }
            
        }
        if(p==0)return false;
        else {
            if(arr[0]>arr[1])return false;
            return true;
        }
    }
};