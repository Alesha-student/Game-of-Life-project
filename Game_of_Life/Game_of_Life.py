import copy

import pygame as pg
from random import randint

width_count, height_count = 180, 100
size = 8
resolution = width, height = width_count * size + 1, height_count * size + 1
FPS = 20

screen = pg.display.set_mode(resolution)
clock = pg.time.Clock()

next_blocks_stage = [[0 for l in range(width_count)] for j in range(height_count)]
blocks = [[randint(0, 1) for l in range(width_count)] for j in range(height_count)]

#Other patterns
#blocks = [[1 if not i % 10 else 0 for i in range(width_count)] for j in range(height_count)]
#blocks = [[1 if not (i*j) % 10 else 0 for i in range(width_count)] for j in range(height_count)]
#blocks = [[1 if i == width_count // 2 or  (j == height_count // 2) else 0 for i in range(width_count)] for j in range(height_count)]
'''blocks = [[0 for i in range(width_count)] for j in range(height_count)]
for i in range(height_count):
    blocks[i][i+(width_count-height_count) // 2]=1
    blocks[height_count-i-1][i+(width_count-height_count) // 2]=1'''


def check_block(field, pos):
    x, y = pos
    neighbors = 0
    for yS in range(y-1, y+2):
        for xS in range(x-1, x+2):
            if field[yS % height_count][xS % width_count] == 1:
                neighbors += 1

    if field[y][x] == 1:
        neighbors -= 1
        if neighbors == 2 or neighbors == 3:
            return 1
        else:
            return 0
    else:
        if neighbors == 3:
            return 1
        else:
            return 0


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            quit()

    screen.fill(pg.Color('black'))

    [pg.draw.line(screen, (78,78,78), (x,0), (x, height)) for x in range(0, width, size)]
    [pg.draw.line(screen, (78,78,78), (0,y), (width, y)) for y in range(0, height, size)]

    for x_block in range(width_count):
        for y_block in range(height_count):
            if blocks[y_block][x_block] == 1:
                pg.draw.rect(screen, (255,255,255), (x_block * size + 2, y_block * size + 2, size-2, size-2))
            next_blocks_stage[y_block][x_block] = check_block(blocks, (x_block, y_block))

    blocks = copy.deepcopy(next_blocks_stage)

    pg.display.set_caption("FPS: " + str(int(clock.get_fps())))
    clock.tick(FPS)
    pg.display.flip()
