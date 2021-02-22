import pygame
from pygame import * 
import sys
import random
from pygame.locals import *

pygame.init()

display_width = 600  
display_height = 500
screen = display.set_mode((display_width, display_height))

white = ((255,255,255))
red = ((255,0,0))

player_x = 280
player_y = 425
#move_Player#
player_left_x = 0
player_right_x = 0
##DEFAUT SKIN##
player_s = "turtle1"

apple = image.load("images/apple.png")
btnr = image.load("Buttons/left.png")
btnr_active = image.load("Buttons/left_active.png")
btnl = image.load("Buttons/right.png")
btnl_active = image.load("Buttons/right_active.png")
bg = image.load('background/eat the apples bg.png')
player_right1 = image.load('turtle right/turtle1.png')
player_right2 = image.load('turtle right/turtle2.png')
player_right3 = image.load('turtle right/turtle3.png')
player_right4 = image.load('turtle right/turtle4.png')
player_left1 = image.load('turtle left/turtle11.png')
player_left2 = image.load('turtle left/turtle22.png')
player_left3 = image.load('turtle left/turtle33.png')
player_left4 = image.load('turtle left/turtle44.png')
block = image.load('ground block/ground_block.png')
ground_lock = image.load('ground block/ground_lock.png')
red_apple = image.load('apples/apple.png')
#########DEFAUT___SKIN######################
skin = player_right1
############################################
green_apple = image.load('apples/apple3.png')
purple_apple = image.load('apples/apple2.png')
live = image.load('live/live.png')
pause = image.load('messages/pause.png')
fall = image.load('messages/fall.png')
rebuild_soild = image.load('messages/rebuild.png')
not_enough = image.load('messages/not_enough.png')
no_broken_solid = image.load('messages/no_broken_solid.png')
lives_increased = image.load('messages/lives_increased.png')
gameoverpic = image.load('background/gameoverpic.png')
intropic = image.load('intro/intropic.png')
play_button_active = image.load('intro/play_button_active.png')
play_button_inactive = image.load('intro/play_button_inactive.png')
how_to_play_button_active = image.load('intro/how_to_play_button_active.png')
how_to_play_button_inactive = image.load('intro/how_to_play_button_inactive.png')
quit_button_active = image.load('intro/quit_button_active.png')
quit_button_inactive = image.load('intro/quit_button_inactive.png')
how_to_pic = image.load('intro/how to play.png')
exit_how_to = image.load('intro/exit how to.png')
###################
skin_changer = 0
###################
#1-5#    
block_x1 = 0
block_y1 = 440
block_x2 = 40
block_y2 = 440
block_x3 = 80
block_y3 = 440
block_x4 = 120
block_y4 = 440
block_x5 = 160
block_y5 = 440
##############
#6-10#
block_x6 = 200
block_y6 = 440
block_x7 = 240
block_y7 = 440
block_x8 = 280
block_y8 = 440
block_x9 = 320
block_y9 = 440
block_x10 = 360
block_y10 = 440
###############
#11-15#
block_x11 = 400
block_y11 = 440
block_x12 = 440
block_y12 = 440
block_x13 = 480
block_y13 = 440
block_x14 = 520
block_y14 = 440
block_x15 = 560
block_y15 = 440
##################
#block_State's
block1s = "placed"
block2s = "placed"
block3s = "placed"
block4s = "placed"
block5s = "placed"
block6s = "placed"
block7s = "placed"
block8s = "placed"
block9s = "placed"
block10s = "placed"
block11s = "placed"
block12s = "placed"
block13s = "placed"
block14s = "placed"
block15s = "placed"
##################
broken_block = False
##################
#block_images#
block1pic = block
block2pic = block
block3pic = block
block4pic = block
block5pic = block
block6pic = block
block7pic = block
block8pic = block
block9pic = block
block10pic = block
block11pic = block
block12pic = block
block13pic = block
block14pic = block
block15pic = block
#red_apple_score#
red_apple_score = 0

green_apple_x = random.randrange(20,570)
green_apple_y = -30
purple_apple_x = random.randrange(20,570)
purple_apple_y = -30

# class redapple(object):	
# 	apples_x = []
# 	apples_y = []
# 	apple_x_move = random.choice([10,40,80,120,160,200,240,280,320,360,400,440,480,520,560])
# 	apple_y_move = -10
# 	apple = image.load("images/apple.png")
# 	global red_apple
# 	def __init__(self):
# 		apples_x = []
# 		apples_y = []

