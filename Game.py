from Board import Board
from Player import Player
class Game:
    
    def __init__(self):
        self.player1=None
        self.player2=None
        self.board=Board()
        self.game=True
    
    
    def start_game(self):
        print("Game Started")
        self.initialize_players()
        game=self.game
        player1_turn=True
        while game:
            self.board.print_board()
            if player1_turn:
                self.turn(self.player1)
                self.board.print_board()
                player1_turn=False
            else:
                self.turn(self.player2)
                player1_turn=True
        return self.end_game()        
                

    def end_game(self):
        pass
    
    
    def initialize_players(self):
        player1_name= input("Enter a name for player 1: ").strip().upper()
        player1_color=input("Enter your color ('white' for White, 'black' for Black): ").strip().lower()
        while player1_color not in ("white", "black"):
            print("Invalid input. Enter your color ('white' for White, 'black' for Black): ")
            player1_color = input().strip().lower()
        player2_name=input("Enter a name for player 2: ").strip().upper()
        player2_color="white" if player1_color=="black" else "black"
        self.player1=Player(player1_name,player1_color)
        self.player2=Player(player2_name,player2_color)
 
    def win_piece(player,piece):
        pass
    
    def in_check(self, start,end) ->bool:
        pass
    
    def in_checkmate(self)->bool:
        """if self.in_check()==True:
            check if possible moves,
            check if after possible moves still in check,
            if yes it's checkmate"""
        pass
    
    def turn(self,player)->bool:
        #returns False when the turn is over
        
        pass
    
    def move(self,player):
        board=self.board.get_board()
        start=input("Enter the starting point of the piece you want to play: ")
        if self.check_valid_start(start,player)==True:
            piece=board[start]  
            end=input("Enter the destination: ")
            if end in piece.possible_moves(self.board):
                if self.board.board_get_piece(end) !=None:
                    piece_to_replace=self.board.board_get_piece(end)
                    self.win_piece(player,piece_to_replace)
                board[end]=piece
                board[start]=None 
                piece.set_location(end)
            else:
                print("This move is not possible")
                return self.move(player)
        else:
            return self.move(player)        
                

            
        
    def check_valid_start(self,sqr,player):
        if self.board.get_board()[sqr]==None:
            print("This square is empty")
            return False
        if sqr in self.board.get_board().keys():
            color=player.get_color()
            if self.board.get_board()[sqr].get_color()==color:
                return True
            else:
                print("You cannot play this piece.")
                return False
        else:
            print("Invalid input")
            return False
            
        
player1=Player("Pelin","white")
game=Game()

game.board.print_board()
game.move(player1)    
game.board.print_board()