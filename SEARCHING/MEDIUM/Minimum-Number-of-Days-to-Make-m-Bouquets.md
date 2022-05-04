## [Minimum Number of Days to Make m Bouquets](https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/)

* **C++**
```cpp
class Solution {
public:
    int minDays(vector<int>& bloomDay, int m, int k) {
        int low = 1, high = 1e9;
        
        if(m * k > bloomDay.size())
            return -1;
        
        while(low < high){
            int mid = low + (high - low)/2, f = 0, b = 0;
            
            for(int j = 0; j < bloomDay.size(); j++){
                if(bloomDay[j] > mid){
                    f = 0;    
                }
                else if(++f >= k){
                    b++;
                    f = 0;
                }
            }
            
            if(b < m)
                low = mid + 1;
            else
                high = mid;
        }
        
        return low;
    }
};
```
