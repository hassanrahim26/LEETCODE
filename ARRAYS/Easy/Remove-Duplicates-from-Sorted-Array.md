## [Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)

* **C++**

  * 1
  ```cpp
  class Solution {
  public:
      int removeDuplicates(vector<int>& nums) {
          if(nums.size() == 0) return 0;
          int start = 0;
          for(int end = 1; end < nums.size(); end++){
              if(nums[start] != nums[end]){
                  start++;
                  nums[start] = nums[end];
              }
          }
          return start+1;
      }
  };
  ```
  
  * 2
  ```cpp
  class Solution {
  public:
      int removeDuplicates(vector<int>& nums) {
          int k = 1;
          for(int i = 1; i < nums.size(); i++)
              if(nums[i] != nums[i-1]) nums[k++] = nums[i];
          return k;
      }
  };
  ```
<hr>  

* **PYTHON**

 * 1
 ```py
 class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for j in range(1,len(nums)):
            if nums[j] != nums[j-1]:
                nums[i] = nums[j-1]
                i += 1
        nums[i] = nums[-1]
        return i+1
 ```
