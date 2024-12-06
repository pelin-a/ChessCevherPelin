class Board:
    def __init__(self) -> None:
        self.board = [
            {"a1": "r", "b1": "n", "c1": "b", "d1": "q", "e1": "k", "f1": "b", "g1": "n", "h1": "r"},
            {"a2": "p", "b2": "p", "c2": "p", "d2": "p", "e2": "p", "f2": "p", "g2": "p", "h2": "p"},
            {"a3": "", "b3": "", "c3": "", "d3": "", "e3": "", "f3": "", "g3": "", "h3": ""},
            {"a4": "", "b4": "", "c4": "", "d4": "", "e4": "", "f4": "", "g4": "", "h4": ""},
            {"a5": "", "b5": "", "c5": "", "d5": "", "e5": "", "f5": "", "g5": "", "h5": ""},
            {"a6": "", "b6": "", "c6": "", "d6": "", "e6": "", "f6": "", "g6": "", "h6": ""},
            {"a7": "P", "b7": "P", "c7": "P", "d7": "P", "e7": "P", "f7": "P", "g7": "P", "h7": "P"},
            {"a8": "R", "b8": "N", "c8": "B", "d8": "Q", "e8": "K", "f8": "B", "g8": "N", "h8": "R"},
        ]
     
    def generate_pieces(self):
        pass    

    def print_board(self):
        
        print("\n     A   B   C   D   E   F   G   H")
        print("   +---+---+---+---+---+---+---+---+")
        
        for index, row in enumerate(self.board, start=1):
            row_str=f"{index} |"
            for  piece in row:
                row_str+= " "+f' {row.get(piece) if not "" else " "}'+" "
            print(row_str)
            print("   +---+---+---+---+---+---+---+---+")
    def get_row_index(row_num):
        return 8- row_num    
    
    def check_full(self,end)-> list:
        """#check if there is a piece at end square
        is_full=False
        color=None
        row =self.get_row_index(int(end[1]))
        piece=self.board[row][end]
        if piece:
            is_full=True 
            if piece.islower():
                
            
        return [False,None] #"B" if there is a black piece "W" if there is a white piece 
    """
"""board=Board()
board.print_board()"""
    