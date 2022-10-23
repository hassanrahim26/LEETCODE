## [Set Mismatch](https://leetcode.com/problems/set-mismatch/)

* **C++**

  * 1
  ```cpp
  class Solution {
  public:
      vector<int> findErrorNums(vector<int>& nums) {
          int n = nums.size();
          int s1 = (n*(n+1))/2, s2 = 0;
          for(auto x: nums){
              s2 += x;
          }
          sort(nums.begin(), nums.end());
          int x;
          for(int i = 1; i < nums.size(); i++){
              if(nums[i-1] == nums[i]){
                  x = nums[i-1];
                  break;
              }
          }
          int d = s1-s2+x;
          return {x, d};
      }
  };
  ```
  
  * 2
  ```cpp
  class Solution {
  public:
      vector<int> findErrorNums(vector<int>& nums) {
          unordered_map<int, int> mp;
          for(auto x: nums){
              mp[x]++;
          }
          int mis = 0, dup = 0;
          for(int i = 1; i <= nums.size(); i++){
              if(mp[i] == 2)
                  dup = i;
              if(mp[i] == 0)
                  mis = i;
          }
          return {dup, mis};
      }
  };
  ```
  
  * 3
  ```cpp
  class Solution {
  public:
      vector<int> findErrorNums(vector<int>& nums) {
          int s1 = accumulate(nums.begin(), nums.end(), 0);
          set<int> s;
        
          for(auto i: nums){
              s.insert(i);
          }
          int s2 = accumulate(s.begin(), s.end(), 0);
          int dup = s1-s2;
          int n = nums.size();
          int x = n*(n+1)/2 - s2;
          return {dup, x};
      }
  };
  ```
<hr>

* **PYTHON**

  * 1
  ```py
  class Solution:
      def findErrorNums(self, nums: List[int]) -> List[int]:
          n = len(nums)
          s1 = int((n*(n+1))/2)
          s2 = sum(nums)
          s3 = sum(set(nums))
        
          return [s2-s3, s1-s3]
  ```
  
  * 2
  ```py
  class Solution:
      def findErrorNums(self, nums: List[int]) -> List[int]:
          mp = Counter(nums)
          ans = [0, 0]
          for i in range(1, len(nums)+1):
              if mp[i] == 2:
                  ans[0] = i
              if mp[i] == 0:
                  ans[1] = i
          return ans
  ```
  
  * 3
  ```py
  class Solution:
      def findErrorNums(self, nums: List[int]) -> List[int]:
          s1 = sum(nums)
          s = set()
          for i in nums:
              s.add(i)
            
          s2 = sum(set(nums))
          dup = s1-s2
          n = len(nums)
          x = n*(n+1)//2 - s2
          return [dup, x]
  ```
