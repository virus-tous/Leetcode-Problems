class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]      # create 9 rows
        cols = [set() for _ in range(9)]      # create 9 cols
        boxes = [set() for _ in range(9)]     # create 9 subboxes
        
        # traverse the board
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                # check if the position is filled with number
                if val == '.':
                    continue
                
                # if val already in row r, invalid
                if val in rows[r]:
                    return False
                rows[r].add(val)
                
                # if val already in col c, invalid
                if val in cols[c]:
                    return False
                cols[c].add(val)
                
                # check subboxes
                idx = (r//3)*3 + c//3
                if val in boxes[idx]:
                    return False
                boxes[idx].add(val)
                
        return True
        