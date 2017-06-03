# Snake Game!

import pygame, sys, random, time

def gameOver():
    my_font = pygame.font.SysFont('monaco', 72)
    game_over_surface = my_font.render('Game over!', True, red)
    game_over_rectangle = game_over_surface.get_rect()
    game_over_rectangle.midtop = (400, 15)  #(x, y)
    play_surface.blit(game_over_surface, game_over_rectangle)
    pygame.display.flip()
    time.sleep(5)
    pygame.quit()   # pygame exit
    sys.exit()  #console exit

def getSnakeFoodRandomPosition():
    # 10 multiplier equals to one snake step; important to catch food
    return [random.randrange(1, 80) * 10, random.randrange(1, 60) * 10]

# check for initializing errors
check_errors = pygame.init()
if check_errors[1] > 0:
    print ("Had {0} initializing errors...".format(check_errors[0]))
    sys.exit(-1)
else:
    print("PyGame successfully initialized!")

# Colors
red = pygame.Color(255, 0, 0)   # RGB colors; Gameover
green = pygame.Color(0, 150, 0) # snake
black = pygame.Color(0, 0, 0)   # score
# white = pygame.Color(255, 255, 255) # background
brown = pygame.Color(165, 42, 42)   # snake food
grey = pygame.Color(210, 210, 210)  # background

# Play surface
resolution = (800, 600) # (x, y)
play_surface = pygame.display.set_mode(resolution)
pygame.display.set_caption('Snake game!')
pygame.display.flip()

# FPS (frames-per-second) controller
fps_controller = pygame.time.Clock()

snake_pos = [100, 50]   # x and y of snake head = first block
snake_body = [[100, 50], [90, 50], [80, 50]]    # snake body at the beginning

food_pos = getSnakeFoodRandomPosition()
food_spawn = True

direction = 'RIGHT'
change_to = direction

# Main logic of the game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                change_to = 'RIGHT'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                change_to = 'LEFT'
            if event.key == pygame.K_UP or event.key == ord('w'):
                change_to = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                change_to = 'DOWN'
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))

    # validation of direction
    if change_to == 'RIGHT' and not direction == 'LEFT':
        direction = 'RIGHT'
    if change_to == 'LEFT' and not direction == 'RIGHT':
        direction = 'LEFT'
    if change_to == 'UP' and not direction == 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and not direction == 'UP':
        direction = 'DOWN'

    if direction == 'RIGHT':
        # [x, y]
        snake_pos[0] += 10
    if direction == 'LEFT':
        snake_pos[0] -= 10
    if direction == 'UP':
        snake_pos[1] -= 10
    if direction == 'DOWN':
        snake_pos[1] += 10

    # Snake body mechanism
    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        food_spawn = False
    else:
        snake_body.pop()

    if not food_spawn:
        food_pos = getSnakeFoodRandomPosition()
        food_spawn = True

    play_surface.fill(grey)    # draws clean surface

    for pos in snake_body:
        pygame.draw.rect(play_surface, green, pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.draw.rect(play_surface, brown, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    if snake_pos[0] > (resolution[0] - 10) or snake_pos[0] < 0 or \
        snake_pos[1] > (resolution[1] - 10) or snake_pos[1] < 0:
        gameOver()

    for body_block in snake_body[1:]:
        if snake_pos[0] == body_block[0] and snake_pos[1] == body_block[1]:
            gameOver()

    pygame.display.flip()
    fps_controller.tick(22) # 25 frames per second