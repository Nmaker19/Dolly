import pygame as pg
from random import randrange

def colored_image(d):
	i = pg.image.load(d)
	i.fill([randrange(0, 256), randrange(0, 256), randrange(0, 256)], special_flags=pg.BLEND_RGB_MAX)
	return i

def dark_image(d, p):
	i = pg.image.load(d)
	o = i.copy()

	percent = p*255
	o.fill([percent, percent, percent, percent], special_flags=pg.BLEND_RGB_SUB)
	r = [0, 128]
	o.fill([randrange(r[0], r[1]), randrange(r[0], r[1]), randrange(r[0], r[1])], special_flags=pg.BLEND_RGB_SUB)
	return o
