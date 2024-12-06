from Board import Board
class Piece:
    """Class for representing all different pieces in the chess game and their specific methods"""
    
    def __init__(self,color,location,symbol):
        self.color=color
        self.location=location
        self.symbol=symbol
    
    def get_piece_type(self):
        return self.piece_type
    
    #setter
    
    def get_color(self):
        return self.color
    
    #setter
    
    def get_location(self):
        return self.location
    
    def set_location(self,location):
        self.location=location
        
    
        
    
    

#will inherit from piece class, will have their own movement logic        
#TODO: getters, setters, move_piece() for each class
class Pawn(Piece):
    def __init__(self,color,location):
        super().__init__(color,location)
    
    def validate_move(self,end,board:Board):
        start =self.get_location()
        start_row=int(start[1])   # Convert '1'-'8' to 0-7
        start_column=ord(start[0]) - ord('a')  # Convert 'a'-'h' to 0-7
        
        end_row= int(end[1]) 
        end_column=ord(end[0]) - ord('a')
        
        if self.color=="white":
            direction=1
        else:
            direction=-1
        print(direction)   
        #End row can only be current row+1 if white and current row-1 if black
        possible_row=start_row+direction
        print(possible_row) 
        if start_column==end_column and end_row==possible_row:
            if not board.check_full(end)[0]:
                return True
            
        #check for diognal move if there is a piece to win    
        if abs(int(start_column)-int(end_column))==1 and end_row==possible_row:
                if board.check_full(end):
                    #win_piece(end)
                    return True
        return False
                
                
                 
            
            
            
        
        

        
        
        
    
class Rook:
    pass
class Knight:
    pass
class Bishop:
    pass
class Queen:
    pass
class King:
    pass
        
pawn=Pawn("white","e2")
board=Board()
#assert pawn.validate_move("e3",board) ==True
assert pawn.validate_move("d3",board)==True    