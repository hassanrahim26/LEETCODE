## [Minimum Rounds to Complete All Tasks](https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/)

* **C++**

  * 1
  ```cpp
  class Solution {
  public:
      int minimumRounds(vector<int>& t) {
          unordered_map<int, int> mp;
          for(auto x: t)
              mp[x]++;
        
          int ans = 0;
          for(auto it: mp){
              if(it.second == 1)
                  return -1;
              else if(it.second % 3 == 0)
                  ans += it.second/3;
              else
                  ans += it.second/3 + 1;
          }
          return ans;
      }
  };
  ```
  
  * 2
  ```cpp
  class Solution {
  public:
      int minimumRounds(vector<int>& t) {
          unordered_map<int, int> mp;
          for(auto x: t)
              mp[x]++;
        
          int ans = 0;
          for(auto it: mp){
              if(it.second == 1)
                  return -1;
              ans += (it.second + 2)/3;
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
      def minimumRounds(self, t: List[int]) -> int:
          mp = Counter(t)
          ans = 0
        
          for it in mp.values():
              if it == 1:
                  return -1
              elif int(it) % 3 == 0:
                  ans += it//3
              else:
                  ans += it//3 + 1
                
          return ans
  ```
  
  * 2
  ```py
  class Solution:
      def minimumRounds(self, t: List[int]) -> int:
          mp = Counter(t)
          ans = 0
        
          for it in mp.values():
              if it == 1:
                  return -1
              ans += (it + 2)//3
                
          return ans
  ```
