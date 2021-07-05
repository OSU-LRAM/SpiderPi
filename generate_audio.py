#!/usr/bin/env python3
import numpy as np
import wave, struct, math, random


import matplotlib.pyplot as plt

import scipy.io
import scipy.io.wavfile


'''
Code is based on https://stackoverflow.com/questions/33879523/python-how-can-i-generate-a-wav-file-with-beeps
Also code was recycled from past work playing audio.
'''


class GenerateAudio:

    def __init__(self, sample_rate=44100, frequency=55):
        self.sample_rate = sample_rate
        self.frequency = frequency
        self.audio = []
        self.filename = 'test.wav'

    def add_silence(self, pause_time=500):
        """
        Adds silence to the self.audio variable
        :param pause_time: time taken for pause (ms)
        :return: None
        """
        len_silence = pause_time/1000*self.sample_rate
        for i in range(int(len_silence)):
            self.audio.append(0)

    def add_impulse(self, impulse_time=100, volume=1):
        """
        Adds an impulse at self.frequency to the self.audio variable
        :param impulse_time: time taken for impulse (ms)
        :param volume: volume of impulse (0-1)
        :return: None
        """
        len_impulse = impulse_time/1000*self.sample_rate
        for i in range(int(len_impulse)):
            temp_audio_val = np.sin(i / self.sample_rate * 2 * np.pi * self.frequency)
            self.audio.append(temp_audio_val)

    def add_both(self, pause_time=500, impulse_time=100, volume=1):
        """
        Generates a pause, then an impulse aat a set volume
        :param pause_time: time taken for pause (ms)
        :param impulse_time: time taken for impulse (ms)
        :param volume: volume of impulse (0-1)
        :return: None
        """
        self.add_silence(pause_time)
        self.add_impulse(impulse_time, volume)

    def save_wav_audio(self):
        """
        Saves a .wav file based on the self.audio variable and wipes self.audio.
        Function to be called after impulses and pauses have been added.
        :return: None
        """
        audio_obj = wave.open("audio/"+self.filename, 'w')
        audio_obj.setparams((1, 2, 44100, len(self.audio), 'NONE', 'not compressed'))
        for sample in self.audio:
            audio_obj.writeframes(struct.pack('h', int(sample * 32767.0)))
        audio_obj.close()
        self.audio = []

    def plot_wav_audio(self):
        """
        Plots .wav file based on self.filename.
        set self.filename to desired file beforehand.
        :return: None
        """
        sample_rate, audio_buffer = scipy.io.wavfile.read("audio/"+self.filename)
        duration = len(audio_buffer) / sample_rate
        times = np.arange(0, duration, 1 / sample_rate)  # time vector
        plt.plot(times, audio_buffer)
        plt.xlabel('Time [s]')
        plt.ylabel('Amplitude')
        plt.title(self.filename)
        plt.show()
        return


# Sample rate and impulse frequency
ga = GenerateAudio(44100, 550)

ga.filename = "test3.wav"
# pause time, impulse time, volume of impulse
ga.add_both(500, 100)
ga.add_both(500, 100)
ga.add_both(500, 100)
ga.save_wav_audio()
ga.plot_wav_audio()




