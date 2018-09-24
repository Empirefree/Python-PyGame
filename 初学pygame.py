import sys
import pygame
from pygame.locals import *

white = 255, 255, 255
blue = 0, 0, 200

pygame.init()
screen = pygame.display.set_mode((600, 500))   #窗口大小
myfont = pygame.font.Font(None, 60)   #创建一个文本对象
textImage = myfont.render("Hello, world", True, white)   #文本读入内存，再当图像渲染

#保证窗口一直存在
while True:
	for event in pygame.event.get():
		if event.type in (QUIT, KEYDOWN):
			sys.exit()
	screen.fill(blue)
	screen.blit(textImage, (0, 0))		#填入图像及位置
	pygame.display.update()