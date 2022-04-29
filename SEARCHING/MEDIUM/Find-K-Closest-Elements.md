## [Find K Closest Elements](https://leetcode.com/problems/find-k-closest-elements/)

* **C++**
```cpp
class Solution {
public:
    vector<int> findClosestElements(vector<int>& arr, int k, int x) {
        int low = 0, high = arr.size() - k;
        
        while (low < high) {
            int mid = low + (high - low) / 2;
            
            if (x - arr[mid] > arr[mid + k] - x)
                low = mid + 1;
            else
                high = mid;
        }
        return vector<int>(arr.begin() + low, arr.begin() + low + k);
    }
};
```

* **Python**
```py
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        low, high = 0, len(arr) - k
        
        while low < high:
            mid = low + (high - low)//2
            
            if x - arr[mid] > arr[mid + k] - x:
                low = mid + 1
            else:
                high = mid
        
        return arr[low: low + k]
```
