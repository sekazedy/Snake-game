# Snake Game!

import pygame, sys, random, time, os


def gameOver():
	my_font = pygame.font.SysFont('monaco', 72)
	game_over_surface = my_font.render('Game over!', True, red)
	game_over_rectangle = game_over_surface.get_rect()
	game_over_rectangle.midtop = (400, 15)  #(x, y)
	play_surface.blit(game_over_surface, game_over_rectangle)
	showScore(True)
	pygame.display.flip()
	time.sleep(5)
	pygame.quit()   # pygame exit
	sys.exit()  #console exit

def getSnakeFoodRandomPosition():
	# 10 multiplier equals to one snake step; important to catch food
	return [random.randrange(1, 80) * 10, random.randrange(1, 60) * 10]

def showScore(end_game_score = False):
	if end_game_score:
		score_font = pygame.font.SysFont('monaco', 48)
		score_surface = score_font.render('Your final score: {0}'.format(score),
			True, black)
	else:
		score_font = pygame.font.SysFont('monaco', 32)
		score_surface = score_font.render('Score: {0}'.format(score), True, black)
	score_rectangle = score_surface.get_rect()
	if end_game_score:
		score_rectangle.midtop = (400, 120)  #(x, y)
	else:
		score_rectangle.midtop = (80, 10)  #(x, y)
	play_surface.blit(score_surface, score_rectangle)

def quit_game():
	pygame.event.post(pygame.event.Event(pygame.QUIT))

def text_objects(text, font):
	text_surf = font.render(text, True, black)
	return text_surf, text_surf.get_rect()

def button(text, x, y, width, height, main_color, highlight_color, action=None):
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()

	if x+width > mouse[0] > x and y+height > mouse[1] > y:
		pygame.draw.rect(play_surface, highlight_color, (x, y, width, height))
		if click[0] == 1 and action != None:
			action()
	else:
		pygame.draw.rect(play_surface, main_color, (x, y, width, height))

	btn_text_font = pygame.font.SysFont('monaco', 36)
	text_surf, text_rect = text_objects(text, btn_text_font)
	text_rect.center = ( (x + (width/2)), (y + (height/2)) )
	play_surface.blit(text_surf, text_rect)

def game_loop():
	food_pos = getSnakeFoodRandomPosition()
	food_spawn = True
	direction = 'RIGHT'
	change_to = direction
	global score

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
					quit_game()

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
			score += 1
		else:
			snake_body.pop()

		if not food_spawn:
			food_pos = getSnakeFoodRandomPosition()
			food_spawn = True

		play_surface.fill(light_grey)	# draws clean surface

		for pos in snake_body:
			pygame.draw.rect(play_surface, green, pygame.Rect(pos[0], pos[1], 10, 10))

		pygame.draw.rect(play_surface, brown,
			pygame.Rect(food_pos[0], food_pos[1], 10, 10))

		if snake_pos[0] > (resolution[0] - 10) or snake_pos[0] < 0 or \
			snake_pos[1] > (resolution[1] - 10) or snake_pos[1] < 0:
			gameOver()

		for body_block in snake_body[1:]:
			if snake_pos[0] == body_block[0] and snake_pos[1] == body_block[1]:
				gameOver()

		showScore()
		pygame.display.flip()
		fps_controller.tick(22) # 22 frames per second

		# TODO:
		# add menu
		# add sounds
		# change speed according to score (or difficulty level)
		# add settings
		# try to add image

'''def game_loop():
	# variables
	snake_pos = [100, 50]   # x and y of snake head = first block
	snake_body = [[100, 50], [90, 50], [80, 50]]	# snake body at the beginning

	food_pos = getSnakeFoodRandomPosition()
	food_spawn = True

	direction = 'RIGHT'
	change_to = direction

	score = 0

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
					quit_game()

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
			score += 1
		else:
			snake_body.pop()

		if not food_spawn:
			food_pos = getSnakeFoodRandomPosition()
			food_spawn = True

		play_surface.fill(light_grey)	# draws clean surface

		for pos in snake_body:
			pygame.draw.rect(play_surface, green, pygame.Rect(pos[0], pos[1], 10, 10))

		pygame.draw.rect(play_surface, brown,
			pygame.Rect(food_pos[0], food_pos[1], 10, 10))

		if snake_pos[0] > (resolution[0] - 10) or snake_pos[0] < 0 or \
			snake_pos[1] > (resolution[1] - 10) or snake_pos[1] < 0:
			gameOver()

		for body_block in snake_body[1:]:
			if snake_pos[0] == body_block[0] and snake_pos[1] == body_block[1]:
				gameOver()

		showScore()
		pygame.display.flip()
		fps_controller.tick(22) # 22 frames per second

		# TODO:
		# add menu
		# add sounds
		# change speed according to score (or difficulty level)
		# add settings
		# try to add image'''

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
pygame.display.flip()

# set window icon
game_icon = pygame.image.load(os.path.join('images', 'snake_icon.jpg'))
pygame.display.set_icon(game_icon)

# Colors
red = pygame.Color(150, 0, 0)   # RGB colors; Gameover
light_red = pygame.Color(230, 50, 50)
green = pygame.Color(0, 180, 0) # snake
light_green = pygame.Color(50, 230, 50)
black = pygame.Color(0, 0, 0)   # score
brown = pygame.Color(165, 42, 42)   # snake food
light_grey = pygame.Color(230, 230, 230)  # background

# FPS (frames-per-second) controller
fps_controller = pygame.time.Clock()

# variables
snake_pos = [100, 50]   # x and y of snake head = first block
snake_body = [[100, 50], [90, 50], [80, 50]]	# snake body at the beginning

score = 0

# Game intro
intro = True
while intro:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
			quit_game()

	play_surface.fill(light_grey)
	title_font = pygame.font.SysFont('monaco', 128)
	game_intro_surface = title_font.render('Snake', True, light_green)
	game_intro_rectangle = game_intro_surface.get_rect()
	game_intro_rectangle.midtop = (400, 75)  #(x, y)
	play_surface.blit(game_intro_surface, game_intro_rectangle)

	button("START", 150, 350, 150, 80, green, light_green, game_loop)
	button("QUIT", 500, 350, 150, 80, red, light_red, quit_game)

	pygame.display.flip()
	fps_controller.tick(15)