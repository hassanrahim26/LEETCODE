## [Group Anagrams](https://leetcode.com/problems/group-anagrams/)

* **C++**

  * 1
  ```cpp
    class Solution {
    public:
        vector<vector<string>> groupAnagrams(vector<string>& strs) {
            unordered_map<string, vector<string>> mp;
        
            for(string s : strs)
            {
                string t = s;
                sort(t.begin(), t.end());
                mp[t].push_back(s);
            }
        
            vector<vector<string>> anagrams;
            for(auto p : mp)
                anagrams.push_back(p.second);
            return anagrams;
        }
    };
  ```
  
  
  * 2
  ```cpp
    class Solution {
    public:
        vector<vector<string>> groupAnagrams(vector<string>& strs) {
            unordered_map<string, vector<string>> mp;
            for (string s : strs) {
                mp[solve(s)].push_back(s);
            }
            vector<vector<string>> ans;
            for (auto p : mp) { 
                ans.push_back(p.second);
            }
            return ans;
        }
        
    private:
        string solve(string s) {
            int counter[26] = {0};
            for (char c : s) {
                counter[c - 'a']++;
            }
            string t;
            for (int c = 0; c < 26; c++) {
                t += string(counter[c], c + 'a');
            }
            return t;
        }
    }; 
  ```

* **Python**
```py
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        anagrams = []
        for s in strs:
            t = ''.join(sorted(s))
            if t not in d:
                d[t] = [s]
            else:
                d[t].append(s)
        
        for x in d:
            anagrams.append(d[x])
        
        return anagrams
```
