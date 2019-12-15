import pygame
from modules.settings import *

def update_label(data, title, font, x, y, gameDisplay):
    label = font.render('{} {}'.format(title, data), 1, DATA_FONT_COLOR)
    gameDisplay.blit(label, (x, y))
    return y

def update_data_labels(gameDisplay, dt, gameTime, font):
    y_pos = 5
    gap = 20 
    x_pos = DISPLAY_W + 10

    y_pos = update_label(round(1000/dt,2), 'FPS', font, x_pos, y_pos + gap, gameDisplay)
    y_pos = update_label(round(gameTime/1000,2),'Game time', font, x_pos, y_pos + gap, gameDisplay)

    y_pos = update_label('Matheus','Created by:', font, x_pos, DISPLAY_H - gap, gameDisplay)
   
isNight = False

def run_game():
    pygame.init()

    gameDisplay = pygame.display.set_mode((DISPLAY_W, DISPLAY_H))

    neuralDisplay = pygame.display.set_mode((DISPLAY_W + DISPLAY_N, DISPLAY_H))
    bgNeural = pygame.image.load(BG_NEURAL) #Load background neural function
    bgNeural = pygame.transform.scale(bgNeural, (DISPLAY_N, DISPLAY_H))

    pygame.display.set_caption('Learn to fly')

    bgImg = pygame.image.load(BG_NIGHT_FILENAME if isNight else BG_DAY_FILENAME) #Load background day or night
    bgImg = pygame.transform.scale(bgImg, (DISPLAY_W, DISPLAY_H))
    
    labelFont = pygame.font.SysFont("monospace", DATA_FONT_SIZE) 

    running = True

    #Time control
    clock = pygame.time.Clock()
    dt = 0
    gameTime = 0

    while running:
        
        dt = clock.tick(FPS)
        gameTime += dt 

        gameDisplay.blit(bgImg, (0,0))  #Load background in screen

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False        
            elif event.type == pygame.KEYDOWN:
                running = False

        neuralDisplay.blit(bgNeural,(DISPLAY_W,0))

        update_data_labels(neuralDisplay, dt, gameTime, labelFont)

        pygame.display.update()



if __name__ == "__main__":
    run_game()

    print('Finish GameS')