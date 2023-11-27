class Solution {
public:
    bool isValid(string s) {
        stack<char>ms;
        for(int i=0;i<s.size();i++)
        {
            if((s[i]=='(') || (s[i] == '{') ||(s[i] == '['))
            {
                ms.push(s[i]);
            }
            else{
                if(ms.empty())
                {
                    ms.push(s[i]);
                }
                else{
                    if((s[i]==')') &&(ms.top()=='('))
                    {
                        ms.pop();
                    }
                    else if((s[i]=='}') &&(ms.top()=='{'))
                    {
                        ms.pop();                       
                    }
                    else if((s[i]==']') &&(ms.top()=='['))
                    {
                        ms.pop();
                    }
                    else{
                        ms.push(s[i]);
                    }
                }
            }
        }
        if(ms.empty())
        {
            return 1;
        }
        else{
            return 0;
        }
    }
};