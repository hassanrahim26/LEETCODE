## [Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/)

* **C++**
  * 1
    ```cpp
    class Solution {
    public:
        int minCostClimbingStairs(vector<int>& cost) {
            int dp = 0, dp1 = 0, dp2 = 0;
            for(int i = 2; i <= cost.size(); i++){
                int one = dp1 + cost[i-1];
                int two = dp2 + cost[i-2];
                dp = min(one, two);
                dp2 = dp1;
                dp1 = dp;
            }
        
            return dp1;
        }
    };
    ```
    
  * 2
    ```cpp
    class Solution {
    public:
        int minCostClimbingStairs(vector<int>& cost) {
            int n = cost.size();
            for(int i = 2; i < n; i++){
                cost[i] += min(cost[i-1], cost[i-2]);
            }
            return min(cost[n-1], cost[n-2]);
        }
    };
    ```
    
* **Python**
  * 1
    ```py
    class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp, dp1, dp2 = 0, 0, 0
        for i in range(2, len(cost)+1):
            one = dp1 + cost[i-1]
            two = dp2 + cost[i-2]
            dp = min(one, two)
            dp2 = dp1
            dp1 = dp
            
        return dp1
    ```
    
  * 2
    ```py
    class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(2, len(cost)):
            cost[i] += min(cost[i-1], cost[i-2])
        return min(cost[-1], cost[-2])
        
    ```
