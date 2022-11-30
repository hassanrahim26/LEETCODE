## [Unique Number of Occurrences](https://leetcode.com/problems/unique-number-of-occurrences/)

* **C++**

  * 1
  ```cpp
  class Solution {
  public:
      bool uniqueOccurrences(vector<int>& arr) {
          unordered_map<int, int> mp;
          for(auto x: arr)
              mp[x]++;
          vector<int> v;
          for(auto it: mp)
              v.push_back(it.second);
          set<int> s(v.begin(), v.end());
          if(v.size() == s.size())
              return true;
          return false;
      }
  };
  ```
  
  * 2
  ```cpp
  class Solution {
  public:
      bool uniqueOccurrences(vector<int>& arr) {
          unordered_map<int, int> mp;
          unordered_set<int> s;
          for(auto x: arr)
              mp[x]++;
          for(auto it: mp)
              s.insert(it.second);
          return mp.size() == s.size();
      }
  };
  ```

<hr>

* **PYTHON**

  * 1
  ```py
  class Solution:
      def uniqueOccurrences(self, arr: List[int]) -> bool:
          return len(set(arr)) == len(set(Counter(arr).values()))
  ```
