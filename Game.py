from Board import Board
from Player import Player
from copy import deepcopy
class Game:
    
    def __init__(self):
        self.player1=None
        self.player2=None
        self.board=Board()
        self.game=None
    
    
    def start_game(self):
        print("Game Started")
        self.initialize_players() # initializing players
        self.game=True 
        player1_turn=True
        while self.game: # while game is True the loop runs, until the game ends with a checkmate, and then the loop gets breaked.
            self.board.print_board()
            if player1_turn:
                self.move(self.player1) # here I am checking if there is a check or checkmate after for either players after each move. 
                if not self.game: #breaking the loop if the game ended.
                    break
                if self.in_check(self.player2):
                    print(f"{self.player2.get_name()} is in CHECK!")
                if self.in_check(self.player1):
                    print(f"{self.player1.get_name()} is in CHECK!")
                if self.checkmate(self.player2):
                    print(f"{self.player2.get_name()} is in CHECKMATE.")
                    self.end_game(self.player1)
                    break # game ends, loop breaks if there is a checkmate.
                if self.checkmate(self.player1):
                    print(f"{self.player1.get_name()} is in CHECKMATE.")
                    self.end_game(self.player2)
                    break
                player1_turn=False
            else:
                self.move(self.player2) # same logic for player 2
                if not self.game:
                    break
                if self.in_check(self.player2):
                    print(f"{self.player2.get_name()} is in CHECK!")
                if self.checkmate(self.player2):
                    print(f"{self.player2.get_name()} is in CHECKMATE.")
                    self.end_game(self.player1)
                    break
                if self.in_check(self.player1):
                    print(f"{self.player1.get_name()} is in CHECK!")
                if self.checkmate(self.player1):
                    print(f"{self.player1.get_name()} is in CHECKMATE.")
                    self.end_game(self.player2)
                    break    
                
                player1_turn=True
        print("THE GAME HAS ENDED! WELL DONE!")      
                
    # ends game by setting game attribute to false.
    def end_game(self, player):
        print(f"{player.get_name()} has won the game!!")
        self.game=False
        
    
    
    def initialize_players(self): # gets names of the players and their colors, assigns numbers to players.
        player1_name= input("Enter a name for player 1: ").strip().upper()
        player1_color=input("Enter your color ('white' for White, 'black' for Black): ").strip().lower()
        while player1_color not in ("white", "black"):
            print("Invalid input. Enter your color ('white' for White, 'black' for Black): ")
            player1_color = input().strip().lower()
        player2_name=input("Enter a name for player 2: ").strip().upper()
        player2_color="white" if player1_color=="black" else "black"
        self.player1=Player(player1_name,player1_color,1) # creates Player objects.
        self.player2=Player(player2_name,player2_color,2)
    
   
    def win_piece(self,player,piece): # adds a piece to player's bag, removes piece from the board.
        player.bag.append(piece)
        self.board.remove_piece(piece.get_location())
        print(f"{player.get_name()} won {piece.get_color()}{piece.get_name()}")
        
       
    
    def in_check(self,player) ->bool: # accepts a player object and check if it's king can possibly be attacked.
        
        opponent = self.player1 if player.get_number()==2 else self.player2
        player_king_location= self.board.get_king(player).get_location()
        safe=self.board.safe_move(player_king_location,opponent.get_color()) # safe==True if king's location cannot be reached if any of the opponent's pieces.
        if not safe:
            return True
        return False

        #if player's king's location is not safe, then it's check
        
    
    
    def checkmate(self,player)->bool: # check's if the player is in checkmate.
        opponent = self.player1 if player.get_number()==2 else self.player2
        king = self.board.get_king(player)
        
        if not self.in_check(player): # if it's not in check, then it cannot be in checkmate.
            return False
        
        for move in king.possible_moves(self.board): # if the king can escape the the check with a possible move, then it is not checkmate.
            if self.board.safe_move(move,player.get_color()):
                return False
        
        for key, piece in self.board.get_board().items(): # if the attack can be blocked by any of the player's pieces than it isnot checkmate.
            if piece and piece.get_color() == player.get_color():
                for move in piece.possible_moves(self.board):
                    # hypothetical move
                    simulated_board = deepcopy(self.board) # deepcopy is creating a copy of the board object in order to simulate a move that may block the check without changing the original board.
                    simulated_board.move_piece(key, move)
                    if simulated_board.safe_move(king.get_location(), opponent.get_color()): # checking after the simulated move the king can be safe.
                        return False  # Another piece can resolve the check
        
        return True    
            
        
    
    #def turn(self,player)->bool:
        #game.move(player)
        #return False
        
    
    def move(self,player):# moves a players's piece on the board.
        board=self.board.get_board()
        opponent = self.player1 if player.get_number()==2 else self.player2
        print(f"It's {player.get_name()}'s turn.")
        while True:
            start=input("Enter the starting point of the piece you want to play: ") # inputting the square of the piece that is played. as e.g. "e3"
            if self.check_valid_start(start,player)==True: # checking if the square belongs to the player and can be played.
                piece=board[start]  # getting the piece object.
                end=input("Enter the destination: ")
                if end in piece.possible_moves(self.board): # checking if the endpoint is in possible moves of the piece.
                    if self.board.board_get_piece(end) !=None: # if there is a piece at the endpoint it get's replaced and won.
                        piece_to_replace=self.board.board_get_piece(end)
                        if piece_to_replace== self.board.get_king(opponent):
                            self.end_game(player)
                        else:
                            self.win_piece(player,piece_to_replace)
                    board[end]=piece
                    board[start]=None 
                    piece.set_location(end) # setting the new location.
                    break
                    # after the move is done the loop breaks.
                else:
                    print("This move is not possible") # error if move cannot be played.
                
            else:
                print("Invalid starting point. Try again.")
            
                

            
        
    def check_valid_start(self,sqr,player): # checks if the starting point belongs to the player and the square exists on the board.
        try:
            if self.board.get_board()[sqr]==None: # checking if the square has a piece.
                print("This square is empty")
                return False
            if sqr in self.board.get_board().keys():
                color=player.get_color()
                if self.board.get_board()[sqr].get_color()==color: # checking if the piece belongs to the 
                    return True
                else:
                    print("You cannot play this piece.")
                    return False
        except KeyError: # error if square cannot be find or mistyped.
            print("Invalid square name") 
            return False
            
        
