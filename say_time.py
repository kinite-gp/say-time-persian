from time import strftime, sleep
import pygame
from os import path


sourceFileDir = path.dirname(path.abspath(__file__))
pygame.init()


def say(path):
    t = pygame.mixer.Sound(path).get_length()-0.8
    pygame.mixer.music.load(path)
    pygame.mixer.music.play()
    sleep(t)
    

def time():
    current_time = strftime("%H:%M")
    current_time = current_time.replace(":", " : ").split(" ")
    t1 = pygame.mixer.Sound(path.join(sourceFileDir, f"wave/{current_time[0]}.wav")).get_length()-0.95
    t2 = pygame.mixer.Sound(path.join(sourceFileDir, f"wave/and.wav")).get_length()-0.95
    t3 = pygame.mixer.Sound(path.join(sourceFileDir, f"wave/{current_time[-1]}.wav")).get_length()-0.95
    pygame.mixer.music.load(path.join(sourceFileDir, f"wave/{current_time[0]}.wav"))
    pygame.mixer.music.play()
    sleep(t1)
    pygame.mixer.music.load(path.join(sourceFileDir, f"wave/and.wav"))
    pygame.mixer.music.play()
    sleep(t2)
    pygame.mixer.music.load(path.join(sourceFileDir, f"wave/{current_time[-1]}.wav"))
    pygame.mixer.music.play()
    sleep(t3)



    
    
# example

time()

