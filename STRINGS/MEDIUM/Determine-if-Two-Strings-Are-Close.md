## [Determine if Two Strings Are Close](https://leetcode.com/problems/determine-if-two-strings-are-close/)

* **C++**

  * 1
  ```cpp
  class Solution {
  public:
      bool closeStrings(string word1, string word2) {
          vector<int> v1(26, 0), v2(26, 0);
          for(auto c: word1) v1[c - 'a']++;
          for(auto c: word2) v2[c - 'a']++;
          for(int i = 0; i < 26; i++)
              if((v1[i] and !v2[i]) || (!v1[i] and v2[i]))
                  return false;
          sort(v1.begin(), v1.end());
          sort(v2.begin(), v2.end());
          return v1 == v2;
      }
  };
  ```
  
  * 2
  ```cpp
  class Solution {
  public:
      bool closeStrings(string word1, string word2) {
          vector<int> w1(26, 0), w2(26, 0);
          set<char> s1, s2;
          for(char c: word1){
              w1[c - 'a']++;
              s1.insert(c);
          }
          for(char c: word2){
              w2[c - 'a']++;
              s2.insert(c);
          }
          sort(w1.begin(), w1.end());
          sort(w2.begin(), w2.end());
          return w1 == w2 and s1 == s2;
      }
  };
  ```
  
<hr>

* **PYTHON**

  * 1
  ```py
  class Solution:
      def closeStrings(self, w1: str, w2: str) -> bool:
          return set(w1) == set(w2) and Counter(Counter(w1).values()) == Counter(Counter(w2).values())
  ```
