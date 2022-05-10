## [Combination Sum III](https://leetcode.com/problems/combination-sum-iii/)

* **C++**
```cpp
class Solution {
    vector<vector<int>> ans;
    
public:    
    int sum(vector<int>& combination){
        int res = 0;
        for(auto x: combination)
            res += x;
        return res;
    }
    
    void helper(int k, int n, vector<int>& combination, int num){
        
        if(k == 0){
            if(sum(combination) == n)
                ans.push_back(combination);
            return;
        }
        
        if(num > 9) 
            return;
        
        combination.push_back(num); 
        helper(k - 1, n, combination, num + 1);
        combination.pop_back(); 
        helper(k, n, combination, num + 1);    
        
    }
    
    vector<vector<int>> combinationSum3(int k, int n) {
        vector<int> combination;
        helper(k, n, combination, 1);
        return ans;    
    }
};
```
