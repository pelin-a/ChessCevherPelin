import Board
class Game:
    
    def __init__(self):
        print("Game Started")
        self.board=Board()
    
    
    def initialize_game(self):
        self.board= Board()
    
    def end_game(self):
        pass
        
    def validate(self,start,end) -> bool:
        pass
    
    def in_check(self, start,end) ->bool:
        pass
    
    def in_checkmate(self)->bool:
        """if self.in_check()==True:
            check if possible moves,
            check if after possible moves still in check,
            if yes it's checkmate"""
        pass
    
    def move(start:str,end:str):
        pass
    
    def check_full()-> list:
        return [True,"B"] #"B" if there is a black piece "W" if there is a white piece