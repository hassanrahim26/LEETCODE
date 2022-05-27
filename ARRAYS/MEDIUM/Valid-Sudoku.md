## [Valid Sudoku](https://leetcode.com/problems/valid-sudoku/)

* **C++**
```cpp
class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        vector<set<int>> rows(9), cols(9), squares(9);
        for(int i = 0; i < 9; i++){
            for(int j = 0; j < 9; j++){
                if(board[i][j] == '.')
                    continue;
                
                int curr = board[i][j];
                
                if(rows[i].count(curr) || cols[j].count(curr) || 
                   squares[(i/3)*3 + j/3].count(curr))
                    return false;
                
                rows[i].insert(curr);
                cols[j].insert(curr);
                squares[(i/3*3) + j/3].insert(curr);
            }
        }
        
        return true;
    }
};
```

* **Python**
```py
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        squares = [set() for i in range(9)]
        
        for i in range(9):
            for j in range(9):
                curr = board[i][j]
                
                if curr != '.':
                    k = (i//3) * 3 + j//3
                    
                    if curr not in rows[i]:
                        rows[i].add(curr)
                    else: 
                        return False
                    
                    if curr not in cols[j]:
                        cols[j].add(curr)
                    else:
                        return False
                    
                    if curr not in squares[k]:
                        squares[k].add(curr)
                    else:
                        return False
        return True
```
