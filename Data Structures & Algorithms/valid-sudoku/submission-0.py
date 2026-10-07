class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            bucket = [0] * 10
            for j in range(9):
                if board[i][j] == ".":
                    continue
                else:
                    bucket[int(board[i][j])] += 1
                    if bucket[int(board[i][j])] > 1:
                        return False
        
        bucket = [0] * 10
        for i in range(9):
            bucket = [0] * 10
            for j in range(9):
                if board[j][i] == ".":
                    continue
                else:
                    bucket[int(board[j][i])] += 1
                    if bucket[int(board[j][i])] > 1:
                        return False
        
        bucket = [0] * 10
        for i in range(0,3):
            for j in range(0,3):
                if board[i][j] == ".":
                    continue
                else:
                    bucket[int(board[i][j])] += 1
                    if bucket[int(board[i][j])] > 1:
                        return False
        
        bucket = [0] * 10
        for i in range(3,6):
            for j in range(0,3):
                if board[i][j] == ".":
                    continue
                else:
                    bucket[int(board[i][j])] += 1
                    if bucket[int(board[i][j])] > 1:
                        return False

        bucket = [0] * 10
        for i in range(6,9):
            for j in range(0,3):
                if board[i][j] == ".":
                    continue
                else:
                    bucket[int(board[i][j])] += 1
                    if bucket[int(board[i][j])] > 1:
                        return False

        bucket = [0] * 10
        for i in range(0,3):
            for j in range(3,6):
                if board[i][j] == ".":
                    continue
                else:
                    bucket[int(board[i][j])] += 1
                    if bucket[int(board[i][j])] > 1:
                        return False

        bucket = [0] * 10
        for i in range(3,6):
            for j in range(3,6):
                if board[i][j] == ".":
                    continue
                else:
                    bucket[int(board[i][j])] += 1
                    if bucket[int(board[i][j])] > 1:
                        return False

        bucket = [0] * 10
        for i in range(6,9):
            for j in range(3,6):
                if board[i][j] == ".":
                    continue
                else:
                    bucket[int(board[i][j])] += 1
                    if bucket[int(board[i][j])] > 1:
                        return False
        
        bucket = [0] * 10
        for i in range(0,3):
            for j in range(6,9):
                if board[i][j] == ".":
                    continue
                else:
                    bucket[int(board[i][j])] += 1
                    if bucket[int(board[i][j])] > 1:
                        return False

        bucket = [0] * 10
        for i in range(3,6):
            for j in range(6,9):
                if board[i][j] == ".":
                    continue
                else:
                    bucket[int(board[i][j])] += 1
                    if bucket[int(board[i][j])] > 1:
                        return False

        bucket = [0] * 10
        for i in range(6,9):
            for j in range(6,9):
                if board[i][j] == ".":
                    continue
                else:
                    bucket[int(board[i][j])] += 1
                    if bucket[int(board[i][j])] > 1:
                        return False
        
        return True
