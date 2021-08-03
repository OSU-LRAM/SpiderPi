#!/usr/bin/env python3


# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

"""Simple test for keypad on I2C RGB character LCD Shield or Pi Plate kits"""
import time
import board
import adafruit_character_lcd.character_lcd_rgb_i2c as character_lcd
import os
import git

import pygame
from pygame import mixer
mixer.init()

print('starting gui')
# Modify this if you have a different sized Character LCD
lcd_columns = 16
lcd_rows = 2

# Initialise I2C bus.
i2c = board.I2C()  # uses board.SCL and board.SDA

# Initialise the LCD class
lcd = character_lcd.Character_LCD_RGB_I2C(i2c, lcd_columns, lcd_rows)

lcd.clear()
lcd.color = [100, 0, 0]

first_menu = [" update?", " play?", " exit?"]


def menu_control(header, menu_text):
    index = 0
    new_index = 0
    menu_length = len(menu_text)
    lcd.clear()
    print(header)
    lcd.message = header + " \n " + menu_text[index]
    confirm = False
    while not confirm:
        if lcd.left_button:
            new_index = (new_index - 1) % menu_length
        #elif lcd.up_button:
        #    new_index = (new_index - 1) % menu_length
        #elif lcd.down_button:
        #    new_index = (new_index + 1) % menu_length
        elif lcd.right_button:
            new_index = (new_index + 1) % menu_length
        elif lcd.select_button:
            choice = index
            #lcd.clear()
            #lcd.message = menu_text[index] + "\nwas chosen"
            #time.sleep(0.2)
            confirm = True
            return choice
        else:
            time.sleep(0.075)
        if new_index != index:
            index = new_index
            lcd.clear()
            print(header)
            lcd.message = header + " \n " + menu_text[index]
            time.sleep(0.075)


def play_audio(vol, left_filename, right_filename):
    """
    Play the .wav file
    :param vol: Volume audio is played at (0-1)
    :param filename: Name of audio file (55hz.wav)
    :return: None
    """


    mixer.pre_init(44100, -16, 2, 512)  # <-- fixes sound lag delay
    mixer.init()
    pygame.mixer.set_num_channels(2)
    print("audio/" + left_filename)
    left_audio = mixer.Sound("audio/" + left_filename)
    right_audio = mixer.Sound("audio/" + right_filename)
    left_channel = mixer.Channel(0)
    right_channel = mixer.Channel(1)
    left_channel.play(left_audio)
    right_channel.play(right_audio)
    left_audio.set_volume(vol)
    right_audio.set_volume(vol)
    time.sleep(max(left_audio.get_length(), right_audio.get_length()))


def git_pull():
    repo = git.Repo("/home/pi/SpiderPi/")
    repo.remotes.origin.pull()

while True:
    first_choice = menu_control(" Main Menu: ", first_menu)
    if first_choice == 0:
        lcd.clear()
        lcd.message = ' updating...'
        git_pull()
        lcd.message = ' update complete'
        lcd.clear()

    elif first_choice == 1:
        second_menu = os.listdir("audio/")
        lcd.clear()
        left_choice = menu_control(" left signal", second_menu)
        lcd.clear()
        right_choice = menu_control(" right signal", second_menu)
        lcd.clear()
        lcd.message = ' playing...'
        print("audio choices", second_menu[left_choice], second_menu[right_choice])
        print(type(second_menu[left_choice]))
        play_audio(1, second_menu[left_choice], second_menu[right_choice])
        lcd.clear()
        lcd.message = ' finished'
        time.sleep(0.25)


    elif first_choice == 2:
        lcd.clear()
        lcd.color = [0,0,0]
        exit()




# pygame.init()
# screen = pygame.display.set_mode((640, 480), pygame.RESIZABLE)




    # while True:
    #     for event in pygame.event.get():
    #         if event.type == pygame.KEYDOWN:
    #             if event.key == pygame.K_ESCAPE:
    #                 print('Quit')
    #                 pygame.quit()
    #                 raise SystemExit(0)





'''
lcd.clear()
# Set LCD color to red
lcd.color = [100, 0, 0]
time.sleep(1)
# Print two line message
lcd.message = "Hello\nCircuitPython"
# Wait 5s
time.sleep(5)
# Set LCD color to blue
lcd.color = [0, 100, 0]
time.sleep(1)
# Set LCD color to green
lcd.color = [0, 0, 100]
time.sleep(1)
# Set LCD color to purple
lcd.color = [50, 0, 50]
time.sleep(1)
lcd.clear()
# Print two line message right to left
lcd.text_direction = lcd.RIGHT_TO_LEFT
lcd.message = "Hello\nCircuitPython"
# Wait 5s
time.sleep(5)
# Return text direction to left to right
lcd.text_direction = lcd.LEFT_TO_RIGHT
# Display cursor
lcd.clear()
lcd.cursor = True
lcd.message = "Cursor! "
# Wait 5s
time.sleep(5)
# Display blinking cursor
lcd.clear()
lcd.blink = True
lcd.message = "Blinky Cursor!"
# Wait 5s
time.sleep(5)
lcd.blink = False
lcd.clear()
# Create message to scroll
scroll_msg = "<-- Scroll"
lcd.message = scroll_msg
# Scroll to the left
for i in range(len(scroll_msg)):
    time.sleep(0.5)
    lcd.move_left()
lcd.clear()
time.sleep(1)
lcd.message = "Going to sleep\nCya later!"
time.sleep(5)
# Turn off LCD backlights and clear text
lcd.color = [0, 0, 0]
lcd.clear()
'''
