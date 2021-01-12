#!/usr/bin/env python3

# Created by: Marlon Poddalgoda
# Created on: December 2020
# This program is the "Space  Aliens" program on the PyBadge

import ugame
import stage
import time
import random

import constants


def splash_scene():
    # this function is the splash scene
    
    # get sound ready
    coin_sound = open("coin.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    sound.play(coin_sound)
    
    # image bank
    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")
    
    # stage for background and constant fps
    background = stage.Grid(image_bank_mt_background, constants.SCREEN_X, constants.SCREEN_Y)
    
    # used this program to split the image into tile: 
    #   https://ezgif.com/sprite-cutter/ezgif-5-818cdbcc3f66.png
    background.tile(2, 2, 0)  # blank white
    background.tile(3, 2, 1)
    background.tile(4, 2, 2)
    background.tile(5, 2, 3)
    background.tile(6, 2, 4)
    background.tile(7, 2, 0)  # blank white

    background.tile(2, 3, 0)  # blank white
    background.tile(3, 3, 5)
    background.tile(4, 3, 6)
    background.tile(5, 3, 7)
    background.tile(6, 3, 8)
    background.tile(7, 3, 0)  # blank white

    background.tile(2, 4, 0)  # blank white
    background.tile(3, 4, 9)
    background.tile(4, 4, 10)
    background.tile(5, 4, 11)
    background.tile(6, 4, 12)
    background.tile(7, 4, 0)  # blank white

    background.tile(2, 5, 0)  # blank white
    background.tile(3, 5, 0)
    background.tile(4, 5, 13)
    background.tile(5, 5, 14)
    background.tile(6, 5, 0)
    background.tile(7, 5, 0)  # blank white
    
    # stage for background and fps settings
    game = stage.Stage(ugame.display, constants.FPS)
    # set the layers, items show up in order
    game.layers = [background]
    # render all text and background
    game.render_block()
    
    # repeat forever, game loop
    while True:
        # wait for 2 seconds
        time.sleep(2.0)
        menu_scene()

def menu_scene():
    # this function is the menu game_scene
    
    # image bank
    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")
    
    # add text objects
    text = []
    text1 = stage.Text(width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None)
    text1.move(20, 10)
    text1.text("MT Game Studios")
    text.append(text1)
    
    text2 = stage.Text(width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None)
    text2.move(40, 110)
    text2.text("PRESS START")
    text.append(text2)
    
    # sets the background to image 0 in the image banks
    background = stage.Grid(image_bank_mt_background, constants.SCREEN_X, constants.SCREEN_Y)
    
    # stage for background and fps settings
    game = stage.Stage(ugame.display, constants.FPS)
    # set the layers, items show up in order
    game.layers = text + [background]
    # render all text and background
    game.render_block()
    
    # repeat forever, game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()
        
        # Start button selected
        if keys & ugame.K_START != 0:
            game_scene()
        
        # update game logic
        game.tick()

def game_scene():
    # this function is the main game_scene

    # for score
    score = 0

    def show_alien():
        # this function takes an alien from off screen and moves it on screen
        for alien_number in range(len(aliens)):
            if aliens[alien_number].x < 0:
                aliens[alien_number].move(random.randint(0 + constants.SPRITE_SIZE,
                                          constants.SCREEN_X - constants.SPRITE_SIZE),
                                          constants.OFF_TOP_SCREEN)
                break

    # image banks for CircuitPython
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")
    
    # buttons that keep state information
    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]
    
    # sound
    pew_sound = open("pew.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    
    boom_sound = open("boom.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    
    # background and sprites (& sprite loction)
    background = stage.Grid(image_bank_background, constants.SCREEN_X, constants.SCREEN_Y)
    
    for x_location in range(constants.SCREEN_GRID_X):
        for y_location in range(constants.SCREEN_GRID_Y):
            tile_picked = random.randint(1, 3)
            background.tile(x_location, y_location, tile_picked)
    
    ship = stage.Sprite(image_bank_sprites, 5, 75, constants.SCREEN_Y - (2 * constants.SPRITE_SIZE))
    
    # create alist of aliens
    aliens = []
    for alien_number in range(constants.TOTAL_NUMBER_OF_ALIENS):
        a_single_alien = stage.Sprite(image_bank_sprites, 9, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
        aliens.append(a_single_alien)
    
    # place 1 alien on the screen
    show_alien()
                     
    # create a list of lasers for when we shoot
    lasers = []
    for laser_number in range(constants.TOTAL_NUMBER_OF_LASERS):
        a_single_laser = stage.Sprite(image_bank_sprites, 10, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
        lasers.append(a_single_laser)

    # background with constants fps
    game = stage.Stage(ugame.display, constants.FPS)
    # set the layers of all sprites, items show up in order
    game.layers = lasers + [ship] + aliens + [background]
    # render all sprites
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()
        
        # A button to fire
        if keys & ugame.K_O != 0:
            if a_button == constants.button_state["button_up"]:
                a_button = constants.button_state["button_just_pressed"]
            elif a_button == constants.button_state["button_just_pressed"]:
                a_button = constants.button_state["button_still_pressed"]
        else:
            if a_button == constants.button_state["button_still_pressed"]:
                a_button = constants.button_state["button_released"]
            else:
                a_button = constants.button_state["button_up"]
        
        if keys & ugame.K_X != 0:
            pass
        if keys & ugame.K_START != 0:
            pass
        if keys & ugame.K_SELECT != 0:
            pass
        
        if keys & ugame.K_RIGHT != 0:
            if ship.x <= constants.SCREEN_X - constants.SPRITE_SIZE:
                ship.move(ship.x + 1, ship.y)
            else:
                ship.move(constants.SCREEN_X - constants.SPRITE_SIZE, ship.y)
        
        if keys & ugame.K_LEFT != 0:
            if ship.x >= 0:
                ship.move(ship.x - 1, ship.y)
            else:
                ship.move(0, ship.y)
        
        if keys & ugame.K_UP != 0:
            pass
        if keys & ugame.K_DOWN != 0:
            pass
        
        # update game logic
        # play sound if A button was in button_just_pressed
        if a_button == constants.button_state["button_just_pressed"]:
            # fire a laser if we have not used up all of them
            for laser_number in range(len(lasers)):
                if lasers[laser_number].x < 0:
                    lasers[laser_number].move(ship.x, ship.y)
                    sound.play(pew_sound)
                    break
        
        # each frame move the lasers, that have been fired up
        for laser_number in range(len(lasers)):
            if lasers[laser_number].x > 0:
                lasers[laser_number].move(lasers[laser_number].x,
                                          lasers[laser_number].y -
                                            constants.LASER_SPEED)
                if lasers[laser_number].y < constants.OFF_TOP_SCREEN:
                    lasers[laser_number].move(constants.OFF_SCREEN_X,
                                              constants.OFF_SCREEN_Y)
        
        # each frame move the aliens move down, that are on the screen
        for alien_number in range(len(aliens)):
            if aliens[alien_number].x > 0:
                aliens[alien_number].move(aliens[alien_number].x,
                                          aliens[alien_number].y +
                                            constants.ALIEN_SPEED)
                if aliens[alien_number].y > constants.SCREEN_Y:
                    aliens[alien_number].move(constants.OFF_SCREEN_X,
                                              constants.OFF_SCREEN_Y)
                    show_alien()
        
        for laser_number in range(len(lasers)):
            if lasers[laser_number].x > 0:
                for alien_number in range(len(aliens)):
                    if aliens[alien_number].x > 0:
                        if stage.collide(lasers[laser_number].x + 6, lasers[laser_number].y + 2,
                                         lasers[laser_number].x + 11, lasers[laser_number].y + 12,
                                         aliens[alien_number].x + 1, aliens[alien_number].y,
                                         aliens[alien_number].x + 15, aliens[alien_number].y + 15):
                            # you hit an alien
                            aliens[alien_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                            lasers[laser_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                            sound.stop()
                            sound.play(boom_sound)
                            show_alien()
                            show_alien()
                            score = score + 1
        
        # redraw sprites
        game.render_sprites(lasers + aliens + [ship])
        game.tick()

if __name__ == "__main__":
    splash_scene()
    