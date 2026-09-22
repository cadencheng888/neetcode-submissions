class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)
        for i in range(9):
            for j in range(9):
                tile = board[i][j]
                if ord('0') <= ord(tile) <= ord('9'):
                    if tile in rows[i] or tile in cols[j]:
                        return False
                    if tile in squares[(i // 3, j // 3)]:
                        return False
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    squares[(i // 3, j // 3)].add(board[i][j])
                
        return True
        