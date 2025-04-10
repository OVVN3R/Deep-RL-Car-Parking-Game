# ---LIBRARIES---
from settings import *
import pygame as pg # https://kidscancode.org/lessons/
import screens_file

screen = pg.display.set_mode((WIDTH, HEIGHT))

# ---PROCEDURES / FUNCTIONS---

def draw_button(x, y, width, height, color, text, text_color, text_size, transparency=255):
    '''draws a button on the screen with the given parameters'''

    # Prototype -2-
    # add font
    font = pg.font.Font(pg.font.match_font(FONT_NAME), text_size)
    
    # Draws the colored box on the screen with transparency
    button_surface = pg.Surface((width, height), pg.SRCALPHA)
    
     # Adds the transparency to the color
    color_with_transparency = (*color, transparency)
    button_surface.fill(color_with_transparency)
    text_surface = font.render(text, True, text_color)
    
    # Position the text in the middle of the box
    text_rect = text_surface.get_rect(center=(x + width // 2, y + height // 2)) # Creates a text surface to go on top of the colored box. 
    
    # Keeps the transparent box under the text
    screen.blit(button_surface, (x, y))
    
    # Draws the text on top of the colored box
    screen.blit(text_surface, text_rect) 
    
    '''
    Exmple:
    draw_button(WIDTH / 2, HEIGHT*3 / 5, 400, 150,
                TRANSPARENT, "press space to confirm", WHITE, 50. 100)
    '''
    
def highlight_selection():
    '''highlights the current selection on the screen'''

    # PROTOTYPE -3-
    clear_highlight() # clearing the previous box
    if peek(screen_stack) == "title_screen" or peek(screen_stack) == "gamemodes_screen" or \
       peek(screen_stack) == "singleplayer_level_screen" or peek(screen_stack) == "ai_level_screen" or \
       peek(screen_stack) == "speedrun_level_screen":
        
        if current_index == 0: # 3 options for those screens
            draw_button(70, 105, 300, 100, GREEN, "", TRANSPARENT, 0, 100)

        elif current_index == 1:
            draw_button(70, 310, 300, 100, GREEN, "", TRANSPARENT, 0, 100)

        elif current_index == 2:
            draw_button(70, 505, 300, 100, GREEN, "", TRANSPARENT, 0, 100)
            
    elif peek(screen_stack) == "settings_screen":
        
        if current_index == 0: # only two options
            draw_button(70, 105, 300, 100, GREEN, "", TRANSPARENT, 0, 100)
            
        elif current_index == 1:
            draw_button(70, 310, 300, 100, GREEN, "", TRANSPARENT, 0, 100)
            
    elif peek(screen_stack) == "tutorial_screen":
        pass # indicates there is no selections

def clear_highlight(): 
    '''clears the highlight box from the screen by redrawing the screen'''

    if peek(screen_stack) == "title_screen":
        screens_file.title_screen()
                        
    elif peek(screen_stack) == "gamemodes_screen":
        screens_file.gamemodes_screen()
        
    elif peek(screen_stack) == "settings_screen":
        screens_file.settings_screen()
        
    elif peek(screen_stack) == "tutorial_screen":
        screens_file.tutorial_screen()
        
    elif peek(screen_stack) == "singleplayer_level_screen":
        screens_file.singleplayer_level_screen()
        
    elif peek(screen_stack) == "ai_level_screen":
        screens_file.ai_level_screen()
        
    elif peek(screen_stack) == "speedrun_level_screen":
        screens_file.speedrun_level_screen()
        
def push(stack, item):
    '''adds an item to the top of the stack'''

    stack.append(item)
    
def peek(stack):
    '''returns the top item of the stack'''

    return stack[-1]

def brute_navigation():
    '''handles the navigation of the game interface'''

    global game_state, current_index, music, sfx
    
    
    enter_pressed = False

    if game_state != "interface": # only works in the interface
        return enter_pressed

    for event in pg.event.get(): # get the events
       
        if event.type == pg.QUIT: # close the game
            pg.quit()
            exit()

        if event.type == pg.KEYDOWN: # key pressed

            if event.key == pg.K_UP: # move up
                current_index = (current_index - 1) % 3
                highlight_selection()
                nav_sound.play()
                nav_sound.set_volume(sfx)

            elif event.key == pg.K_DOWN: # move down
                current_index = (current_index + 1) % 3
                highlight_selection()
                nav_sound.play()
                nav_sound.set_volume(sfx)

            elif event.key == pg.K_RETURN: # select and advance to next screen

                # title screen group

                if peek(screen_stack) == "title_screen" and current_index == 0: 
                    # go to gamemodes screen
                    push(screen_stack, "gamemodes_screen")
                    current_index = 0
                    screens_file.gamemodes_screen()
                    highlight_selection()
                    next_sound.play()
                    next_sound.set_volume(sfx)

                elif peek(screen_stack) == "title_screen" and current_index == 1:
                    # go to settings screen
                    push(screen_stack, "settings_screen")
                    current_index = 0
                    screens_file.settings_screen()
                    highlight_selection()
                    next_sound.play()
                    next_sound.set_volume(sfx)

                elif peek(screen_stack) == "title_screen" and current_index == 2:
                    # go to tutorial screen
                    push(screen_stack, "tutorial_screen")
                    current_index = 0
                    screens_file.tutorial_screen()
                    highlight_selection()
                    next_sound.set_volume(sfx)

                # gamemodes screen group

                elif peek(screen_stack) == "gamemodes_screen" and current_index == 0:
                    # go to single player level screen
                    push(screen_stack, "singleplayer_level_screen")
                    current_index = 0
                    screens_file.singleplayer_level_screen()
                    highlight_selection()
                    next_sound.play()
                    next_sound.set_volume(sfx)

                elif peek(screen_stack) == "gamemodes_screen" and current_index == 1:
                    # go to ai level screen
                    push(screen_stack, "ai_level_screen")
                    current_index = 0
                    screens_file.ai_level_screen()
                    highlight_selection()
                    next_sound.play()
                    next_sound.set_volume(sfx)

                elif peek(screen_stack) == "gamemodes_screen" and current_index == 2:
                    # go to speedrun level screen
                    push(screen_stack, "speedrun_level_screen")
                    current_index = 0
                    screens_file.speedrun_level_screen()
                    highlight_selection()
                    next_sound.set_volume(sfx)

                # level selection screens

                elif peek(screen_stack) in ["singleplayer_level_screen", "ai_level_screen", "speedrun_level_screen"]:
                    enter_pressed = True # exits procedure and handles this in the main loop to prevent collisions with events
         
                # settings screen group
                
                elif peek(screen_stack) == "settings_screen" and current_index == 0: # music control

                    if music  == 0: # unmutes music
                        music = 0.5
                        screens_file.music_text = "MUSIC: ON"

                    elif music == 0.5: # mutes music
                        music = 0
                        screens_file.music_text = "MUSIC: OFF"

                    pg.mixer.music.set_volume(music) # sets the volume of the music
                    screens_file.settings_screen() # redraws the screen
                    highlight_selection() # highlights the selection
                

                elif peek(screen_stack) == "settings_screen" and current_index == 1: # sfx control

                    if sfx == 0: # unmutes sfx
                        sfx = 1.5
                        screens_file.sfx_text = "SFX: ON"

                    elif sfx == 1.5: # mutes sfx
                        sfx = 0
                        screens_file.sfx_text = "SFX: OFF"

                    # sets the volume of the sfx
                    nav_sound.set_volume(sfx) 
                    next_sound.set_volume(sfx)  
                    return_sound.set_volume(sfx)
                    crash_sound.set_volume(sfx)
                    win_sound.set_volume(sfx)
                    beep_channel.set_volume(sfx)
                    screens_file.settings_screen() # redraws the screen
                    highlight_selection() # highlights the selection
                    
                        
                """elif peek(screen_stack) == "settings_screen" and current_index == 2: # rendering control
                    if rendering == True:
                        rendering = False
                        screens_file.render_text = "rendering: OFF"
                        

                    elif rendering == False:
                        rendering = True
                        screens_file.render_text = "rendering: ON"

                    screens_file.settings_screen() # redraws the screen
                    highlight_selection() # highlights the selection"""
                        


            elif event.key == pg.K_ESCAPE: 
                # title screen is initial so it doesn't get removed
                if len(screen_stack) > 1:
                    return_sound.play() # plays the return sound
                    return_sound.set_volume(sfx) # sets the volume of the return sound
                    screen_stack.pop() # removes the top screen

                    current_index = 0
                    if peek(screen_stack) == "title_screen": 
                        screens_file.title_screen()

                    elif peek(screen_stack) == "gamemodes_screen":
                        screens_file.gamemodes_screen()

                    elif peek(screen_stack) == "settings_screen":
                        screens_file.settings_screen()

                    elif peek(screen_stack) == "tutorial_screen":
                        screens_file.tutorial_screen()

                    elif peek(screen_stack) == "singleplayer_level_screen":
                        screens_file.singleplayer_level_screen()

                    elif peek(screen_stack) == "ai_level_screen":
                        screens_file.ai_level_screen()

                    elif peek(screen_stack) == "speedrun_level_screen":
                        screens_file.speedrun_level_screen()
                    highlight_selection()

            return enter_pressed

    # test navigation
    #print(current_index)
    #print(screen_stack)

def blit_rotate_center(image, top_left, direction):
    '''rotates the image around its center and blits it on the screen'''

    rotated_image = pg.transform.rotate(image, direction)
    new_rect = rotated_image.get_rect(center = image.getrect(topleft = top_left).center)
    screen.blit(rotated_image, new_rect.topleft)    

def read_scores():
    '''reads the scores from the file and returns them as a dictionary'''
    
    scores = {"singleplayer": ["NULL", "NULL", "NULL"],
               "ai": ["NULL", "NULL", "NULL"], 
               "speedrun": ["NULL", "NULL", "NULL"]}
    
    file = open("test_score.txt", "r")
    lines = file.readlines()
    file.close()

    for line in lines:
        level, score = line.strip().split(",")
        level = int(level)

        if level < 3:
            scores["singleplayer"][level] = score
            scores["ai"][level] = score
            scores["speedrun"][level] = score

    return scores