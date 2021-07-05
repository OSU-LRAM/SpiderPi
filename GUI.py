#!/usr/bin/env python3


# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

"""Simple test for keypad on I2C RGB character LCD Shield or Pi Plate kits"""
import time
import board
import adafruit_character_lcd.character_lcd_rgb_i2c as character_lcd
import os
from play_audio.py import play_audio


# Modify this if you have a different sized Character LCD
lcd_columns = 16
lcd_rows = 2

# Initialise I2C bus.
i2c = board.I2C()  # uses board.SCL and board.SDA

# Initialise the LCD class
lcd = character_lcd.Character_LCD_RGB_I2C(i2c, lcd_columns, lcd_rows)

lcd.clear()
lcd.color = [100, 0, 0]

first_menu = ["git pull?", "Choose Signal?", "Exit?"]
second_menu = os.listdir("audio/")
print(second_menu)

def menu_control(menu_text):
    index = 0
    new_index = 0
    menu_length = len(menu_text)
    print(menu_text)
    lcd.clear()
    lcd.message = menu_text[index]
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
            lcd.clear()
            lcd.message = menu_text[index] + "\nwas chosen"
            time.sleep(0.2)
            confirm = True
            return choice
        else:
            time.sleep(0.075)
        if new_index != index:
            print(menu_text[new_index])
            index = new_index
            lcd.clear()
            lcd.message = menu_text[index]
            time.sleep(0.075)

first_choice = menu_control(first_menu)

if first_choice == 0:
    lcd.clear()
    lcd.message = 'will add later'
elif first_choice == 1:
    second_choice = menu_control(second_menu)
    play_audio(1, second_choice)
elif first_choice == 2:
    exit()


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
