import pygame, sys, random
from pygame.locals import *
from particles import *

main_clock = pygame.time.Clock()
pygame.init()

screen = pygame.display.set_mode((500, 500), 0, 32)
player_pos = pygame.math.Vector2(500/2, 500/2)

particles = []

while True:
    screen.fill('black')

    player = pygame.draw.rect(screen, 'white', pygame.Rect(player_pos[0], player_pos[1], 20, 20))

    for particle in particles:

        particle.draw()
        particle.move()        
        particle.glow()
        
        if particle.radius <= 0:
            particles.remove(particle)

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()

        if event.type == MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()            
            particles.append(Particle(screen      = screen, 
                                      pos         = (player.centerx, player.centery),
                                      target_pos  = (mx, my),
                                      radius      = 10, 
                                      shrink_rate = 0,
                                      speed       = 0.5)) 


    pygame.display.flip()
    main_clock.tick(60)

# import math

# import pygame as pg
# import pygame.freetype as ft
# import sys
# from settings import *


# class Game:
#     def __init__(self):
#         pg.init()

#         self.screen     = pg.display.set_mode((WIDTH, HEIGHT))
#         self.clock      = pg.time.Clock()
#         self.player_pos = pg.math.Vector2(HALF_WIDTH, HALF_HEIGHT)
#         self.mouse_pos  = pg.math.Vector2()
#         self.click_pos  = pg.math.Vector2()
#         self.click_time   = pg.time.get_ticks()
#         self.current_time = pg.time.get_ticks()
#         self.end_pos      = pg.math.Vector2()
#         self.bullets      = []
        
#         self.angle = 0
#         self.dx = 0
#         self.dy = 0

#         self.count = 0
        
#         pg.mouse.set_visible(False)
        

#         self.game_font = ft.SysFont('Comic Sans', 10)

#     def draw_red_line(self, s, e, p):
#         x = s[0] * (1-p) + e[0] * p
#         y = s[1] * (1-p) + e[1] * p
#         pg.draw.line(self.screen, 'red', s, (round(x), round(y)))

#     def check_events(self):
#         for event in pg.event.get():
#             if event.type == pg.QUIT or event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
#                 pg.quit()
#                 sys.exit()

#             if event.type == pg.MOUSEBUTTONDOWN:
#                 x, y  = pg.mouse.get_pos()
#                 self.bullet = pg.draw.circle(self.screen, 'red', self.player_pos, 2, 2)               
#                 self.click_time = pg.time.get_ticks()

#                 self.bullets.append(Bullet(self.screen, self.player.centerx, self.player.centery, x, y))


    
#     def draw(self):
#         self.screen.fill('black')
#         self.player = pg.draw.rect(self.screen, 'white', pg.Rect(HALF_WIDTH, HALF_HEIGHT, 20, 20))

#         pg.draw.circle(self.screen, 'green', self.mouse_pos, 2, 2)

#         for b in self.bullets:
#             b.draw()      



#     def update(self):
#         self.delta_time   = self.clock.tick(FPS)
#         self.mouse_pos    = pg.mouse.get_pos()
#         self.current_time = pg.time.get_ticks()
#         for b in self.bullets:
#             b.move()      
#         pg.display.set_caption(f'FPS={self.clock.get_fps()}')
#         pg.display.flip()
        
        
        
        
        
        


#     def run(self):
#         while True:
#             self.check_events()
#             self.draw()
#             self.update()
            



# class Bullet():
#     def __init__(self, screen, x, y, tx, ty):
        
#         self.rect = pg.Rect(x, y, 2, 2)
#         self.screen = screen
#         self.x = x
#         self.y = y

#         self.angle = math.atan2(ty - y, tx - x)
#         self.dx = math.cos(self.angle) * 20
#         self.dy = math.sin(self.angle) * 20

#     def draw(self):
#         pg.draw.rect(self.screen, 'red', self.rect)


#     def move(self):
        
#         self.x += self.dx
#         self.y += self.dy

#         self.rect.x = int(self.x)
#         self.rect.y = int(self.y)




# if __name__ == '__main__':
# 	game = Game()
# 	game.run()    