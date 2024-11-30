from player import Player
import numpy as np
class AlphaBetaPlayer(Player):
    def __init__(self, player_number, board, depth=3):
        super().__init__(player_number, board)
        self.depth = depth
        self.limit=0

    def get_next_move(self):
      #  self.minimax(0,self.player_number)
      #  self.board.start_imagination()
        # default is greedy playing
        alpha=-float('inf')
        beta=float('inf')
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
                        score=self.alphabeta_Minimax(self.depth,not self.player_number,alpha,beta)
                        if score > max_score:
                            max_score=score
                            best_move = move
        return best_move
    def alphabeta_Minimax(self,depth,player_number,alpha,beta):
        if(depth==0 or self.board.is_game_over(self.board.get_imaginary_board())):
             return (self.board.get_scores(self.board.get_imaginary_board())[self.player_number] -
                     self.board.get_scores(self.board.get_imaginary_board())[self.opponent_number])
        range_n = 0, self.board.get_n()
        step = 1
        if player_number == 0:
            range_n = self.board.get_n() - 1, -1
            step = -1
            maxEva=-float('inf')
        if player_number:
            maxEva=float('inf')
        if player_number==self.player_number:
            moves=self.get_moves(range_n[0],range_n[1],step,player_number,self.board.get_imaginary_board(),self.board)
            for move in moves:
                    save_board=np.copy(self.board.get_imaginary_board())
                    if self.board.is_move_valid(self.board.get_imaginary_board(), move,player_number):
                        self.board.place_piece_imaginary(move,player_number)
                    eva=self.alphabeta_Minimax(depth-1,not player_number,alpha,beta)
                    maxEva=max(maxEva,eva)
                    alpha=max(alpha,maxEva)
                    if beta<=alpha:
                         break
                    self.board.imaginary_board_grid=np.copy(save_board)
            return maxEva
        else:
            moves=self.get_moves(range_n[0],range_n[1],step,player_number,self.board.get_imaginary_board(),self.board)
            for move in moves:
                    save_board=np.copy(self.board.get_imaginary_board())
                    if self.board.is_move_valid(self.board.get_imaginary_board(), move,player_number):
                        self.board.place_piece_imaginary(move,player_number)
                    eva= self.alphabeta_Minimax(depth-1,not player_number,alpha,beta)
                    maxEva=min(maxEva,eva)
                    beta=min(beta,eva)
                    if beta<=alpha:
                         break
                    self.board.imaginary_board_grid=np.copy(save_board)
            return maxEva
    
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