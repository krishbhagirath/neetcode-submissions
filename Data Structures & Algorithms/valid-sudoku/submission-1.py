class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set(), set(), set(), set(), set(), set(), set(), set(), set()]
        cols = [set(), set(), set(), set(), set(), set(), set(), set(), set()]
        squares = [set(), set(), set(), set(), set(), set(), set(), set(), set()]

        for i in range(len(board)):
            for j in range(len(board[i])):
                value = board[i][j]
                if(value == '.'):
                    continue

                if(value in rows[i]):
                    return False
                else:
                    rows[i].add(value)

                if(value in cols[j]):
                    return False
                else:
                    cols[j].add(value)

                square = (i // 3) * 3 + (j // 3)
                if(value in squares[square]):
                    return False
                else:
                    squares[square].add(value)


        return True