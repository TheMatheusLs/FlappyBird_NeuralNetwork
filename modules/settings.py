#Settings for the other classes

#Display
DISPLAY_W = 960
DISPLAY_H = 540
DISPLAY_N = 250

#FPS
FPS = 30

#Colors and fonts
DATA_FONT_SIZE = 18
DATA_FONT_COLOR =  (255,255,255)

#Resources
BG_DAY_FILENAME = './resources/background-day.png'
BG_NIGHT_FILENAME = './resources/background-night.png'
BG_NEURAL = './resources/background-neural.png' 
PIPE_GREEN_FILENAME = './resources/pipe-green.png'
PIPE_RED_FILENAME = './resources/pipe-red.png'
BIRD_RED = (
        "./resources/redbird-upflap.png",
        "./resources/redbird-midflap.png",
        "./resources/redbird-downflap.png")
BIRD_BLUE = (
        "./resources/bluebird-upflap.png",
        "./resources/bluebird-midflap.png",
        "./resources/bluebird-downflap.png")
BIRD_YELLOW = (
        "./resources/yellowbird-upflap.png",
        "./resources/yellowbird-midflap.png",
        "./resources/yellowbird-downflap.png")

#Pipe const
PIPE_SPEED = 70/1000
PIPE_DONE = 1
PIPE_MOVING = 0
PIPE_UPPER = 1
PIPE_LOWER = 0

PIPE_W = 50
PIPE_H = 500

PIPE_ADD_GAP = 200
PIPE_MIN = 50
PIPE_MAX = 500
PIPE_START_X = DISPLAY_W
PIPE_GAP_SIZE = 160
PIPE_FIRST = 800

#Bird const
BIRD_START_SPEED = -0.32
BIRD_START_X = 200
BIRD_START_Y = 200
BIRD_ALIVE = 1
BIRD_DEAD = 0
GRAVITY = 0.001