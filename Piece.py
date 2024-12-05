class Piece:
    """Class for representing all different pieces in the chess game and their specific methods"""
    
    def __init__(self,piece_type,color):
        self.piece=piece_type
        self.color=color

#will inherit from piece class, will have their own movement logic        
#TODO: getters, setters, move_piece() for each class
class Pawn:
    pass
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
        
    