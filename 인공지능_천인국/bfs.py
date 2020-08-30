class State:
    def __init__(self, board, goal, moves=0):
        self.board=board
        self.moves=moves
        self.goal=goal
    def get_new_board(self, i1 ,i2, moves):
        new_board=self.board[:]
        new_board[i1],new_board[i2] = new_board[i2], new_board[i1]
        return State(new_board, self.goal, moves)
    def expand(self, moves):
        result = []
        i = self.board.index(0)		# 숫자 0(빈칸)의 위치를 찾는다. 
        if not i in [0, 1, 2] :		# UP 연산자 
            result.append(self.get_new_board(i, i-3, moves))
        if not i in [0, 3, 6] :		# LEFT 연산자 
            result.append(self.get_new_board(i, i-1, moves))
        if not i in [2, 5, 8]:		# DOWN 연산자 
            result.append(self.get_new_board(i, i+1, moves))
        if not i in [6, 7, 8]:		# RIGHT 연산자 
            result.append(self.get_new_board(i, i+3, moves))
        return result
# 객체를 출력할 때 사용한다. 
    def __str__(self):
        return str(self.board[:3]) +"\n"+\
        str(self.board[3:6]) +"\n"+\
        str(self.board[6:]) +"\n"+\
        "------------------"
