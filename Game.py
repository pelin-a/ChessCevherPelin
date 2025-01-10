from Board import Board
from Player import Player
from copy import deepcopy
class Game:
    
    def __init__(self):
        self.player1=None
        self.player2=None
        self.board=Board()
        self.game=True
    
    
    def start_game(self):
        print("Game Started")
        board=self.board
        self.initialize_players()
        game=self.game
        player1_turn=True
        while game:
            self.board.print_board()
            if player1_turn:
                self.move(self.player1)
                #self.turn(self.player1)
                board.print_board()
                if self.in_check(self.player2)==True:
                    print(f"{self.player2.get_name()} is in CHECK!")
                if self.checkmate(self.player2)== True:
                    print(f"{self.player2.get_name()} is in CHECKMATE. {self.player1.get_name()} has won the game!")
                    self.end_game()
                player1_turn=False
            else:
                
                self.move(self.player2)
                #self.turn(self.player2)
                player1_turn=True
        return self.end_game()        
                
    #TODO:
    def end_game(self):
        self.game=False
        
    
    
    def initialize_players(self):
        player1_name= input("Enter a name for player 1: ").strip().upper()
        player1_color=input("Enter your color ('white' for White, 'black' for Black): ").strip().lower()
        while player1_color not in ("white", "black"):
            print("Invalid input. Enter your color ('white' for White, 'black' for Black): ")
            player1_color = input().strip().lower()
        player2_name=input("Enter a name for player 2: ").strip().upper()
        player2_color="white" if player1_color=="black" else "black"
        self.player1=Player(player1_name,player1_color,1)
        self.player2=Player(player2_name,player2_color,2)
    
   
    def win_piece(self,player,piece):
        player.bag.append(piece)
        self.board.remove_piece(piece.get_location())
        print(f"{player.get_name()} won {piece.get_color()}{piece.get_name()}")
        
       
    #TODO:
    def in_check(self,player) ->bool:
        opponent = self.player1 if player.get_number()==2 else self.player2
        player_king_location= self.board.get_king(player).get_location()
        safe=self.board.safe_move(player_king_location,opponent.get_color())
        if not safe:
            return True
        return False

        #if player's king's location is not safe, then it's check
        
    
    
    def checkmate(self,player)->bool:
        opponent = self.player1 if player.get_number()==2 else self.player2
        king = self.board.get_king(player)
        if not self.in_check(player):
            return False
        
        for move in king.possible_moves(self.board):
            if self.board.safe_move(move,player.get_color()):
                return False
        
        for key, piece in self.board.get_board().items():
            if piece and piece.get_color() == player.get_color():
                for move in piece.possible_moves(self.board):
                    # hypothetical move
                    simulated_board = deepcopy(self.board) 
                    simulated_board.move_piece(key, move)
                    if simulated_board.safe_move(king.get_location(), opponent.get_color()):
                        return False  # Another piece can resolve the check
        
        return True    
            
        
    
    def turn(self,player)->bool:
        game.move(player)
        return False
        
    
    def move(self,player):
        board=self.board.get_board()
        print(f"It's {player.get_name()}'s turn.")
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
                #self.in_check(piece,player)
            else:
                print("This move is not possible")
                return self.move(player)
        else:
            return self.move(player)        
                

            
        
    def check_valid_start(self,sqr,player):
        try:
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
        except KeyError:
            print("Invalid suare name") 
            return False
            
        
#player1=Player("Pelin","white")
game=Game()

game.start_game()
"""board=Board()
player1=Player("pp","white",1)
print(board.get_king_location(player1))"""