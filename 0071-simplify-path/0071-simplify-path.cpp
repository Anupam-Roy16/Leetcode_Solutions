class Solution {
public:
    string simplifyPath(string path) {
        
        
        
        
        
        
        stack<string>ms;
        for(int i=0;i<path.size();i++)
        {
            string s="";
            if((path[i]=='/'))
            {
                continue;
            }
            else if(path[i] == '.')
            {
                if((i+1)>=path.size())
                {
                    break;
                }
                if((path[i+1] == '/'))
                {
                    continue;
                }
                else if(path[i+1]=='.')
                {
                    if((path[i+2]=='/')||(i+2)>=path.size())
                       {
                           if(ms.empty())
                           {
                             continue;
                           }
                           ms.pop();
                       }
                       else
                       {   
                            s="..";
                            i+=2;
                            while(((path[i]!='/'))&&(i<path.size()))
                            {
                                s+=path[i];
                                i+=1;
                            }
                            ms.push(s);
                       }
                }
                else{
                    s=".";
                    i+=1;
                    while(((path[i]!='/'))&&(i<path.size()))
                    {
                        s+=path[i];
                        i+=1;
                    }
                    ms.push(s);
                    }
            }
            
            else{
                
                    while(((path[i]!='/'))&&(i<path.size()))
                    {
                       // cout<<"wewr"<<endl;
                        s+=path[i];
                        i+=1;
                        //cout<<path[i]<<endl;
                    }
                    
                    ms.push(s);
                
            }
           // cout<<s<<endl;
        }
        stack<string>ms1;
        while(!ms.empty())
        {
            ms1.push(ms.top());
            ms.pop();
        }
        string s="";
        while(!ms1.empty())
        {
            s+="/";
            s+=ms1.top();
            ms1.pop();
        }
        if (s.size()==0)
        {
            return "/";
        }
        return s;
                  
                    
              
                
               
         
        
        
        
        
        
        
        
        
        
        
    }
};