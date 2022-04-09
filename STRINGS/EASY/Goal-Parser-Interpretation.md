## [Goal Parser Interpretation](https://leetcode.com/problems/goal-parser-interpretation/)

* **C++**
```cpp
class Solution {
public:
    string interpret(string command) {
        string ans;
        for(int i = 0; i < command.size();)
        {
            if(command[i] == 'G')
            {
                ans += 'G';
                i++;
            }
            else if(command[i+1] == ')')
            {
                ans += 'o';
                i += 2;
            }
            else
            {
                ans += "al";
                i += 4;
            }
        }
        
        return ans;
    }
};
```

* **Python**
```py
class Solution:
    def interpret(self, command: str) -> str:
        ans = ""
        i = 0
        while i < len(command):
            if command[i] == 'G': 
                ans += 'G'
                i += 1
            elif command[i+1] == ')':
                ans += 'o'
                i += 2
            else:
                ans += 'al'
                i += 4
        return ans
```
