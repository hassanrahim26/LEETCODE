## [Find Smallest Letter Greater Than Target](https://leetcode.com/problems/find-smallest-letter-greater-than-target/)

* **C++**
```cpp
class Solution {
public:
    char nextGreatestLetter(vector<char>& letters, char target) {
        int start = 0, end = letters.size() - 1;
        
        if(letters.back() <= target or letters[0] > target)
                return letters[0];
        
        while(start <= end)
        {
            int mid = start + (end - start)/2;
            
            if(letters[mid] > target)
                end = mid - 1;
            else
                start = mid + 1;
        }
        
        return letters[start];
    }
};
```

* **Python**
```py
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        start, end = 0, len(letters) - 1
        
        if letters[-1] <= target or letters[0] > target:
            return letters[0]
        
        while start <= end:
            mid = start + (end - start)//2
            
            if letters[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
            
        return letters[start]
        
```
