## [Earliest Possible Day of Full Bloom](https://leetcode.com/problems/earliest-possible-day-of-full-bloom/)

* **C++**

  * 1
  ```cpp
  class Solution {
  public:
      int earliestFullBloom(vector<int>& plantTime, vector<int>& growTime) {
          int n = plantTime.size();
          vector<pair<int, int>> v(n);
            
          for(int i = 0; i < n; i++){
              v[i] = {growTime[i], plantTime[i]};
          }
          sort(v.begin(), v.end(), greater<pair<int, int>>());
            
          int day = 0, ans = 0;
          for(int i = 0; i < n; i++){
              day += v[i].second;
              ans = max(ans, day + v[i].first);
          }
          return ans;
      }
  };
  ```

  * 2
  ```cpp
  class Solution {
  public:
      int earliestFullBloom(vector<int>& plantTime, vector<int>& growTime) {
          vector<pair<int, int>> pairs;
          for(auto i = 0; i < plantTime.size(); i++)
              pairs.emplace_back(growTime[i], plantTime[i]);
          sort(pairs.rbegin(), pairs.rend());
          int c = 0, t = 0;
          for(auto [g, p]: pairs){
              c += p;
              t = max(t, c+g);
         }
         return t;
      }
  };
  ```
