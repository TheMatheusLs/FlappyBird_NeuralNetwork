import pygame
import random
from modules.settings import *

class Bird():

    def __init__(self, gameDisplay, birdColor=BIRD_RED, isPlayer = False):
        self.gameDisplay = gameDisplay
        self.state = BIRD_ALIVE

        self.images = [pygame.image.load(birdColor[0]),
                       pygame.image.load(birdColor[1]),
                       pygame.image.load(birdColor[2])]

        self.img = self.images[1]
        self.current_img = 0
        self.rect = self.img.get_rect()
        self.speed = 0
        self.fitness = 0
        self.timeLived = 0
        self.isPlayer = isPlayer
        self.distance = 0
        self.leapPipes = 0

        self.set_position(random.randint(100,250), BIRD_START_Y)

    def reset(self):
        self.state = BIRD_ALIVE
        self.speed = 0
        self.fitness = 0
        self.timeLived = 0
        self.distance = 0
        self.leapPipes = 0

        self.set_position(random.randint(100,250), BIRD_START_Y)

    def set_position(self, x, y):
        self.rect.centerx = x
        self.rect.centery = y

    def move(self, dt):
        distance = 0
        newSpeed = 0

        distance = (self.speed * dt) + (0.5 * GRAVITY * dt * dt)
        newSpeed = self.speed + (GRAVITY * dt)

        self.rect.centery += distance
        self.speed = newSpeed

        if self.rect.top < 0:
            self.rect.top = 0
            self.speed = 0

    def jump(self):
        self.speed = BIRD_START_SPEED

    def draw(self):
        self.gameDisplay.blit(self.img, self.rect)

    def check_status(self, pipes):
        if self.rect.bottom > DISPLAY_H:
            self.state = BIRD_DEAD
        else:
            self.check_hits(pipes)

    def check_hits(self, pipes):
        for p in pipes:
            if p.rect.colliderect(self.rect):
                self.state = BIRD_DEAD
                #Include how to calculate fitness here
                break

    def update(self, dt, pipes):
        if self.state == BIRD_ALIVE:
            self.current_img = (self.current_img + 1) % 3
            self.img = self.images[self.current_img]
            self.timeLived += dt
            self.distance += 0.3

            #Include

            self.move(dt)

            self.draw()
            self.check_status(pipes)
