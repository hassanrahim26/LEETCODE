## [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)

* **C++**
```cpp
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
```
* **Python**
```py
class Solution:
    def isValid(self, s: str) -> bool:
        d = {'(':')', '{':'}', '[':']'}
        stack = []
        for i in s:
            if i in d:
                stack.append(i)
            elif len(stack) == 0 or d[stack.pop()] != i:
                return False
        return len(stack) == 0
```
