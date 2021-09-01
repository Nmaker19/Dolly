import pygame as pg
from os import listdir
from random import randrange

DIR = {
	'background':'./assets/img/background',
	'body':'./assets/img/body',
	'sides':'./assets/img/sides',
	'front':'./assets/img/front',
	'top':'./assets/img/top'
}

def clamp_color(number, colorrange):
	return round(number / colorrange)*colorrange

def make_list(maketype, necesary, prob, addonprob):
	# Return a surface with
	# a random image in his
	# acording to the draw
	# type.

	lis = []
	ldir = listdir(DIR[maketype])
	for x in ldir: # For each layer
		if not necesary:
			if not randrange(0, 101) <= (prob*100):
				continue
		else:
			if len(ldir) > 1 and x != ldir[0]:
				continue

		l = listdir(DIR[maketype] + '/' + x)
		if len(l) == 0:
			continue

		ilis = []
		for y in l:
			if not '-' in y:
				ilis.append(y)

		select = ilis[randrange(0, len(ilis))]

		alis = []
		for y in l:
			if ('{}-'.format(select.replace('.png', '').replace('+', ''))) in y:
				alis.append(y)
		lis.append('{}/{}/{}'.format(DIR[maketype], x, select))
		if len(alis) != 0 and randrange(0, 101) <= (addonprob*100):
			lis.append('{}/{}/{}'.format(DIR[maketype], x, alis[randrange(0, len(alis))]))

		if '+' in select:
			return lis
	return lis

def make_seed(order, prob, addonprob, r, cn):
	# Variables
	seed = []
	COLORRANGE = 255 / cn
	for a in order:
		lis = []
		ldir = listdir(DIR[a[0]])

		for x in ldir: # For each layer
			if not a[1]: # Is necesary?
				if not randrange(0, 101) <= (prob*100):
					continue
			else:
				if len(ldir) > 1 and x != ldir[0] and not randrange(0, 101) <= (prob*100):
					continue

			l = listdir(DIR[a[0]] + '/' + x)
			if len(l) == 0:
				continue

			ilis = []
			for y in l:
				if not '-' in y:
					ilis.append(y)

			select = ilis[randrange(0, len(ilis))]

			alis = []
			for y in l:
				if ('{}-'.format(select.replace('.png', '').replace('+', ''))) in y:
					alis.append(y)
			lis.append('{}/{}/{}'.format(DIR[a[0]], x, select))
			if len(alis) != 0 and randrange(0, 101) <= (addonprob*100):
				lis.append('{}/{}/{}'.format(DIR[a[0]], x, alis[randrange(0, len(alis))]))

			if '+' in select:
				for z in lis:
					seed.append([z, [clamp_color(randrange(r[0], r[1]), COLORRANGE), clamp_color(randrange(r[0], r[1]), COLORRANGE), clamp_color(randrange(r[0], r[1]), COLORRANGE)]])
					return seed

			for z in lis:
				seed.append([z, [clamp_color(randrange(r[0], r[1]), COLORRANGE), clamp_color(randrange(r[0], r[1]), COLORRANGE), clamp_color(randrange(r[0], r[1]), COLORRANGE)]])
	return seed

ORDER = [                 # Drawing order
	# Type,        Necesary?
	['background',	True],
	['body',		True],
	['sides',		False],
	['front',		True],
	['top',        False]
]

def draw_seed(seed):
	i = pg.Surface([64, 64])
	for step in seed:	
		o = pg.image.load(step[0])
		#o.fill([step[2], step[2], step[2], step[2]], special_flags=pg.BLEND_RGB_SUB)
		print(step[1][0])
		o.fill([step[1][0], step[1][1], step[1][2]], special_flags=pg.BLEND_RGB_MULT)
		i.blit(o, [0, 0])

	return i