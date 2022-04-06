## [Check If It Is a Straight Line](https://leetcode.com/problems/check-if-it-is-a-straight-line/)

* **C++**
```cpp
class Solution {
public:
    bool checkStraightLine(vector<vector<int>>& coordinates) {
        if(coordinates.size() <= 2)    
            return true;
        
        int x1 = coordinates[0][0];
        int y1 = coordinates[0][1];
        int x2 = coordinates[1][0];
        int y2 = coordinates[1][1];
        
        for(int i = 2; i < coordinates.size(); i++){
            int x = coordinates[i][0];
            int y = coordinates[i][1];
            if((y2 - y1) * (x1 - x) != (y1 - y) * (x2 - x1))
                return false;
        }
        
        return true;
    }
};
```

* **Python**
```py
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        (x1, y1), (x2, y2) = coordinates[:2]
        
        for i in range(2, len(coordinates)):
            (x, y) = coordinates[i]
            
            if((y2 - y1) * (x1 - x) != (y1 - y) * (x2 - x1)):
                return False
            
        return True
```
