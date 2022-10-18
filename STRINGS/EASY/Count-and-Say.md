## [Count and Say](https://leetcode.com/problems/count-and-say/)

* **C++**
```cpp
class Solution {
public:
    string countAndSay(int n) {
        if(n == 0)    
            return "";
        string ans = "1";
        while(--n){
            string s = "";
            for(int i = 0; i < ans.size(); i++){
                int count = 1;
                while((i+1 < ans.size()) and (ans[i] == ans[i+1])){
                    count++;
                    i++;
                }
                s += to_string(count) + ans[i];
            }
            ans = s;
        }
        return ans;
    }
};
```
