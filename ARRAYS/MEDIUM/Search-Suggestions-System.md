## [Search Suggestions System](https://leetcode.com/problems/search-suggestions-system/)

* **C++**
```cpp
class Solution {
public:
    vector<vector<string>> suggestedProducts(vector<string>& products, string searchWord) {
        sort(products.begin(), products.end());
        vector<vector<string>> ans;
        int startIdx = 0, endIdx = products.size() - 1;
        
        for(int i = 0; i < searchWord.length(); i++){
            while(startIdx <= endIdx && (i >= products[startIdx].size() || products[startIdx][i] < searchWord[i]))
                startIdx++;
            
            while(startIdx <= endIdx && (i >= products[endIdx].size() || products[endIdx][i] > searchWord[i]))
                endIdx--;
            
            ans.push_back({});
            
            for(int j = startIdx; j < min(startIdx + 3, endIdx + 1); j++)
                ans.back().push_back(products[j]);
        }
        
        return ans;
    }
};
```
