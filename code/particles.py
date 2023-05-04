import pygame
from pygame.locals import *
import math

import random

def circle_surf(radius, color):
    surf = pygame.Surface((radius*2, radius*2))
    pygame.draw.circle(surf, color, (radius, radius), radius)
    surf.set_colorkey((0,0,0))
    return surf


class Particle:
    def __init__(self, screen, pos, target_pos, radius, shrink_rate = 0, speed = 0):
        self.screen = screen

        self.x, self.y   = pos[0], pos[1]         
        self.tx, self.ty = target_pos[0], target_pos[1]

        self.radius = radius
        self.shrink_rate = shrink_rate
        self.y_speed = speed
        self.x_speed = speed        
        self.speed   = speed


        self.angle = math.atan2(self.ty - self.y, self.tx - self.x)
        self.dx = math.cos(self.angle) #* speed
        self.dy = math.sin(self.angle) #* speed


    def shrink(self):
        self.radius -= self.shrink_rate 

    def accelerate(self):
        self.speed += self.y_speed

    def move(self):
        self.x += self.dx * self.speed
        self.y += self.dy * self.speed

        self.rect.x = int(self.x)
        self.rect.y = int(self.y)

        if self.shrink_rate > 0:
            self.shrink()

        self.accelerate()       

    def draw(self):
        self.rect = pygame.draw.circle(self.screen, (255, 255, 255), [int(self.x), int(self.y)], int(self.radius))

    def glow(self):
        glow_radius = self.radius * 2
        
        self.screen.blit(
            circle_surf(glow_radius, (20, 20, 20)), 
            (int(self.x-glow_radius), int(self.y-glow_radius)), special_flags=BLEND_RGB_ADD)
        
        