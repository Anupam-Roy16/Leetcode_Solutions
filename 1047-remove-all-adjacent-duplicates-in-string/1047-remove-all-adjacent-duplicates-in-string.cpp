class Solution {
public:
    string removeDuplicates(string s) {
        int k,l,i,q=s.size();
        stack<char>p;
        for(auto u:s)
        {
            if(p.empty()!=1)
            {
                if(p.top()==u)
                {
                    p.pop();
                }
                else{
                    p.push(u);
                }
            }
            else{
                p.push(u);
            }
        }
        k=p.size();
       s.clear();
        while(k--)
        {
            s+=p.top();
            p.pop();
        }
       reverse ( s.begin(), s.end() );
      return s;
    }
};