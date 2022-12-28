## [Remove Stones to Minimize the Total](https://leetcode.com/problems/remove-stones-to-minimize-the-total/)

* **C++**

  * 1
  ```cpp
  class Solution {
  public:
      int minStoneSum(vector<int>& p, int k) {
          priority_queue<int> pq(p.begin(), p.end());
          int ans = accumulate(p.begin(), p.end(), 0);
          while(k--){
              int x = pq.top();
              pq.pop();
              pq.push(x - x/2);
              ans -= x/2;
          }
          return ans;
      }
  };
  ```
  
  * 2
  ```cpp
  class Solution {
  public:
      int minStoneSum(vector<int>& piles, int k) {
          priority_queue<int> pq;
          for(auto x: piles) pq.push(x);
        
          int x, ans = 0;
          while(k-- and !pq.empty()){
              x = pq.top(); pq.pop();
              x -= x/2;
              pq.push(x);
          }  
        
          while(!pq.empty()){
              ans += pq.top();
              pq.pop();
          }
        
          return ans;
      }
  };
  ```
  
<hr>

* **PYTHON**

  * 1
  ```py
  class Solution:
      def minStoneSum(self, piles: List[int], k: int) -> int:
          pq = [-x for x in piles]
          heapify(pq)
          for _ in range(k): heapreplace(pq, pq[0]//2)
          return -sum(pq)
  ```
