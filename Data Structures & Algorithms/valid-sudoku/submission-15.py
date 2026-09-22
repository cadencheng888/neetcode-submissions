from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)
        for i in range(9):
            for j in range(9):
                char = board[i][j]
                if ord('0') <= ord(char) <= ord('9'):
                    if char in rows[i] or char in cols[j] or char in squares[(i // 3, j // 3)]:
                        return False
                    rows[i].add(char)
                    cols[j].add(char)
                    squares[(i // 3, j // 3)].add(char)
                
        return True
        