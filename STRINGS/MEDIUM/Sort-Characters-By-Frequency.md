## [Sort Characters By Frequency](https://leetcode.com/problems/sort-characters-by-frequency/)

* **C++**

  * 1
  ```cpp
  class Solution {
  public:
      string frequencySort(string s) {
          int mp[256] = {0};
          for(char c: s)
              mp[c]++;
          sort(s.begin(), s.end(), [&](char a, char b) {
              return mp[a] > mp[b] or (mp[a] == mp[b] and a < b) ;
          });
          return s;
      }
  };
  ```
  
  * 2
  ```cpp
  class Solution {
  public:
      string frequencySort(string s) {
          unordered_map<char, int> mp;
          vector<string> v(s.size()+1, "");
          string ans;
        
          for(char c: s)
              mp[c]++;
        
          for(auto& it: mp){
              int n = it.second;
              char c = it.first;
              v[n].append(n, c);
          }
        
          for(int i = s.size(); i > 0; i--){
              if(!v[i].empty())    
                  ans.append(v[i]);
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
      def frequencySort(self, s: str) -> str:
          return "".join(char * times for char, times in collections.Counter(s).most_common())
  ```
