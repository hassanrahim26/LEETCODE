## [Minimum Number of Refueling Stops](https://leetcode.com/problems/minimum-number-of-refueling-stops/)

* **C++**
```cpp
class Solution {
public:
    int minRefuelStops(int t, int pos, vector<vector<int>>& v) {
        int i = 0, c;
        priority_queue<int> pq;
        for(c = 0; pos < t; c++){
            while(i < v.size() and v[i][0] <= pos)
                pq.push(v[i++][1]);
            if(pq.empty())  return -1;
            pos += pq.top(); pq.pop();
        }
        return c;
    }
};
```

* **PYTHON**
```py
class Solution:
    def minRefuelStops(self, t: int, pos: int, v: List[List[int]]) -> int:
        pq = []
        c = i = 0
        while pos < t:
            while i < len(v) and v[i][0] <= pos:
                heapq.heappush(pq, -v[i][1])
                i += 1
            if not pq:  return -1
            pos += -heapq.heappop(pq)
            c += 1
        return c
```
