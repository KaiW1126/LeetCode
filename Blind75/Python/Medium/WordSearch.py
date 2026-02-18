class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if self.dfs(board, i, j, word, 0):
                        return True
        return False

    def dfs(self, board, i, j, word, index):
        # 全文字一致したら成功
        if index == len(word):
            return True
        
        # 範囲外 or 文字不一致 → 失敗
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return False
        if board[i][j] != word[index]:
            return False
        
        # 訪問済みマーク（バックトラック用）
        temp = board[i][j]
        board[i][j] = "#"
    
        # 上下左右に再帰
        found = (self.dfs(board, i+1, j, word, index+1) or
                self.dfs(board, i-1, j, word, index+1) or
                self.dfs(board, i, j+1, word, index+1) or
                self.dfs(board, i, j-1, word, index+1))
    
        # バックトラック: 元に戻す
        board[i][j] = temp
    
        return found