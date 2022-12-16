class Chessboard:
    def __init__(self):
        self.board = [[0] * 8] * 8
        self.move_dict = {'Rook': [[-1, 0], [1, 0], [0, -1], [0, 1]], 'Bishop': [[-1, 1], [1, 1], [-1,-1], [1, -1]], 'Knight': [[2, 1], [1,2], [1, -2], [-1, -2]]}
        self.single_movers = set(['Knight', 'Pawn', 'King'])

    def get_positions(self, piece, inital_pos):
        start_x, start_y = inital_pos
        possible_positions = []
        for move in self.move_dict[piece]:
            c_x, c_y = start_x, start_y
            moves = 0
            while 0 <= c_x + move[0] < len(self.board) and 0 <= c_y + move[1] < len(self.board[0]):
                if moves > 0 and piece in self.single_movers:
                    break
                c_x, c_y = c_x + move[0], c_y + move[1]
                possible_positions.append((c_x, c_y))
                moves += 1
        return possible_positions

    
chessboard = Chessboard()
print(chessboard.get_positions('Knight', (1, 1)))
