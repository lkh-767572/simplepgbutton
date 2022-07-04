import pygame as pg
from pygame.locals import *

#======SCREEN==================================================================
WIDTH = 100
HEIGHT = 100
screen = pg.display.set_mode((WIDTH, HEIGHT))

#======COLORS==================================================================
MAIN_COLOR = "#475F77"
SHADOW =  "#273a4d"
WHITE = "#FFFFFF"
HOVERCOLOR = "#80a8d1"

#======FONTS===================================================================
pg.font.init()
PIXELFONT10 = pg.font.SysFont("Grand9KPixel", 10)
PIXELFONT20 = pg.font.SysFont("Grand9KPixel", 20)
PIXELFONT30 = pg.font.SysFont("Grand9KPixel", 30)
PIXELFONT40 = pg.font.SysFont("Grand9KPixel", 40)
PIXELFONT50 = pg.font.SysFont("Grand9KPixel", 50)
PIXELFONT60 = pg.font.SysFont("Grand9KPixel", 60)

class SimplePgButton:

	def __init__(self, text, pos, width, height, color=MAIN_COLOR, 
              	hovercolor=HOVERCOLOR, textcolor=WHITE, shadowcolor=SHADOW, 
            	font=PIXELFONT40, elevation=6, border_rad=10):
     
		#attributes
		self.pressed = False
		self.elevation = elevation
		self.dynamic_elevation = elevation
		self.original_y_pos = pos[1]
		self.mouse_down = False
		self.click = False
		self.border_rad = border_rad

		#main rect
		self.main_rect = pg.Rect(pos, (width,height))
		self.color = color
		self.main_color = self.color
		self.hovercolor = hovercolor

		#shadow
		self.shadow_rect = pg.Rect(pos, (width, elevation))
		self.shadow_color = shadowcolor

		#text
		self.text_surf = font.render(text, True, textcolor)
		self.text_rect = self.text_surf.get_rect(center = self.main_rect.center)

	def draw(self):

		#elevation logic
		self.main_rect.y = self.original_y_pos - self.dynamic_elevation
		self.text_rect.center = self.main_rect.center

		self.shadow_rect.midtop = self.main_rect.midtop
		self.shadow_rect.height = self.main_rect.height + self.dynamic_elevation

		#draw rects
		pg.draw.rect(screen, self.shadow_color, self.shadow_rect, 
   						border_radius=self.border_rad)
		pg.draw.rect(screen, self.main_color, self.main_rect, 
   						border_radius = self.border_rad)
		screen.blit(self.text_surf, self.text_rect)
		
  		#functions
		self.hovercolor_switch()
		self.elevating()

	def clicked(self):
		
		action = False
		self.mouse_pos = pg.mouse.get_pos()
		#check if mouse over button
		if self.main_rect.collidepoint(self.mouse_pos):
			self.mouse_over_button = True
		else:
			if not self.main_rect.collidepoint(self.mouse_pos):
				self.mouse_over_button = False

		#register click and click only once
		if self.mouse_over_button:
				if not self.click:
					if pg.mouse.get_pressed()[0]:
						self.click = True
						action = True

		#set click back to false if not pressed
		if pg.mouse.get_pressed()[0] == 0:
				self.click = False

		#return true or false if function is called
		#can be called in an if statement
		#bsp: if test.clicked:
		#			print("clicked")
		return action

	def hovercolor_switch(self):
     
		#change the color if mouse hovers over it
		mouse_pos = pg.mouse.get_pos()
		if self.main_rect.collidepoint(mouse_pos):
			self.main_color = self.hovercolor
		else:
			self.main_color = self.color

	def elevating(self):
     
		#if get pressed it seems like the button gets pushed down
		#elevation can be changed while calling Button class
		mouse_pos = pg.mouse.get_pos()
		if self.main_rect.collidepoint(mouse_pos) and pg.mouse.get_pressed()[0]:
			self.dynamic_elevation = 0
		else:
			self.dynamic_elevation = self.elevation
