from Piece import Pawn, Rook, Knight, Bishop, Queen, King  
class Board:
    
    def __init__(self) -> None:
        #creates a board structure that is a dictionary and the keys are the nmaes of the squares, the values are the piece objects
        self.board = {f"{col}{row}": None for col in "abcdefgh" for row in "87654321"}
        self.place_pieces()
    
    def get_board(self):
        return self.board 
    def generate_pieces(self):
        pieces = [
        Rook("white", "a1"), Knight("white", "b1"), Bishop("white", "c1"), Queen("white", "d1"),
        King("white", "e1"), Bishop("white", "f1"), Knight("white", "g1"), Rook("white", "h1"),
        Pawn("white", "a2"), Pawn("white", "b2"), Pawn("white", "c2"), Pawn("white", "d2"),
        Pawn("white", "e2"), Pawn("white", "f2"), Pawn("white", "g2"), Pawn("white", "h2"),

        Rook("black", "a8"), Knight("black", "b8"), Bishop("black", "c8"), Queen("black", "d8"),
        King("black", "e8"), Bishop("black", "f8"), Knight("black", "g8"), Rook("black", "h8"),
        Pawn("black", "a7"), Pawn("black", "b7"), Pawn("black", "c7"), Pawn("black", "d7"),
        Pawn("black", "e7"), Pawn("black", "f7"), Pawn("black", "g7"), Pawn("black", "h7")
        ]
        return pieces
    
    def board_get_piece(self,key):
        return self.board[key]
    
    def remove_piece(self,key):
        self.board[key]=None
        
    def place_pieces(self)-> None: 
        # does the inital placement of pieces on board, 
        pieces=self.generate_pieces()
        for piece in pieces:
            location=piece.get_location()
            if location in self.board:
                self.board[location]=piece
    

    def print_board(self):
        print("\n     A   B   C   D   E   F   G   H")
        print("   +---+---+---+---+---+---+---+---+")
        board = [{} for i in range(8)] # creating 8 dictionariies, each representing a row inside the board dictionary, for display purposes

            
        for square, piece in self.board.items():
            row_index = 8 - int(square[1])  # first row's index is 0, but because of the board layout it corresponds to 8, so we are substracting the row nummber from 8 so that they are the same
            board[row_index][square] = piece

        # Print each row
        for row_index, row in enumerate(board):
            row_number = 8 - row_index  
            row_str = f"{row_number} |"
            for column in "abcdefgh":
                square = f"{column}{row_number}"
                piece = row.get(square, None)
                row_str += f" {piece.symbol if piece else ' '} |"
            print(row_str)
            print("   +---+---+---+---+---+---+---+---+")

                 
    
    def check_full(self,end)-> list:
        
        #returns a list, first element is bool 2nd is the color of the piece if there is a piece at the endpoint.
        is_full=False
        color=None
        piece=self.board[end]
        if piece:
            is_full=True 
            color=piece.get_color()
                
        return [is_full,color] #"B" if there is a black piece "W" if there is a white piece 
   

#board=Board()
#piece=Pawn("white","a4")
#print(piece.possible_moves(board))
#board.print_board2()
#print(board.check_full("a2"))
    