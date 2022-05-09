## [Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)

* **C++**
```cpp
class Solution {
public:
    vector<string> mp = {"abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"}, ans;
    
    vector<string> letterCombinations(string digits) {
        if(digits == "")    
            return ans;
        
        string combination = "";
        solve(digits, 0, combination);
        return ans;
    }
    
    void solve(string &digits, int i, string combination){
        if(i == digits.size()){
            ans.push_back(combination);
            return;
        }
        
        for(auto c: mp[digits[i] - '2']){
            combination.push_back(c);
            solve(digits, i + 1, combination);
            combination.pop_back();
        }
    }
};
```
