## [Valid Anagram](https://leetcode.com/problems/valid-anagram/)

* **C++**
  * Code 1
  ```cpp
  class Solution {
  public:
      bool isAnagram(string s, string t) {
          if(s.length() != t.length())        
              return false;
        
          int n = s.length();
          int counts[26] = {0};
          for(int i = 0; i < n; i++)
          {
              counts[s[i] - 'a']++;
              counts[t[i] - 'a']--;
          }
        
          for(int i = 0; i < 26; i++)
          {
              if(counts[i])
                  return false;
          }
        
          return true;
      }
  };
  ```
  * Code 2
  ```cpp
  class Solution {
  public:
      bool isAnagram(string s, string t) {
          sort(s.begin(), s.end());
          sort(t.begin(), t.end());
          return s == t;
      }
  };
  ```

* **Python**
  * Code 1
  ```py
  class Solution:
      def isAnagram(self, s: str, t: str) -> bool:
          s = s.lower()
          t = t.lower()
        
          if (len(s) == len(t)):
              if(sorted(s) == sorted(t)):
                  return True
          return False
        
  ```
  
  * Code 2
  ```py
  class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
  ```
