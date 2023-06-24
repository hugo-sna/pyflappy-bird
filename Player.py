import pyray as rl

class Player:
    score: int      = 0
    velocity: int   = 0
    jumpHeight: int = 10
    collider: rl.Rectangle = None

    def __init__(self) -> None:
        self.collider = rl.Rectangle(0, 0, 10, 10)

    def update(self) -> None:
        if rl.is_key_pressed(rl.KeyboardKey.KEY_SPACE) and self.jumpHeight is 15:
            self.jumpHeight = 0

        if self.jumpHeight < 15:
            self.collider.y -= 2
            self.jumpHeight += 1
        else:
            self.collider.y += 0.5

        rl.draw_circle(int(self.collider.x), int(self.collider.y), 10, rl.RED)

 