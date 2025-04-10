# ---LIBRARIES---
from settings import *
from procedures import draw_button, read_scores

music_text = "MUSIC: ON"
sfx_text = "SFX: ON"
render_text = "RENDER: ON"


# ---SCREENS---
def title_screen():
    '''Title screen of the game'''

    screen.blit(MENU_BG, (0, 0)) # Apply background
    
    draw_button(400, 300, 600, 100, ORANGE,
                "MADE WITH LOVE", BLACK, 30, 160) # Title of screen
    
    draw_button(70, 105, 300, 100, BLACK,
                "HUNTIN' TIME", WHITE, 30, 155) # Start button
    
    draw_button(70, 310, 300, 100, BLACK,
                "SETTINGS", WHITE, 30, 155) # settings button
    
    draw_button(70, 505, 300, 100, BLACK,
                "TUTORIAL", WHITE, 30, 155) # tutorial button
    

def gamemodes_screen():
    '''Game modes screen'''
    screen.blit(MENU_BG, (0, 0)) # Apply background
    
    draw_button(WIDTH / 7, 20, 900, 100, ORANGE,
                "GAMEMODES", BLACK, 70) # Title of screen
    
    draw_button(70, 105, 300, 100, RED,
                "SINGLE PLAYER", WHITE, 30, 155) # singple player button
    
    draw_button(70, 310, 300, 100, RED,
                "AI", WHITE, 30, 155) # ai button
    
    draw_button(70, 505, 300, 100, RED,
                "SPEEDRUN", WHITE, 30, 155) # speedrun button

def settings_screen():
    '''Settings screen'''
    
    screen.blit(MENU_BG, (0, 0)) # Apply background
    
    draw_button(WIDTH / 7, 20, 900, 100, ORANGE,
                "SETTINGS", BLACK, 70) # Title of screen
    
    draw_button(70, 105, 300, 100, RED,
                music_text, WHITE, 30, 155)
    
    draw_button(70, 310, 300, 100, RED,
                sfx_text, WHITE, 30, 155)
    
    
                
def tutorial_screen(): 
    '''Tutorial screen''' 

    screen.blit(MENU_BG, (0, 0)) # Apply background
    
    draw_button(100, 20, 900, 100, ORANGE,
                "TUTORIAL", BLACK, 70) # Title of screen
    
    draw_button(100, 115, 900, 200, GREEN,
                "Move the car with WASD", BLACK, 40, 200)

    draw_button(100, 315, 900, 200, GREEN,
                "SPACE to use powerup", BLACK, 40, 200)

    draw_button(100, 515, 900, 200, GREEN,
                "Avoid obstacles and park your car", BLACK, 40, 200)

def singleplayer_level_screen():
    '''Single player level screen'''
    
    scores = read_scores()

    screen.blit(MENU_BG, (0, 0)) # Apply background
    
    draw_button(WIDTH / 7, 20, 900, 100, ORANGE,
                "SINGLE PLAYER", BLACK, 70) # Title of screen
    
    draw_button(70, 105, 300, 100, BLACK,
                f"1 Best: {scores['singleplayer'][0]}", WHITE, 30) 
    
    draw_button(70, 310, 300, 100, BLACK,
                f"2 Best: {scores['singleplayer'][1]}", WHITE, 30) 
    
    draw_button(70, 505, 300, 100, BLACK,
                f"3 Best: {scores['singleplayer'][2]}", WHITE, 30) 
    

def ai_level_screen():
    '''AI level screen'''

    scores = read_scores()

    screen.blit(MENU_BG, (0, 0)) # Apply background
    
    draw_button(WIDTH / 7, 20, 900, 100, ORANGE,
                "AI", BLACK, 70) # Title of screen
    
    draw_button(70, 105, 300, 100, BLACK,
                f"1 Best: {scores['ai'][0]}", WHITE, 30) 
    
    draw_button(70, 310, 300, 100, BLACK,
                f"2 Best: {scores['ai'][1]}", WHITE, 30) 
    
    draw_button(70, 505, 300, 100, BLACK,
                f"3 Best: {scores['ai'][2]}", WHITE, 30) 

def speedrun_level_screen():
    '''Speedrun level screen'''

    scores = read_scores()

    screen.blit(MENU_BG, (0, 0)) # Apply background
    
    draw_button(WIDTH / 7, 20, 900, 100, ORANGE,
                "SPEEDRUN", BLACK, 70) # Title of screen
    
    draw_button(70, 105, 300, 100, BLACK,
                f"1 Best: {scores['speedrun'][0]}", WHITE, 30)
    
    draw_button(70, 310, 300, 100, BLACK,
                f"2 Best: {scores['speedrun'][1]}", WHITE, 30)
    
    draw_button(70, 505, 300, 100, BLACK,
                f"3 Best: {scores['speedrun'][2]}", WHITE, 30) 
       
    
def level_one():
    '''under development'''
    screen.fill(BLACK)

def level_two():
    '''under development'''
    screen.fill(BLACK)

def level_three():
    '''under development'''
    screen.fill(BLACK)
    
def playground(car, spot, obstacle, moving_obstacle):
    '''to test the game'''

    screen.fill(BLACK)
    
    # place objects
    
    spot.place() 
    obstacle.place() 
    moving_obstacle.place() 
    
    # add penalties
    obstacle.penalty(car)
    moving_obstacle.penalty(car)
    
    car.update() # update the procedures for the car
    
