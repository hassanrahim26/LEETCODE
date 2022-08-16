## [Node With Highest Edge Score](https://leetcode.com/problems/node-with-highest-edge-score/)

* **C++**
  * 1
    ```cpp
    class Solution {
    public:
        int edgeScore(vector<int>& edges) {
            int n = edges.size();
            vector<long long> v(n, 0);
            for(int i = 0; i < n; i++)
                v[edges[i]] += i;
            int x = 0;
            for(int i = 0; i < n; i++)
                if(v[i] > v[x])
                    x = i;
            return x;
        }
    };
    ```
  * 2 
    ```cpp
    class Solution {
    public:
        int edgeScore(vector<int>& edges) {
            vector<long long> v(edges.size());
            for (int i = 0; i < edges.size(); ++i)
                v[edges[i]] += i;
            return max_element(begin(v), end(v)) - begin(v);
        }
    };
    ```
    
* **PYTHON** 
  ```py
  class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        v = [0] * len(edges)
        for i in range(0, len(edges)):
            v[edges[i]] += i
        return v.index(max(v))  
  ```
