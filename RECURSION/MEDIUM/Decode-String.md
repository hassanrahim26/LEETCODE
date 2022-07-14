## [Decode String](https://leetcode.com/problems/decode-string/)

* **C++**
```cpp
class Solution {
public:
    string solve(int &i, string s){
        int num = 0;
        string word = "";
        
        for(; i < s.length(); i++)
        {
            if(s[i] >= '0' and s[i] <= '9')
                num = num*10 + s[i] - '0';
            
            else if(s[i] == '[')
            {
                string ans = solve(++i, s);
                for(; num > 0; num--)
                    word += ans;
            }
            
            else if(s[i] == ']')
                return word;
            
            else
                word += s[i];
        }
        return word;
    }
    
    string decodeString(string s) {
        int i = 0;
        return solve(i, s);
    }
};
```
