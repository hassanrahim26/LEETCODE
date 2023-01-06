## [Minimum Number of Arrows to Burst Balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/)

* **C++**

  * 1
  ```cpp
  class Solution {
  public:
      static bool comp(vector<int>& a, vector<int>& b){
          return a[1] < b[1];
      }
      int findMinArrowShots(vector<vector<int>>& points) {
          if(points.size() == 0)    
              return 0;
          sort(points.begin(), points.end(), comp);
          int ans = 1, l = points[0][1];
        
          for(int i = 1; i < points.size(); i++){
              if(points[i][0] > l){
                  ans++;
                  l = points[i][1];
              }
          }
          return ans;
      }
  };
  ```
  
  * 2
  ```cpp
  class Solution {
  public:
      int findMinArrowShots(vector<vector<int>>& points) {
          if(points.size() == 0)    
              return 0;
          sort(points.begin(), points.end(), [](const vector<int>& x, const vector<int>& y){
              return x[1] < y[1];
          });
          int ans = 1, l = points[0][1];
        
          for(int i = 1; i < points.size(); i++){
              if(points[i][0] > l){
                  ans++;
                  l = points[i][1];
              }
          }
          return ans;
      } 
  };
  ```
  
  * 3
  ```cpp
  class Solution {
  public:
      int findMinArrowShots(vector<vector<int>>& points) {
          sort(points.begin(), points.end());
          int l = points[0][1], ans = 1;
        
          for(auto x: points){
              if(x[0] > l){
                  ans++;
                  l = x[1];
              }
              l = min(x[1], l);
          }
          return ans;
      }
  };
  ```
  
<hr>

* **PYTHON**

  * 1
  ```py
  class Solution:
      def findMinArrowShots(self, points: List[List[int]]) -> int:
          if len(points) == 0:
              return 0
          points.sort(key=lambda x: x[1])
          ans, l = 1, points[0][1]
        
          for i in range(1, len(points)):
              if points[i][0] > l:
                  ans += 1
                  l = points[i][1]
          return ans
  ```
  
  * 2
  ```py
  class Solution:
      def findMinArrowShots(self, points: List[List[int]]) -> int:
          points.sort()
          l, ans = points[0][1], 1
        
          for x in points:
              if x[0] > l:
                  ans += 1
                  l = x[1]
              l = min(x[1], l)
          return ans
  ```
