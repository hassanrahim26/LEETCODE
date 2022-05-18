## [Sum of Mutated Array Closest to Target](https://leetcode.com/problems/sum-of-mutated-array-closest-to-target/)

* **C++**
```cpp
class Solution {
public:
    int diff(int mid, vector<int> &arr, int target){
        int sum = 0;
        for(int i = 0; i < arr.size(); i++)
            sum += min(mid, arr[i]);
        
        return abs(target - sum);
    }
    
    int findBestValue(vector<int>& arr, int target) {
        int n = arr.size();
        int low = 0, high = target;
        
        while(low < high){
            int mid = low + (high - low)/2;
            
            if(diff(mid, arr, target) <= diff(mid+1, arr, target))
                high = mid;
            else
                low = mid + 1;
        }
        
        return low;
    }
};
```
