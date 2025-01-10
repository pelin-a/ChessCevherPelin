class Player:
    
    def __init__(self,name,color,number):
        self.number=number
        self.name=name
        self.color=color
        self.bag=[] #list of piece objects that the player won
        
    def get_name(self):
        return self.name
    
    def set_name(self,name):
        self.name=name
        
    def set_color(self,color):
        self.color=color
        
    def get_color(self):
        return self.color
    
    def get_bag(self):
        return self.bag
    
    def win_piece(self,piece):
        self.bag.append(piece)
       
    def empty_bag(self):
        self.bag.clear()
        
    def get_number(self):
        return self.number
    
    def set_number(self,number):
        self.number=number

