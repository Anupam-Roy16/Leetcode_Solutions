class Solution {
public:
    bool backspaceCompare(string s, string t) {
        stack<char>first;
        stack<char>sec;
        for(int i=0;i<s.size();i++)
        {
            if(s[i]!='#')
            {
                first.push(s[i]);
            }
            else{
                if(!first.empty())
                {
                    first.pop();
                }
            }
        }
        //cout<<first.size()<<endl;
        for(int i=0;i<t.size();i++)
        {
            if(t[i]!='#')
            {
                sec.push(t[i]);
            }
            else{
                if(!sec.empty())
                {
                    sec.pop();
                }
            }
        }
        if(first.size()!=sec.size())
        {
            return 0;
        }
        else{
            while(!first.empty())
            {
                if(first.top()!=sec.top())
                {
                    return 0;
                }
               // cout<<first.top()<<" "<<sec.top()<<endl;
                first.pop();
                sec.pop();
            }
            return 1;
            
        }
        
        
    }
};