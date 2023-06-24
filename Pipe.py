from pyray import draw_rectangle_rec, GREEN, RED, Rectangle, check_collision_recs

import random

class Pipe:
    openingTop: int    = 0
    openingBottom: int = 0
    rectTop: Rectangle   = None
    rectBottom: Rectangle = None


    def __init__(self) -> None:
        self.openingTop    = random.randint(20, 50)
        self.openingBottom = random.randint(20, 50)
        self.rectTop: Rectangle    = Rectangle(320, -180 - self.openingTop, 75, 180)
        self.rectBottom: Rectangle = Rectangle(320, 10 + self.openingBottom, 75, 180)
        
    
    def update(self) -> None:
        self.rectTop.x    -= 1
        self.rectBottom.x -= 1
        draw_rectangle_rec(self.rectTop, GREEN) # top rectangle
        draw_rectangle_rec(self.rectBottom, GREEN) # bottom rectangle
        