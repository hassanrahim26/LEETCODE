## [Find K Closest Elements](https://leetcode.com/problems/find-k-closest-elements/)

* **C++**
  * 1
    ```cpp
    // Two Pointers
    class Solution {
    public:
        vector<int> findClosestElements(vector<int>& arr, int k, int x) {
            int l = 0, r = arr.size()-1;
            while(r - l >= k){
                if(x - arr[l] <= arr[r] - x)
                    r--;
                else
                    l++;
            }
            return vector<int>(arr.begin()+l, arr.begin()+r+1);
        }
    };
    ```
    
  * 2
    ```cpp
    // Binary Search Using Two Pointers
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
  * 1
    ```py
    class Solution:
        def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
            l, r = 0, len(arr)-1
        
            while(r - l >= k):
                if(x - arr[l] <= arr[r] - x):
                    r -= 1
                else:
                    l += 1
            return arr[l: r+1]
    ```
    
  * 2
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
