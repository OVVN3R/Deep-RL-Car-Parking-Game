# ---LIBRARIES---
import pygame as pg # https://kidscancode.org/lessons/
import time
from settings import *
import screens_file
import procedures
from Car import Car
from ParkingSpot import ParkingSpot
from Obstacles import Obstacle, MovingObstacle
from agent import CarAgent
from ParkingEnv import ParkingEnv


# ---INITIALISATION---
pg.init()
pg.mixer.init()
pg.font.init()

# ---SCREEN SETUP---
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("SPOT HUNTER")
clock = pg.time.Clock()

# ---SPRITES/OBJECTS---
car = Car()
spot = ParkingSpot()
obstacle = Obstacle()
moving_obstacle = MovingObstacle() 
env = ParkingEnv(render=False)
agent = CarAgent(env)


# ---MAIN LOOP---
running = True

# To happen before the main loop
screens_file.title_screen()
procedures.highlight_selection()
pg.mixer.music.load(menu_music)
pg.mixer.music.play(loops=-1)

while running:
    #print(game_state) # test game_state
    #print("beep ", beep)
    #print("sfx: ", sfx)
    #print("Music:" ,music)
    
    for event in pg.event.get():
        
        if event.type == pg.QUIT: # close the game
            running = False
            
        if event.type == pg.KEYDOWN: 
            if game_state == "interface": # interface event handling

                if event.key == pg.K_RETURN: # handle level screen selection after exiting brute navigation
                    if (procedures.peek(screen_stack) in ["singleplayer_level_screen",
                                                          "speedrun_level_screen"]) \
                                                          and (current_index in range(3)):
                        
                        # handles game state transition
                        game_state = "playing"
                        start_time = time.time() - paused_time
                        paused_time = 0
                        paused = False
                        car.reset()
                        spot.random_position()
                        spot.place()
                        obstacle.place()
                        moving_obstacle.place()
                        pg.mixer.music.load(game_music) # load the game music
                        pg.mixer.music.play(loops=-1) # play the game music

                    if procedures.peek(screen_stack) == "ai_level_screen" and (current_index in range(3)): # handle ai level screen selection
                        game_state = "ai_playing"

                        agent.train()

            elif game_state == "playing": # playing event handling
                if event.key == pg.K_ESCAPE: # pause the game
                    paused_time = time.time() - start_time
                    paused = True
                    game_state = "paused"
                    pg.mixer.music.pause()

            elif game_state == "paused": # paused event handling
                if event.key == pg.K_RETURN: # return to the main menu
                    game_state = "interface"

                    pg.mixer.music.load(menu_music) # load the menu music
                    pg.mixer.music.play(loops=-1)

                    if procedures.peek(screen_stack) == "singleplayer_level_screen": # return to the singleplayer level screen
                        screens_file.singleplayer_level_screen()
                        procedures.highlight_selection()

                    elif procedures.peek(screen_stack) == "ai_level_screen": # return to the ai level screen
                        screens_file.ai_level_screen()
                        procedures.highlight_selection()
                    
                    elif procedures.peek(screen_stack) == "speedrun_level_screen": # return to the speedrun level screen
                        screens_file.speedrun_level_screen() 
                        procedures.highlight_selection()
                         
                elif event.key == pg.K_ESCAPE: # unpause the game
                    start_time = time.time() - paused_time
                    paused = False
                    game_state = "playing"
                    pg.mixer.music.unpause()

            elif game_state == "game_over": # game over event handling
                if event.key == pg.K_r: # restart the game
                    game_state = "playing" 
                    start_time = time.time()
                    car.reset()
                    spot.random_position()
                    spot.place()
                    obstacle.place()
                    moving_obstacle.place()
                    pg.mixer.music.load(game_music)
                    pg.mixer.music.play(loops=-1)
                
                elif event.key == pg.K_RETURN: # return to the main menu
                    game_state = "interface"
                    pg.mixer.music.load(menu_music)     
                    pg.mixer.music.play(loops=-1)
                    
                    if procedures.peek(screen_stack) == "singleplayer_level_screen": # return to the singleplayer level screen
                        screens_file.singleplayer_level_screen()
                        procedures.highlight_selection()

                    elif procedures.peek(screen_stack) == "ai_level_screen": # return to the ai level screen
                        screens_file.ai_level_screen()
                        procedures.highlight_selection()
                    
                    elif procedures.peek(screen_stack) == "speedrun_level_screen": # return to the speedrun level screen
                        screens_file.speedrun_level_screen()
                        procedures.highlight_selection()

    # Animation speed
    clock.tick(FPS)
    
    # Menu Screen -Prototype 9-
    if game_state == "interface": 
        if not pg.mixer.music.get_busy():  # check if the music is already playing
            pg.mixer.music.load(menu_music)
            pg.mixer.music.play(loops=-1)
            
        enter_pressed = procedures.brute_navigation()

        if enter_pressed: # handle level screen selection and music 
            if (procedures.peek(screen_stack) in ["singleplayer_level_screen",
                                                  "speedrun_level_screen"]) \
                                                  and (current_index in range(3)):
                
                game_state = "playing"
                start_time = time.time() - paused_time
                paused_time = 0
                paused = False
                car.reset()
                spot.place()
                obstacle.place()
                moving_obstacle.place()
                pg.mixer.music.load(game_music)
                pg.mixer.music.play(loops=-1)
            
            if procedures.peek(screen_stack) == "ai_level_screen" and (current_index in range(3)): # handle ai level screen selection
                game_state = "ai_playing"
                
                agent.train()

            if procedures.peek(screen_stack) == "settings_screen": # sfx control UNDO

                if sfx == 0: # unmutes sfx
                    sfx = 1.5
                    screens_file.sfx_text = "sfx: ON"

                elif sfx == 1.5: # mutes sfx
                    sfx = 0
                    screens_file.sfx_text = "sfx: OFF"

                # sets the volume of the sfx
                nav_sound.set_volume(sfx) 
                next_sound.set_volume(sfx)  
                return_sound.set_volume(sfx)
                crash_sound.set_volume(sfx)
                win_sound.set_volume(sfx)
                beep_channel.set_volume(sfx)
                engine_channel.set_volume(sfx)
                screens_file.settings_screen() # redraws the screen
                procedures.highlight_selection() # highlights the selection

    # Playing -Prototype 12-
    elif game_state == "playing":
        if start_time == 0:
            start_time = time.time()
    
        screens_file.playground(car, spot, obstacle, moving_obstacle)

        elapsed_time = time.time() - start_time
        
        #print("{:.2f}".format(elapsed_time)) # test time
        
        # Draw the time
        time_text = pg.font.Font(None, 36).render("{:.2f}".format(elapsed_time), True, WHITE)
        text_rect = time_text.get_rect(center=(WIDTH - 100, 50))
        screen.blit(time_text, text_rect)

        if spot.is_parked(car): # check if the car is parked
            if sfx > 0:
                win_sound.play()
                win_sound.set_volume(sfx)
                
            game_state = "game_over"
            
            # stop the engine sound when the game is not playing
            engine_sound.stop()
            beep_sound.stop()
        
    # Paused settings -Prototype 1-
    elif game_state == "paused":
        procedures.draw_button(WIDTH / 2, HEIGHT / 4, 0, 0, BLACK,
                              "PAUSED: ESC to unpause, ENTER to main menu", WHITE, 35, 0) 

    # Game Over -Prototype 2-
    elif game_state == "game_over":

        # read lines of the file and put them into a variable. 
        TEST_FILE = open("test_score.txt", "r")
        lines = TEST_FILE.readlines()
        TEST_FILE.close()
        
        best_score = None

        TEST_FILE = open("test_score.txt", "w")

        for i, line in enumerate(lines): # read the lines of the file

            # if the level is the same as the current level, update the score
            level, score = line.strip().split(',')

            if int(level) == current_level: # check if the level is the same as the current level
                
                if score == "NULL" or elapsed_time < float(score): # check if the score is NULL or the elapsed time is less than the score

                    TEST_FILE.write("{},{:.2f}\n".format(current_level, elapsed_time))
                    best_score = elapsed_time  

                else:  # keep the score the same

                    TEST_FILE.write(line)  
                    if score != "NULL":
                        best_score = float(score)
            else: # keep the score the same
                TEST_FILE.write(line)
        
        if best_score is not None: # check if the best score is not None
            procedures.draw_button(WIDTH / 2, HEIGHT / 4, 0, 0, BLACK,
                                f"Best Score: {best_score:.2f}s", WHITE, 35, 0)
        else: # check if the best score is None
            procedures.draw_button(WIDTH / 2, HEIGHT / 4, 0, 0, BLACK,
                                f"Best Score: {score}s", WHITE, 35, 0)

        procedures.draw_button(WIDTH / 2, HEIGHT / 3, 0, 0, BLACK,
                            "Score: {:.2f}s".format(elapsed_time), WHITE, 35, 0)
        
        TEST_FILE.close()
        
        procedures.draw_button(WIDTH / 2, HEIGHT*3 / 4, 0, 0, BLACK,
                              "R to restart || ENTER to return", WHITE, 35, 0)
    

    elif game_state == "ai_playing":
        pass 


    # Update the display
    pg.display.flip()

# ---QUIT---
pg.quit()