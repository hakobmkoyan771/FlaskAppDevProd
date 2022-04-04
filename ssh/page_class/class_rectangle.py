class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_width(self):
        return self.width
 
    def get_height(self):
        return self.height
   
    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height



class Square(Rectangle):
    
    def __init__(self, width, height):
        super().__init__(width , height)
 
    def get_square_diagonal(self):
        return self.width ** 2 * 2 * 0.5

    


  
   
