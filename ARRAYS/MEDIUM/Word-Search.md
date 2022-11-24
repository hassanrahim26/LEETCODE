## [Word Search](https://leetcode.com/problems/word-search/)

* **C++**
```cpp
class Solution {
public:
    bool dfs(vector<vector<char>>& board, string word, int i, int j, int n){
        if(n == word.size()) return true;
        if(i < 0 || i >= board.size() || j < 0 || j >= board[i].size() || board[i][j] != word[n]) 
            return false;
        board[i][j] = '0';
        bool dir = dfs(board, word, i+1, j, n+1) ||
                   dfs(board, word, i, j+1, n+1) ||
                   dfs(board, word, i-1, j, n+1) ||
                   dfs(board, word, i, j-1, n+1);
        board[i][j] = word[n];
        return dir;
    }
    
    bool exist(vector<vector<char>>& board, string word) {
        if(word == "") return false;
        for(int i = 0; i < board.size(); i++)
            for(int j = 0; j < board[i].size(); j++)
                if(board[i][j] == word[0] and dfs(board, word, i, j, 0))
                    return true;
        return false;
    }
};
```
