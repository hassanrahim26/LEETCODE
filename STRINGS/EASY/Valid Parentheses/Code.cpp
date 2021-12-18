/*
PROBLEM LINK:- https://leetcode.com/problems/valid-parentheses/
*/

class Solution {
public:
    bool isValid(string exp) {
        stack<char> s;
        
        for(int i = 0; exp[i] != '\0'; i++)
        {
            if (exp[i] == '{' || exp[i] == '(' || exp[i] == '[')
		    {
			    s.push(exp[i]);
		    }

		    if (exp[i] == '}')
		    {
			    if (!s.empty() && s.top() == '{')
				    s.pop();
			    else
				    return false;
		    }

		    if (exp[i] == ']')
		    {
			    if (!s.empty() && s.top() == '[')
				    s.pop();
			    else
				    return false;
		    }

		    if (exp[i] == ')')
		    {
			    if (!s.empty() && s.top() == '(')
				    s.pop();
			    else
				    return false;
		    }
        }
        
        if(!s.empty())
            return false;
        return true;
    }
};
