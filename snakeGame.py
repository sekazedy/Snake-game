# Snake Game!

import pygame, sys, random, time

# check for initializing errors
check_errors = pygame.init()
if check_errors[1] > 0:
    print ("Had {0} initializing errors...".format(check_errors[0]))
    sys.exit(-1)
else:
    print("PyGame successfully initialized!")

# Play surface
resolution = (800, 600)
playSurface = pygame.display.set_mode(resolution)
pygame.display.set_caption('Snake game!')
time.sleep(5)