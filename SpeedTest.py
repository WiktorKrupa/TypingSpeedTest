from time import time
from matplotlib import style
import pygame
from pygame.locals import *
import sys
import time
import random


class Game:

    def __init__(self):
        self.width=750
        self.hight=500
        self.reset=True
        self.active=False
        self.input_text=''
        self.word=''
        self.time_start=0
        self.total_time=0
        self.accuracy = '0%'
        self.wpm=0
        self.results = 'Time:0 Accuracy:0 % Wpm:0 '
        self.HEAD_C = (255,213,102)
        self.TEXT_C = (240,240,240)
        self.RESULT_C = (255,70,70)


        pygame.init()
        self.open_img = pygame.image.load('starter.jpg')
        self.open_img = pygame.transform.scale(self.open_img,(self.width,self.hight))
        self.background_img = pygame.image.load('background.jpg')
        self.background_img = pygame.transform(self.background_img,(self.width, self.hight))
        self.screen = pygame.display.set_mode((self.width,self.hight))
        pygame.display.set_caption('Type Speed Test')

