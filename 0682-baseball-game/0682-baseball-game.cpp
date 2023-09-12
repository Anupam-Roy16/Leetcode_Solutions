class Solution {
public:
    int calPoints(vector<string>& ops) {
        stack<int> p;
        for(auto u:ops)
        {
            if(u=="+")
            {
                int x,y;
                x=p.top();
                p.pop();
                y=p.top();
                y+=x;
                p.push(x);
                p.push(y);
            }
            else if(u=="D")
            {
                int x;
                x=p.top();
                x*=2;
                p.push(x);
            }
            else if(u=="C")
            {
                p.pop();
            }
            else
            {
                 stringstream dege(u);
                 int x;
                 dege>>x;
                 p.push(x);
            }
        }
        int y=0;
        while(!p.empty())
        {
               y+=p.top();
               p.pop();
        }
        return y;
    }
};