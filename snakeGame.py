# Snake Game!

import pygame, sys, random, time

def gameOver():
    my_font = pygame.font.SysFont('monaco', 72)
    game_over_surface = my_font.render('Game over!', True, red)
    game_over_rectangle = game_over_surface.get_rect()
    game_over_rectangle.midtop = (400, 15)  #(x, y)
    play_surface.blit(game_over_surface, game_over_rectangle)
    pygame.display.flip()


# check for initializing errors
check_errors = pygame.init()
if check_errors[1] > 0:
    print ("Had {0} initializing errors...".format(check_errors[0]))
    sys.exit(-1)
else:
    print("PyGame successfully initialized!")

# Play surface
resolution = (800, 600) # (x, y)
play_surface = pygame.display.set_mode(resolution)
pygame.display.set_caption('Snake game!')

# Colors
red = pygame.Color(255, 0, 0)   # RGB colors; Gameover
green = pygame.Color(0, 255, 0) # snake
black = pygame.Color(0, 0, 0)   # score
white = pygame.Color(255, 255, 255) # background
brown = pygame.Color(165, 42, 42)   # snake food

# FPS (frames-per-second) controller
fps_controller = pygame.time.Clock()

snake_pos = [100, 50]   # x and y of snake head = first block
snake_body = [[100, 50], [90, 50], [80, 50]]    # snake body at the beginning

food_pos = [random.randrange(1, 80) * 10, random.randrange(1, 60) * 10] # 10 multiplier is important to catch food
food_spawn = True

direction = 'RIGHT'
change_to = direction

gameOver()
time.sleep(10)