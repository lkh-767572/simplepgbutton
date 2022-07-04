import pygame as pg
from sys import exit
from pygbutton import SimplePgButton

pg.init()
pg.font.init()


width, height = 500, 500
screen = pg.display.set_mode((width, height))


b_width, b_height = 200, 100
test = SimplePgButton("test2", (width/2-b_width/2, height/2-b_height/2),
                    b_width, b_height, border_rad=30, elevation=5)

count = 0
# Run until the user asks to quit
running = True
while running:

     # Did the user click the window close button?
     for event in pg.event.get():
          if event.type == pg.QUIT:
               pg.quit()
               exit()

     if test.clicked() == True:
          print(1)

     screen.fill((0, 0, 0))
     test.draw()

     pg.display.flip()
    
