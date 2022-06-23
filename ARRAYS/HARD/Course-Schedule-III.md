## [Course Schedule III](https://leetcode.com/problems/course-schedule-iii/)

* **C++**
```cpp
class Solution {
public:
    int scheduleCourse(vector<vector<int>>& courses) {
        if(courses.size() <= 0)    
            return 0;
        sort(courses.begin(), courses.end(), [](const vector<int>& a , const vector<int>& b){
            return a[1] < b[1];
        });
        
        priority_queue<int> pq;
        int sum = 0;
        
        for(auto i: courses){
            sum += i[0];
            pq.push(i[0]);
            
            if(sum > i[1]){
                sum -= pq.top();
                pq.pop();
            }
        }
        
        return pq.size();
    }
};
```
