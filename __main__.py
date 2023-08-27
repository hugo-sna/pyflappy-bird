import pyray as rl
import math
import random

# Local files
from Game import Game
from Player import Player
from Pipe import Pipe

def main() -> None:
    # Raylib settings
    rl.init_window(640, 360, 'PyFlappy bird')
    rl.set_target_fps(144)

    # Game code
    game: Game          = Game()
    player: Player      = Player()
    camera: rl.Camera2D = rl.Camera2D((320, 180), (0, 0), 0, 1)

    game.status = game.status.idle # Set default status to idle
    pipes = [] # Stores all the pipes on screen
    lastTime = 0 # Last time a pipe spawne

    # Main loop
    while not rl.window_should_close():
        rl.clear_background(rl.BLACK) # Clear the display
        rl.begin_drawing()
        rl.begin_mode_2d(camera)

        player.update()

        if rl.is_key_down(rl.KeyboardKey.KEY_SPACE):
            if game.status is game.status.idle:
                game.status = game.status.playing
        
        if game.status is game.status.idle: # Play the animation of the player bouncing
            # Generating a sin wave to animate the player
            ampl: float  = 10 # Wave's amplitude
            freq: float  = 1.5  # Wave's frequency
            player.collider.y = int(ampl * math.sin(2 * math.pi * freq * rl.get_time()))
            rl.draw_text('Press space to start playing', int(rl.measure_text('Press space to start playing', 25)/2-320), 50, 25, rl.WHITE)

            rl.end_mode_2d()
            rl.end_drawing()
            continue # Skip the loop iteration
        
        # Gameplay code
        if rl.get_time() - lastTime >= 1.5: # Spawn a pipe if delta time 
            pipes.append(Pipe())
            lastTime = rl.get_time()
            player.score += 1

        for pipe in pipes:
            pipe.update() # Simulate pipes
            if rl.check_collision_recs(pipe.rectTop, player.collider) or rl.check_collision_recs(pipe.rectBottom, player.collider): # Check collision with pipes
                player = Player()
                pipes = []
                game.status = game.status.idle

        if len(pipes) >= 5:
            pipes.pop(0)    

        rl.end_mode_2d()

        # Debug code
        #if len(pipes) > 0:
        #    txt = ''
        #    for i, pipe in enumerate(pipes):
        #        txt += f'Pipe{i}: x={pipe.rectTop.x}\n'
        #    rl.draw_text(txt, 0, 0, 7, rl.WHITE)
        rl.draw_text(f'Score: {player.score}', 0, 0,15, rl.WHITE)
        rl.end_drawing()

if __name__ == '__main__':
    main()
