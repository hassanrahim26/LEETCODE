## [Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/)

* **C++**
```cpp
class Solution {
public:
    int evalRPN(vector<string>& tokens) {
	stack<long long> s;
	for(auto& t : tokens){
            if(t == "+" || t == "-" || t == "*" || t == "/") {
	        long long op1 = s.top(); s.pop();
	        long long op2 = s.top(); s.pop();
	        if(t == "+") op1 = op2 + op1; 
	        if(t == "-") op1 = op2 - op1;
	        if(t == "/") op1 = op2 / op1;
	        if(t == "*") op1 = op2 * op1;   
                s.push(op1);
	    }
            else 
                s.push(stoll(t));     
        }
	return s.top(); 
    }
};
```
