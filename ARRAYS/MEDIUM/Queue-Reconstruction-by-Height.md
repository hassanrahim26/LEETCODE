## [Queue Reconstruction by Height](https://leetcode.com/problems/queue-reconstruction-by-height/)

* **C++**
```cpp
class Solution {
public:
    static bool compare(vector<int>& a, vector<int>& b)
    {
        if(a[0] == b[0])    
            return a[1] < b[1];
        return a[0] > b[0];
    }
    
    vector<vector<int>> reconstructQueue(vector<vector<int>>& people) {
        sort(people.begin(), people.end(), compare);
        vector<vector<int>> ans;
        
        for(auto p: people)
            ans.insert(ans.begin() + p[1], p);
        
        return ans;
    }
};
```

* **Python**
```py
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key = lambda person: (-person[0], person[1]))
        ans = []
        for p in people:
            ans.insert(p[1], p)
        return ans
```
