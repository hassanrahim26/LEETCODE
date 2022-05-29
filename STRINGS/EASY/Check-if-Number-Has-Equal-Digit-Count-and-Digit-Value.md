## [Check if Number Has Equal Digit Count and Digit Value](https://leetcode.com/problems/check-if-number-has-equal-digit-count-and-digit-value/)

* **C++**
```cpp
class Solution {
public:
    bool digitCount(string num) {
        unordered_map<int, int> mp;
        for(auto i: num){
            mp[i - '0']++;
        }
        
        for(int i = 0; i < num.size(); i++){
            if(mp[i] != int(num[i] - '0'))    
                return false;
        }
        return true;
    }
};
```

* **Python**
```py
class Solution:
    def digitCount(self, num: str) -> bool:
        c = Counter(num)
        for i in range(len(num)):
            if c[str(i)] != int(num[i]):
                return False
        return True
```
