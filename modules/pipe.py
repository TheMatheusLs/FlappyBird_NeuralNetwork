import pygame
import random 
from modules.settings import *

class Pipe():

    def __init__(self, gameDisplay, x, y, pipeType, isGreen = True):
        self.gameDisplay = gameDisplay
        self.state = PIPE_MOVING
        self.pipeType = pipeType
        
        self.img = pygame.image.load(PIPE_GREEN_FILENAME if isGreen else PIPE_RED_FILENAME) #Load background day or night

        self.rect = self.img.get_rect()
        if pipeType == PIPE_UPPER:
            y = y - self.rect.height

        self.set_position(x, y)

    def set_position(self, x, y):
        self.rect.left = x
        self.rect.top = y
    
    def move_position(self, dx, dy):
        self.rect.centerx += dx
        self.rect.centery += dy 
    
    def draw(self):
        self.gameDisplay.blit(self.img, self.rect)

    def check_status(self):
        if self.rect.right < 0:
            self.state = PIPE_DONE

    def update(self, dt):
        if self.state == PIPE_MOVING:
            self.move_position(-(PIPE_SPEED * dt), 0)
            self.draw()
            self.check_status()

class PipeCollection():

    def __init__(self, gameDisplay):
        self.gameDisplay = gameDisplay
        self.pipes = []

    def add_new_pipe_pair(self, x):
        top_y = random.randint(PIPE_MIN, PIPE_MAX - PIPE_GAP_SIZE)
        bottom_y = top_y + PIPE_GAP_SIZE

        color = self.random_color_pipe()

        p1 = Pipe(self.gameDisplay, x, top_y, PIPE_UPPER, color)
        p2 = Pipe(self.gameDisplay, x, bottom_y, PIPE_LOWER, color)

        self.pipes.append(p1)
        self.pipes.append(p2)

    def create_new_set(self):
        self.pipes = []
        placed = PIPE_FIRST

        while placed < DISPLAY_W:
            self.add_new_pipe_pair(placed)
            placed += PIPE_ADD_GAP
    
    def random_color_pipe(self, percent_green=0.8):
        if random.random() < percent_green:
            return True
        else:
            return False

    def update(self, dt):
        rightmost = 0

        for p in self.pipes:
            p.update(dt)
            if p.pipeType == PIPE_UPPER:
                if p.rect.left > rightmost:
                    rightmost = p.rect.left
        
        if rightmost < (DISPLAY_W - PIPE_ADD_GAP):
            self.add_new_pipe_pair(DISPLAY_W)
        
        self.pipes = [p for p in self.pipes if p.state == PIPE_MOVING]