# 	def handler(self,x,y):
# 		global red_apple
# 		while True:
# 			apples_counter = 0
# 			for applex in self.apples_x: 
# 				if not applex:
# 					apples_counter = apples_counter + 1
# 					if self.apples_y[apples_counter] > 520:
# 						self.apples_y.remove(apples_counter)
# 						self.apples_x.remove(apples_counter)
# 					else:
# 						self.apples_y[apples_counter] = self.apples_y[apples_counter] + 10
# 						appley = self.apples_y[apples_counter]
# 						screen.blit(self.apple,(applex,appley))

# 	def run(self):
# 		global apples_x,apples_y
# 		apple_y_move = -10
# 		while True:
# 			apple_x_move = random.choice([10,40,80,120,160,200,240,280,320,360,400,440,480,520,560])
# 			choice = random.choice(["no","no","yes","no","no"])
# 			if(choice == "yes"):
# 				x = apple_x_move
# 				y = apple_y_move
# 				thread = threading.Thread(target=self.handler, args=(x,y))
# 				thread.daemon = True
# 				thread.start()
# 				self.apples_x.append(x)
# 				self.apples_y.append(y)
		

# def re_define():
# 	#player_positions#
# 	player_x = 280
# 	player_y = 425
# 	#move_Player#
# 	player_left_x = 0
# 	player_right_x = 0
# 	##DEFAUT SKIN##
# 	player_s = "turtle1"

# 	apple = image.load("images/apple.png")
# 	btnr = image.load("Buttons/left.png")
# 	btnr_active = image.load("Buttons/left_active.png")
# 	btnl = image.load("Buttons/right.png")
# 	btnl_active = image.load("Buttons/right_active.png")
# 	bg = image.load('background/eat the apples bg.png')
# 	player_right1 = image.load('turtle right/turtle1.png')
# 	player_right2 = image.load('turtle right/turtle2.png')
# 	player_right3 = image.load('turtle right/turtle3.png')
# 	player_right4 = image.load('turtle right/turtle4.png')
# 	player_left1 = image.load('turtle left/turtle11.png')
# 	player_left2 = image.load('turtle left/turtle22.png')
# 	player_left3 = image.load('turtle left/turtle33.png')
# 	player_left4 = image.load('turtle left/turtle44.png')
# 	block = image.load('ground block/ground_block.png')
# 	ground_lock = image.load('ground block/ground_lock.png')
# 	red_apple = image.load('apples/apple.png')
# 	#########DEFAUT___SKIN######################
# 	skin = player_right1
# 	############################################
# 	green_apple = image.load('apples/apple3.png')
# 	purple_apple = image.load('apples/apple2.png')
# 	live = image.load('live/live.png')
# 	pause = image.load('messages/pause.png')
# 	fall = image.load('messages/fall.png')
# 	rebuild_soild = image.load('messages/rebuild.png')
# 	not_enough = image.load('messages/not_enough.png')
# 	no_broken_solid = image.load('messages/no_broken_solid.png')
# 	lives_increased = image.load('messages/lives_increased.png')
# 	gameoverpic = image.load('background/gameoverpic.png')
# 	intropic = image.load('intro/intropic.png')
# 	play_button_active = image.load('intro/play_button_active.png')
# 	play_button_inactive = image.load('intro/play_button_inactive.png')
# 	how_to_play_button_active = image.load('intro/how_to_play_button_active.png')
# 	how_to_play_button_inactive = image.load('intro/how_to_play_button_inactive.png')
# 	quit_button_active = image.load('intro/quit_button_active.png')
# 	quit_button_inactive = image.load('intro/quit_button_inactive.png')
# 	how_to_pic = image.load('intro/how to play.png')
# 	exit_how_to = image.load('intro/exit how to.png')
# 	###################
# 	skin_changer = 0
# 	###################
# 	#1-5#    
# 	block_x1 = 0
# 	block_y1 = 440
# 	block_x2 = 40
# 	block_y2 = 440
# 	block_x3 = 80
# 	block_y3 = 440
# 	block_x4 = 120
# 	block_y4 = 440
# 	block_x5 = 160
# 	block_y5 = 440
# 	##############
# 	#6-10#
# 	block_x6 = 200
# 	block_y6 = 440
# 	block_x7 = 240
# 	block_y7 = 440
# 	block_x8 = 280
# 	block_y8 = 440
# 	block_x9 = 320
# 	block_y9 = 440
# 	block_x10 = 360
# 	block_y10 = 440
# 	###############
# 	#11-15#
# 	block_x11 = 400
# 	block_y11 = 440
# 	block_x12 = 440
# 	block_y12 = 440
# 	block_x13 = 480
# 	block_y13 = 440
# 	block_x14 = 520
# 	block_y14 = 440
# 	block_x15 = 560
# 	block_y15 = 440
# 	##################
# 	#block_State's
# 	block1s = "placed"
# 	block2s = "placed"
# 	block3s = "placed"
# 	block4s = "placed"
# 	block5s = "placed"
# 	block6s = "placed"
# 	block7s = "placed"
# 	block8s = "placed"
# 	block9s = "placed"
# 	block10s = "placed"
# 	block11s = "placed"
# 	block12s = "placed"
# 	block13s = "placed"
# 	block14s = "placed"
# 	block15s = "placed"
# 	##################
# 	broken_block = False
# 	##################
# 	#block_images#
# 	block1pic = block
# 	block2pic = block
# 	block3pic = block
# 	block4pic = block
# 	block5pic = block
# 	block6pic = block
# 	block7pic = block
# 	block8pic = block
# 	block9pic = block
# 	block10pic = block
# 	block11pic = block
# 	block12pic = block
# 	block13pic = block
# 	block14pic = block
# 	block15pic = block
# 	#red_apple_score#
# 	red_apple_score = 0

