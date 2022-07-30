## [Word Subsets](https://leetcode.com/problems/word-subsets/)

* **C++**
```cpp
class Solution {
public:
    vector<string> wordSubsets(vector<string>& A, vector<string>& B) {
        vector<int> v1(26), v2(26);
        int i;
        for(string b: B){
            v2 = counter(b);
            for(int i = 0; i < 26; i++)
                v1[i] = max(v1[i], v2[i]);
        }
        
        vector<string> ans;
        for(string a: A){
            v2 = counter(a);
            for(i = 0; i < 26; i++)
                if(v2[i] < v1[i])
                    break;
            if(i == 26)
                ans.push_back(a);
        }
        
        return ans;
    }
    
    vector<int> counter(string& w){
        vector<int> v(26);
        for(char c: w)
            v[c-'a']++;
        return v;
    }
};
```
