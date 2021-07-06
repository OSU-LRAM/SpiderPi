#!/usr/bin/env python3
# import pygame
from pygame import mixer
import time

pygame.mixer.init()
# pygame.init()
# screen = pygame.display.set_mode((640, 480), pygame.RESIZABLE)


def play_audio(vol, filename):
    """
    Play the .wav file
    :param vol: Volume audio is played at (0-1)
    :param filename: Name of audio file (55hz.wav)
    :return: None
    """
    mixer.pre_init(44100, -16, 1, 512)  # <-- fixes sound lag delay
    mixer.init()
    audio = mixer.Sound("audio/"+filename)
    audio.set_volume(vol)
    audio.play()
    time.sleep(1)
    print('start')
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    print('Quit')
                    pygame.quit()
                    raise SystemExit(0)


play_audio(1, 'test.wav')
