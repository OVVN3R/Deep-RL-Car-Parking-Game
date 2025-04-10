# ---LIBRARIES---
import pygame as pg # https://kidscancode.org/lessons/
import os

# ---INITIALISE---
pg.mixer.init()

# ---CONSTANTS---
WIDTH = 1080
HEIGHT = 720
FPS = 120
FONT_NAME = "arialblack"


# ---VARIABLES---
game_state = "interface"
current_index = 0
screen_stack = ["title_screen"]
current_level = 0
screen = pg.display.set_mode((WIDTH, HEIGHT))
sfx = 1.5
music = 0.5
rendering = True

# ---TIMER VARIABLES---
start_time = 0
elapsed_time = 0
paused = True
paused_time = 0

# ---COLOURS---
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
TRANSPARENT = (0, 0, 0)
ORANGE = (255, 127, 80)

# ---FILE ACCESS---
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")
snd_folder = os.path.join(game_folder, "snd")

# ---SOUNDS AND MUSIC---
# Interface sounds
nav_sound = pg.mixer.Sound(os.path.join(snd_folder, "nav.ogg"))
nav_sound.set_volume(sfx)

next_sound = pg.mixer.Sound(os.path.join(snd_folder, "next.ogg"))
next_sound.set_volume(sfx)

return_sound = pg.mixer.Sound(os.path.join(snd_folder, "return.ogg"))
return_sound.set_volume(sfx)

# Music
menu_music = os.path.join(snd_folder, "menu_music.ogg")
game_music = os.path.join(snd_folder, "game_music.mp3")
pg.mixer.music.set_volume(music)


# Playing sounds
win_sound = pg.mixer.Sound(os.path.join(snd_folder, "win.ogg"))
win_sound.set_volume(sfx)

beep_sound = pg.mixer.Sound(os.path.join(snd_folder, "beep.mp3"))
beep_sound.set_volume(sfx)
beep_channel = pg.mixer.Channel(1)

crash_sound = pg.mixer.Sound(os.path.join(snd_folder, "crash.ogg"))
crash_sound.set_volume(sfx)
crash_channel = pg.mixer.Channel(2)

engine_sound = pg.mixer.Sound(os.path.join(snd_folder, "engine.ogg"))
engine_channel = pg.mixer.Channel(3)




# ---IMAGES---
MENU_BG = pg.transform.scale(pg.image.load(os.path.join(img_folder, "menu_background.png")), (WIDTH, HEIGHT))
CAR_IMG = pg.transform.scale(pg.image.load(os.path.join(img_folder, "car.png")), (100, 45))
OBSTACLE_IMG = pg.transform.scale(pg.image.load(os.path.join(img_folder, "better_obstacle.png")), (100, 100))

# ---CAR PROPERTIES---
CAR_ACC = 0.2
CAR_FRICTION = 0.1
CAR_SPEED = 5
MAX_SPEED = 20
CAR_ROTATION = 3

# ---OBSTACLES PROPERTIES---
OBSTACLE_SPEED = 2

# ---TESTING VARIABLES---
beep = False

