#!/usr/bin/env python3

# Created by: Marlon Poddalgoda
# Created on: Nov 2020
# This program is the "Space  Aliens" program on the PyBadge

import ugame
import stage


def game_scene():
    # this function is the main game_scene

    # image banks for CircuitPython
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")
    
    # set the background to image 0 in the image Bank
    #   and the size (10x8 tiles of size 16x16)
    background = stage.Grid(image_bank_background, 10, 8)
    
    # a sprite that will update every 60 hz
    ship = stage.Sprite(image_bank_sprites, 5, 75, 66)

    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the layers of all sprites, items show up in order
    game.layers = [ship] + [background]
    # render all sprites
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()
        
        if keys & ugame.K_X:
            print("A")
        if keys & ugame.K_O:
            print("B")
        if keys & ugame.K_START:
            print("Start")
        if keys & ugame.K_SELECT:
            print("Select")
        if keys & ugame.K_RIGHT:
            ship.move(ship.x + 1, ship.y)
        if keys & ugame.K_LEFT:
            ship.move(ship.x - 1, ship.y)
        if keys & ugame.K_UP:
            ship.move(ship.x, ship.y - 1)
        if keys & ugame.K_DOWN:
            ship.move(ship.x, ship.y + 1)
        
        # update game logic
        
        # redraw sprites
        game.render_sprites([ship])
        game.tick()

if __name__ == "__main__":
    game_scene()
    