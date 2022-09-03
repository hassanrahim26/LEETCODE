## [Numbers With Same Consecutive Differences](https://leetcode.com/problems/numbers-with-same-consecutive-differences/)

* **C++**
```cpp
class Solution {
public:
    vector<int> ans;
    void solve(int len, int &k, int num, int digit){
        if(len == 0){
            ans.push_back(num);
            return;
        }
        for(int i = 0; i < 10; i++){
            if(abs(i - digit) == k)
                solve(len-1, k, num*10 + i, i);
        }
    }
    
    vector<int> numsSameConsecDiff(int n, int k) {
        for(int i = 1; i <= 9; i++)    
            solve(n-1, k, i, i);
        return ans;
    }
};
```
