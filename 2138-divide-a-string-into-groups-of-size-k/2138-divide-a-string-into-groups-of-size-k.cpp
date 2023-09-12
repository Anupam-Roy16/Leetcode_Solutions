class Solution {
public:
    vector<string> divideString(string s, int k, char fill) {
        int i=0,p,l=s.size();
        vector<string>vs;
        string v;
        while(1)
        { 
             p=0;
            
            for(;i<l;)
            {
                v+=s[i];
                p++;
                if(p==k)
                {
                    vs.push_back(v);
                    i++;
                    v="";
                    break;
                }
                else{
                    i++;
                }
            }
            if(i==l)
            {
                break;
            }
        }
        if(v.size()!=0)
        {
            k-=p;
            for(i=0;i<k;i++)
            {
                v+=fill;
            }
            vs.push_back(v);
        }
      
        return vs;
    }
};