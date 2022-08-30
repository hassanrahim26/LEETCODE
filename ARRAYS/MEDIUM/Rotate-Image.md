## [Rotate Image](https://leetcode.com/problems/rotate-image/)

* **C++**
  * 1
    ```cpp
    class Solution {    
    public:
        void rotate(vector<vector<int>>& matrix) {
            for(int i = 0; i < matrix.size(); i++)
                for(int j = 0; j < i; j++)
                    swap(matrix[i][j], matrix[j][i]);
        
            for(int i = 0; i < matrix.size(); i++)
                reverse(matrix[i].begin(), matrix[i].end());
        }
    };
    ```
    
  * 2
    ```cpp
    class Solution {
    public:
        void rotate(vector<vector<int>>& matrix) {
            for(int i = 0; i < matrix.size(); ++i) 
                for(int j = i; j < matrix.size(); ++j) 
                    swap(matrix[i][j], matrix[j][i]);
            
            for(int i = 0; i < matrix.size(); i++){
                int left = 0, right = matrix.size()-1;
                while(left < right) {
                    swap(matrix[i][left], matrix[i][right]);
                    ++left;
                    --right;
                }
            }
        }
    };
    ```

* **Python**
  * 1
    ```py
    class Solution:
        def rotate(self, matrix: List[List[int]]) -> None:
            matrix.reverse()
            for i in range(len(matrix)):
                for j in range(i):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
    ```

  * 2
    ```py
    class Solution:
        def rotate(self, matrix: List[List[int]]) -> None:
            for i in range(len(matrix)):
                for j in range(i):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
            for i in range(len(matrix)):
                left, right = 0, len(matrix)-1
                while(left < right):
                    matrix[i][left], matrix[i][right] = matrix[i][right], matrix[i][left]
                    left += 1
                    right -= 1
    ```
