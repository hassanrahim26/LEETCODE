## [Find Right Interval](https://leetcode.com/problems/find-right-interval/)

* **C++**
```cpp
class Solution {
public:
    vector<int> findRightInterval(vector<vector<int>>& intervals) {
        vector<int> ans;
        vector<pair<int, int>> v;
        
        for(int i = 0; i < intervals.size(); i++)
            v.push_back({intervals[i][0], i});
        
        sort(v.begin(), v.end());
        
        for(int i = 0; i < intervals.size(); i++){
            int x = intervals[i][1], val = -1, low = 0, high = v.size() - 1;
            
            while(low <= high){
                int mid = low + (high - low)/2;
                
                if(v[mid].first >= x)
                {
                    val = v[mid].second;
                    high = mid - 1;
                }
                else if(v[mid].first < x)
                {
                    low = mid + 1;
                }
            }
            ans.push_back(val);
        }
        
        return ans;
    }
};
```