def buttons(cx,cy,x,y,w,h,active,inactive):
	if(x + w > cx > x and y + h > cy > y):
		pic = active
		screen.blit(pic,(x,y))
		return True	
	else:
		pic = inactive
		screen.blit(pic,(x,y))

def blition():
	# red_ = redapple()
	global player_x,player_y,player_left_x,player_right_x,player_s,skin,skin_changer
	global red_apple_score,block1pic,block2pic,block3pic,block4pic,block5pic,block6pic
	global block7pic,block8pic,block9pic,block10pic,block11pic,block12pic,block13pic
	global block14pic,block15pic,block1s,block2s,block3s,block4s,block5s,block6s,block7s
	global block8s,block9s,block10s,block11s,block12s,block13s,block14s,block15s,block_x1
	global block_y1,block_x2,block_y2,block_x3,block_y3,block_x4,block_y4,block_x5,block_y5
	global block_x6,block_y6block_x7,block_y7,block_x8,block_y8,block_x9,block_y9,block_x10,block_y10
	global block_x11,block_y11,block_x12,block_y12,block_x13,block_y13,block_x14,block_y14,block_x15,block_y15
	global apple,btnr,btnr_active,btnl,btnl_active,bg,player_right1,player_right2,player_right3,player_right4
	global player_left1,player_left2,player_left3,player_left4,block,ground_lock,red_apple
	global green_apple,purple_apple,live,pause,fall,rebuild_soild,not_enough,no_broken_solid
	global lives_increased,gameoverpic,intropic,play_button_active,play_button_inactive
	global how_to_play_button_active,how_to_play_button_inactive,quit_button_active,quit_button_inactive
	global how_to_pic,exit_how_to

	if(player_s == "turtle11"):
		skin = player_left1
	elif(player_s == "turtle22"):
			skin = player_left2
	elif(player_s == "turtle33"):
			skin = player_left3
	elif(player_s == "turtle44"):
			skin = player_left4
	elif(player_s == "turtle1"):
			skin = player_right1
	elif(player_s == "turtle2"):
			skin = player_right2
	elif(player_s == "turtle3"):
			skin = player_right3
	elif(player_s == "turtle4"):
			skin = player_right4

	#block's_blit_1#
	# red_.run()
	screen.blit(block1pic ,(block_x1,block_y1))
	screen.blit(block2pic ,(block_x2,block_y2))
	screen.blit(block3pic ,(block_x3,block_y3))
	screen.blit(block4pic ,(block_x4,block_y4))
	screen.blit(block5pic ,(block_x5,block_y5))
	#block's_blit_2#
	screen.blit(block6pic ,(block_x6,block_y6))
	screen.blit(block7pic ,(block_x7,block_y7))
	screen.blit(block8pic ,(block_x8,block_y8))
	screen.blit(block9pic ,(block_x9,block_y9))
	screen.blit(block10pic ,(block_x10,block_y10))
	#block's_blit_3#
	screen.blit(block11pic ,(block_x11,block_y11))
	screen.blit(block12pic ,(block_x12,block_y12))
	screen.blit(block13pic ,(block_x13,block_y13))
	screen.blit(block14pic ,(block_x14,block_y14))
	screen.blit(block15pic ,(block_x15,block_y15))
	#########################################
	# screen.blit(red_apple, (apple_x_move,apple_y_move))
	# screen.blit(green_apple, (green_apple_x,green_apple_y))
	# screen.blit(purple_apple, (purple_apple_x,purple_apple_y))
	#screen.blit(skin, (player_x, player_y))
	screen.blit(live, (0,0))
	screen.blit(red_apple, (0, 30))
	screen.blit(skin, (player_x, player_y))

	# screen.blit(,(,))
	# screen.blit(,(,))
	#draw.rect(screen,red,(x,y,50,25),2)

