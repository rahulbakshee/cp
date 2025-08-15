# time:O(1), space:O(n)
class TicTacToe:
    def __init__(self, n:int):
        self.rows = [0] * n
        self.cols = [0] * n
        self.diag = 0
        self.adiag = 0
        self.n = n

    def move(self, row:int, col:int, player:int)->int:
        move = 1
        if player == 2:
            move  = -1

        self.rows[row] += move
        self.cols[col] += move
        if row == col:
            self.diag += move
        if self.n - row - 1 == col:
            self.adiag += move


        # check for winning condition
        if self.n in [abs(self.rows[row]), abs(self.cols[col]), abs(self.diag), abs(self.adiag)]:
            return player

        return 0
