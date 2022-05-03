## [Maximum Number of Removable Characters](https://leetcode.com/problems/maximum-number-of-removable-characters/)

* **C++**
```cpp
class Solution {
public:
    bool isSubSequence(string str1, string str2){
        int j = 0, n1 = str1.size(), n2 = str2.size();
        
        for(int i = 0; i < n2 and j < n1; i++)
            if(str1[j] == str2[i])
                j++;
        
        return j == n1;
    }
    
    int maximumRemovals(string s, string p, vector<int>& removable) {
        string s1 = s;
        int low = 0, high = removable.size();
        
        while(low <= high){
            int mid = low + (high - low)/2;
            
            for(int i = 0; i < mid; i++)
                s1[removable[i]] = '*';
            
            if(isSubSequence(p, s1))
                low = mid + 1;
            else
            {
                for(int i = 0; i < mid; i++)
                    s1[removable[i]] = s[removable[i]];
                high = mid - 1;
            }
        }
        
        return high;
    }
};
```
