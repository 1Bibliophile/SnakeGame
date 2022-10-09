import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox

class cube(object):
    rows = 200
    w = 500

    def __init__(self, start, dirnx=1, dirny=0, color=(255,0,0)):
        self.pos = start
        self.dirnx = 1
        self.dirny = 0
        self.color = color
        

    def move(self, dirnx,  dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos(self.pos[0] + self.dirnx, self.pos[1] + self.dirny)

    def draw(self, surface, eyes=False):
        distance = self.w // self.rows

        i = self.pos[0]
        j = self.pos[1]

        pygame.draw.rect(surface, self.color, (i * distance + 1, j * distance + 1, distance - 2, distance - 2))

class snake(object):
    body = []
    turns = {}
    
    def __init__(self, color, pos):
        self.color = color
        self.head = cube(pos)
        self.body.append(self.head)
        self.dirnx = 0
        self.dirny = 1

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            keys = pygame.key.get_pressed()

            for keys in keys():
                if keys[pygame.K_LEFT]:
                    self.dirnx = -1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_RIGHT]:
                    self.dirnx = 1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_UP]:
                    self.dirnx = 0
                    self.dirny = -1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_DOWN]:
                    self.dirnx = 0
                    self.dirny = 1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

        for i, c in enumerate(self.body):
            p = c.pos[:]
            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0], turn[1])

                if i == len(self.body) - 1:
                    self.turns.pop(p)

            else:
                if c.dirnx == -1 and c.pos[0] <= 0: c.pos = (c.rows - 1, c.pos[-1])
                elif c.dirnx == 1 and c.pos[0] >= c.rows - 1: c.pos = (0, c.pos[1])
                elif c.dirny == 1 and c.pos[1] >= c.rows - 1: c.pos = (c.pos[0], 0)
                elif c.dirny == -1 and c.pos[1] <= 0: c.pos = (c.pos[0], c.rows - 1)
                else: c.move(c.dirnx, c.dirny)


    def reset(self, pos):
        pass

    def addCube(self):
        pass

    def draw(self, surface):
        for i, c in enumerate(self.body):
            if i == 0:
                c.draw(surface, True)
            else: 
                c.draw(surface)

def drawGrid(w, rows, surface):
    sizeBtw = w // rows

    x = 0
    y = 0
    for l in range(rows):
        x = x + sizeBtw
        y = y + sizeBtw

        pygame.draw.line(surface, (255,255,255), (x,0), (x,w))
        pygame.draw.line(surface, (255,255,255), (0,y), (w,y))

def redrawWindow(surface):
    global rows, width, s
    surface.fill((0,0,0))
    drawGrid(width, rows, surface)
    s.draw(surface)
    
    pygame.display.update()
    pass

def randomSnack(rows, items):
    pass

def messageBox(subject, content):
    pass

def main():
    global width, rows, s 
    width = 500
    #height = 500
    rows = 20

    win = pygame.display.set_mode((width, width))
    s = snake((255, 0, 0), (10, 10))

    flag = True

    clock = pygame.time.Clock

    while flag:
        pygame.time.delay(50)

        # Makes sure the game doesn't more than 10 frames/second
        clock.tick(10)

        redrawWindow(win)
         
    pass

# rows =
# w =
# h =

#cube.rows = rows
#cube.w = w

main()
