## [Kth Smallest Element in a Sorted Matrix](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/)

* **C++**
```cpp
class Solution {
public:
    int kthSmallest(vector<vector<int>>& matrix, int k) {
        int n = matrix.size();
        int low = matrix[0][0], high = matrix[n-1][n-1], mid;
        
        while(low < high){
            mid = low + (high-low)/2;
            int c = 0, j = n-1;
            
            for(int i = 0; i < n; i++){
                while(j >= 0 and matrix[i][j] > mid)
                    j--;
                c += j+1;
            }
            
            if(c < k)
                low = mid+1;
            else 
                high = mid;
        }
        return low;
    }
};
```

* **PYTHON**
```py
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        low, high = matrix[0][0], matrix[n-1][n-1]
        
        while(low < high):
            mid = low + (high - low)//2
            c, j, i = 0, n-1, 0
            
            while(i < n):
                while j >= 0 and matrix[i][j] > mid:
                    j -= 1
                c += j+1
                i += 1
            
            if(c < k):
                low = mid+1
            else:
                high = mid
        
        return low
```