def touch_down(cx,cy):
	global player_x,skin,skin_changer,player_s
	if buttons(cx,cy,0,350,60,60,btnr_active,btnr):
		if(player_x >= -1.75):
			player_x = player_x - 1.25
			if(skin_changer == -10):
				skin_changer = -0.25
			else:
			    skin_changer = skin_changer - 0.25

			if((skin_changer <= 0) and (skin_changer >= -2.50)):
				player_s = "turtle11"
			elif((skin_changer <= -2.50) and (skin_changer >= -5)):
				player_s = "turtle22"
			elif((skin_changer <= -5) and (skin_changer >= -7.50)):
				player_s = "turtle33"
			elif((skin_changer <= -7.50) and (skin_changer >= -10)):
				player_s = "turtle44"  

	elif buttons(cx,cy,0,350,60,60,btnr_active,btnr):
			pass


	if buttons(cx,cy,540,350,60,60,btnl_active,btnl):
		if(player_x <= 569.5):
			player_x = player_x + 1.5
			if(skin_changer == 10):
				skin_changer = 0.25
			else:
			    skin_changer = skin_changer + 0.25

			if((skin_changer >= 0) and (skin_changer <= 2.50)):
				player_s = "turtle1"
			elif((skin_changer >= 2.50) and (skin_changer <= 5)):
				player_s = "turtle2"
			elif((skin_changer >= 5) and (skin_changer <= 7.50)):
				player_s = "turtle3"
			elif((skin_changer >= 7.50) and (skin_changer <= 10)):
				player_s = "turtle4"  
	elif buttons(cx,cy,0,350,60,60,btnr_active,btnr):
			pass

def main():
	global player_x,player_y,player_left_x,player_right_x,skin,skin_changer
	global red_apple_score,block1pic,block2pic,block3pic,block4pic,block5pic,block6pic
	global block7pic,block8pic,block9pic,block10pic,block11pic,block12pic,block13pic
	global block14pic,block15pic,block1s,block2s,block3s,block4s,block5s,block6s,block7s
	global block8s,block9s,block10s,block11s,block12s,block13s,block14s,block15s,block_x1
	global block_y1,block_x2,block_y2,block_x3,block_y3,block_x4,block_y4,block_x5,block_y5
	global block_x6,block_y6block_x7,block_y7,block_x8,block_y8,block_x9,block_y9,block_x10,block_y10
	global block_x11,block_y11,block_x12,block_y12,block_x13,block_y13,block_x14,block_y14,block_x15,block_y15
	global apple,btnr,btnr_active,btnl,btnl_active,bg,player_right1,player_right2,player_right3,player_right4
	global player_left1,player_left2,player_left3,player_left4,block,ground_lock,red_apple
	global green_apple,purple_apple,live,pause,fall,rebuild_soild,not_enough,no_broken_solid
	global lives_increased,gameoverpic,intropic,play_button_active,play_button_inactive
	global how_to_play_button_active,how_to_play_button_inactive,quit_button_active,quit_button_inactive
	global how_to_pic,exit_how_to

	while True:
		touch_ = False
		cx,cy = pygame.mouse.get_pos()
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

			# if(event.type == pygame.KEYDOWN):
			# 	if(event.key == K_p):
			# 		print(player_x,player_y)
			elif event.type == MOUSEBUTTONDOWN:
				touch_ = True
				cx,cy = pygame.mouse.get_pos()

		player_left_x = 0
		
		screen.fill(white)
		screen.blit(bg,(0,0))
		if(touch_ == True):
			touch_down(cx,cy)
		else:
			touch_down(cx,cy)

		blition()
		display.update()

main()