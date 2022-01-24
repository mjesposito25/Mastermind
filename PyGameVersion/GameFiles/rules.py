class Rules:
    def __init__(self):
        self.colors = ["red", "blue", "green", "yellow", "black", "white", "purple", "orange"]
        self.num_colors = 4
        self.repeat = False
        self.ordered = False
    
    def change_colors(self, num):
        self.num_colors = num
    
    def change_repeat(self, repeat):
        self.repeat = repeat
    
    def change_ordered(self, ordered):
        self.ordered = ordered
        
    def get_colors(self):
        return self.colors[:self.num_colors]
    
    def get_repeat(self):
        return self.repeat
    
    def get_ordered(self):
        return self.ordered
        