from player import Player
import numpy as np
class MinimaxPlayer(Player):
    def __init__(self, player_number, board, depth=3):
        super().__init__(player_number, board)
        self.depth = depth
        self.limit=0

    def get_next_move(self):
      #  self.minimax(0,self.player_number)
      #  self.board.start_imagination()
        # default is greedy playing
        max_score = -float('inf')
        best_move = None
        range_n = 0, self.board.get_n()
        step = 1
        if self.player_number == 0:
            range_n = self.board.get_n() - 1, -1
            step = -1
        moves=self.get_moves(range_n[0],range_n[1],step,self.player_number,self.board.get_board_grid(),self.board)
        for move in moves:
                    self.board.start_imagination()
                    if self.board.is_move_valid(self.board.get_imaginary_board(), move, self.player_number):
                        scores, game_over = self.board.place_piece_imaginary(move, self.player_number)
                        score=self.Minimax(self.depth,not self.player_number)
                        if score > max_score:
                            max_score=score
                            best_move = move
        return best_move
    def Minimax(self,depth,player_number):
        if(depth==0 or self.board.is_game_over(self.board.get_imaginary_board())):
             return (self.board.get_scores(self.board.get_imaginary_board())[self.player_number] -
                     self.board.get_scores(self.board.get_imaginary_board())[self.opponent_number])
        range_n = 0, self.board.get_n()
        step = 1
        if player_number == 0:
            range_n = self.board.get_n() - 1, -1
            step = -1
            max_score=-float('inf')
        if player_number:
            max_score=float('inf')
        if player_number==self.player_number:
            moves=self.get_moves(range_n[0],range_n[1],step,player_number,self.board.get_imaginary_board(),self.board)
            for move in moves:
                    save_board=np.copy(self.board.get_imaginary_board())
                    if self.board.is_move_valid(self.board.get_imaginary_board(), move,player_number):
                        self.board.place_piece_imaginary(move,player_number)
                    score=self.Minimax(depth-1,not player_number)
                    score=max(score,max_score)
                    self.board.imaginary_board_grid=np.copy(save_board)
            return max_score
        else:
            moves=self.get_moves(range_n[0],range_n[1],step,player_number,self.board.get_imaginary_board(),self.board)
            for move in moves:
                    save_board=np.copy(self.board.get_imaginary_board())
                    if self.board.is_move_valid(self.board.get_imaginary_board(), move,player_number):
                        self.board.place_piece_imaginary(move,player_number)
                    score= self.Minimax(depth-1,not player_number)
                    score=min(score,max_score)
                    self.board.imaginary_board_grid=np.copy(save_board)
            return max_score
    
        # TODO: Implement this function based on the minimax algorithm
        pass

    def get_moves(self,range_1,range_2,step,player_number,test_board,board):
        moves=[]
        for i in range(range_1,range_2,step):
            for j in range(range_1,range_2,step):
                if test_board[i][j] == player_number:
                 for direction in board.get_possible_directions(player_number):
                    move = (i, j), (i + direction[0], j + direction[1])
                    moves.append(move)
        return moves