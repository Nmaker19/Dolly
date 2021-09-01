import pygame as pg
from random import randrange
import dolly
import drawing

# Variables ###########################################
IMAGENUMBER   = 16        # How many image it will draw
SAVEDIRECTORY = './files' # Image directory
COLORNUMBER = 8          # Numbers of colors can clamp
ORDER = [                 # Drawing order
	# Type,        Necesary?
	['background',	True],
	['body',		True],
	['sides',		False],
	['front',		True],
	['top',        False]
]

# Main functions
def make_random(order, n, savedir):
	# Make a random number of
	# Seeds and save them
	seeds = []
	for y in range(0, n):

		seeds.append(dolly.make_seed(order, 0.5, 0.5, [0, 255], 16))
		print('seed - {}: {}\n'.format(y, seeds[y]))
		pg.image.save(pg.transform.scale(dolly.draw_seed(seeds[y]), [320, 320]), '{}/{}.png'.format(savedir, y))

	return seeds

def make_from_seed(seed, savedir):
	pg.image.save(pg.transform.scale(dolly.draw_seed(seed), [320, 320]), '{}/{}.png'.format(SAVEDIRECTORY, 0))

# Main

make_random(ORDER, 32, SAVEDIRECTORY)
#make_from_seed([['./assets/img/background/0/0.png', [11, 100, 255, 255]], ['./assets/img/body/0/0.png', [255, 236, 204, 255]], ['./assets/img/front/0/2.png', [0, 0, 0, 255]], ['./assets/img/top/0/4.png', [20, 20, 20, 255]], ['./assets/img/top/1/1.png', [255, 213, 0, 255]], ['./assets/img/top/1/1-1.png', [226, 0, 42, 255]]], SAVEDIRECTORY)