
class Piece:
    """Class for representing all different pieces in the chess game and their specific methods"""
    
    def __init__(self,color,location,symbol):
        self.color=color
        self.location=location
        self.symbol=symbol
    
    #def get_piece_type(self):
        #return self.piece_type
    
    #setter
    
    def get_color(self):
        return self.color
    
    #setter
    
    def get_location(self):
        return self.location
    
    def set_location(self,location):
        self.location=location
        
    def get_symbol(self):
        return self.symbol
        
    
    

#will inherit from piece class, will have their own movement logic        
#TODO: getters, setters, move_piece() for each class
class Pawn(Piece):
    def __init__(self,color,location):
        symbol="P" if color == "white" else "p"
        super().__init__(color,location,symbol)
        
    def possible_moves(self,board):
        #returns a list of the possible moves Piece object can have
        possible_moves = []
        start_col = self.location[0]  
        start_row = int(self.location[1])  
        direction = 1 if self.color == "white" else -1
        
        # ine square forward
        forward_row = start_row + direction
        if 1 <= forward_row <= 8:  # Check if within board limits
            forward_move = f"{start_col}{forward_row}"
            if board.board_get_piece(forward_move)==None:
                
                possible_moves.append(forward_move)
        
        # if it is the first move of the pawn, it can move 2 squares
        if (self.color == "white" and start_row == 2) or (self.color == "black" and start_row == 7):
            double_forward_row = start_row + (2 * direction)
            double_forward_move = f"{start_col}{double_forward_row}"
            intermediate_square = f"{start_col}{forward_row}"
            if (
           board.board_get_piece(intermediate_square)==None and  # if pawn is moving 2 squares, the square in betwween must be empty
            board.board_get_piece(double_forward_move)==None  # Destination square must also be empty
        ):
             possible_moves.append(double_forward_move)
        
        # Diagonal moves to win pieces
        left_diagonal_col = chr(ord(start_col) - 1)  
        right_diagonal_col = chr(ord(start_col) + 1)  
        
        for diagonal_col in [left_diagonal_col, right_diagonal_col]:
            if 'a' <= diagonal_col <= 'h':  #checking if within board limits and there is a piece to win
                diagonal_row = forward_row
                if 1 <= diagonal_row <= 8:
                    diagonal_move=f"{diagonal_col}{diagonal_row}"
                    
                    if board.board_get_piece(diagonal_move)!=None and board.board_get_piece(diagonal_move).get_color() != self.color:  
                        possible_moves.append(diagonal_move)
        
        return possible_moves
                
            
            
        
        
    def validate_move(self,end,board):
        start =self.get_location()
        start_row=int(start[1])   # Convert '1'-'8' to 0-7
        start_column=ord(start[0]) - ord('a')  # Convert 'a'-'h' to 0-7
        
        end_row= int(end[1]) 
        end_column=ord(end[0]) - ord('a')
        
        if self.color=="white":
            direction=1
        else:
            direction=-1   
        #End row can only be current row+1 if white and current row-1 if black
        possible_row=start_row+direction 
        if start_column==end_column and end_row==possible_row:
            if not board.check_full(end)[0]:
                return True
            
        #check for diognal move if there is a piece to win    
        if abs(int(start_column)-int(end_column))==1 and end_row==possible_row:
                if board.check_full(end):
                    #win_piece(end)
                    return True
        return False
                
  
class Rook(Piece):
    def __init__(self,color,location):
        super().__init__(color,location,"R" if color == "white" else "r")
    
    #TODO:    
    def possible_moves(self,board)->list:
        #returns a list of possible,legal moves a piece can make
        pass
        
class Knight(Piece):
    def __init__(self,color,location):
        symbol="N" if color == "white" else "n"
        super().__init__(color,location,symbol)
        
        #TODO:    
    def possible_moves(self,board)->list:
        #returns a list of possible,legal moves a piece can make
        pass
        
class Bishop(Piece):
    def __init__(self,color,location):
        symbol= "B" if color == "white" else "b"
        super().__init__(color,location,symbol)
        
        #TODO:    
    def possible_moves(self,board)->list:
        #returns a list of possible,legal moves a piece can make
        pass
        
class Queen(Piece):
    def __init__(self,color,location):
        symbol="Q" if color == "white" else "q"
        super().__init__(color,location,symbol)
        
        #TODO:    
    def possible_moves(self,board)->list:
        #returns a list of possible,legal moves a piece can make
        pass
        
class King(Piece):
    def __init__(self,color,location):
        symbol="K" if color == "white" else "k"
        super().__init__(color,location,symbol)
        
        #TODO:    
    def possible_moves(self,board)->list:
        #returns a list of possible,legal moves a piece can make
        pass
        
pawn=Pawn("white","e2")

