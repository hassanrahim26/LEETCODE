## [Container With Most Water](https://leetcode.com/problems/container-with-most-water/)

* **C++**
  - 1
  ```cpp
  class Solution {
  public:
    int maxArea(vector<int>& height) {
        int left = 0, right = height.size() - 1;
        int x = 0;
        
        while(left < right)
        {
            int w = right - left;
            int h = min(height[left], height[right]);
            int area = h * w;
            x = max(x, area);
            
            if(height[left] < height[right])
                left++;
            else if(height[left] > height[right])
                right--;
            else
            {
                left++;
                right--;
            }
        }
        
        return x;
     }
  };
  ```
  
  - 2
  ```cpp
  class Solution {
  public:
    int maxArea(vector<int>& height) {
        int area = 0;
        int l = 0, r = height.size() - 1;
        
        while(l < r)
        {
            area = max(area, min(height[l], height[r]) * (r-l));
            
            if(height[l] < height[r])
                l++;
            else
                r--;
        }
        
        return area;
     }
  };
  ```
