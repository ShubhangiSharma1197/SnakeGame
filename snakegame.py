# Snake Game
import pygame  #libraries
import sys
import random
import time
#print(pygame.init())
check_errors=pygame.init()
if check_errors[1]>0:
    print("Had {0} initializing errors".format(check_errors[1]))
    sys.exit(-1)
else:
    print("pygame successfully installed")
#Creating Player Surface
playSurface = pygame.display.set_mode((720,460)) #receives a tuple,only one argument
pygame.display.set_caption('Snake Game By Shubhangi!!')

#Colors
red=pygame.Color(255,0,0)#red color for GAME OVER message   (r,g,b) for pixel
green=pygame.Color(0,255,0)#color of Snake
black=pygame.Color(0,0,0)#absence of color ,score
white=pygame.Color(255,255,255)#background
brown=pygame.Color(165,42,42)#food
# Frame per second Controller
fpsController=pygame.time.Clock()
#Variables
snakePos=[100,50] #position of snake coordinates
snakeBody=[[100,50],[90,50],[80,50]]  #initially snake is only three blocks long
#random module used for food
foodPos=[random.randrange(1,72)*10,random.randrange(1,46)*10] #10 because the snake will then only pass through food and within the frame
foodSpawn=True
direction ='RIGHT'#initially direction will be right
changeto = direction
score=0

#Game Over Function
def gameOver():      #two types of fonts---System font that comes within OS and file font
   myFont=pygame.font.SysFont('monaco',72)
   GOsurf=myFont.render('Game Over!',True,red) #receives text,anti-aliased ,color also takes background which is default here
   GOrect=GOsurf.get_rect()
   GOrect.midtop=(360,15)
   playSurface.blit(GOsurf,GOrect)
   showScore(0)
   pygame.display.flip()
   time.sleep(4)
   pygame.quit()#for game
   sys.exit()#for console
#show score
def showScore(choice=1):     #argument for printing score at two different positions
   sFont=pygame.font.SysFont('monaco',30)
   ssurf=sFont.render('Score : '+str(score),True,black)
   srect=ssurf.get_rect()
   if choice==1:
         srect.midtop=(80,10)
   else:
         srect.midtop=(360,120)
   playSurface.blit(ssurf,srect)

#Events
while True:
   for event in pygame.event.get():  #for looping through events    gives a list of events in pygame
         if event.type==pygame.QUIT:
             pygame.quit()
             sys.exit()
         elif event.type==pygame.KEYDOWN:
             if event.key==pygame.K_RIGHT or event.key== ord('d'):
                 changeto='RIGHT'
             if event.key==pygame.K_LEFT or event.key==ord('a'):
                 changeto='LEFT'
             if event.key==pygame.K_UP or event.key==ord('w'):
                 changeto='UP'
             if event.key==pygame.K_DOWN or event.key==ord('s'):
                 changeto='DOWN'
             if event.key==pygame.K_ESCAPE:
                 pygame.event.post(pygame.event.Event(pygame.QUIT))
#validation of direction
#if direction left we cant directly make it go right and same for all
   if changeto=='RIGHT' and not direction=='LEFT':
         direction='RIGHT'
   if changeto=='LEFT' and not direction=='RIGHT':
         direction='LEFT'
   if changeto=='UP' and not direction=='DOWN':
         direction='UP'
   if changeto=='DOWN' and not direction=='UP':
         direction='DOWN'
   if direction=='RIGHT':
         snakePos[0] += 10
   if direction=='LEFT':
         snakePos[0] -= 10
   if direction=='UP':
         snakePos[1] -= 10
   if direction=='DOWN':
         snakePos[1] += 10
#Snake Body mechanism
   snakeBody.insert(0,list(snakePos))
   if snakePos[0] == foodPos[0] and snakePos[1] == foodPos[1]:
         score += 10  #basically food found and a hit
         foodSpawn = False  #food is not on screen,we ate it and grew bigger
   else:
         snakeBody.pop()
   if foodSpawn == False:
         foodPos=[random.randrange(1,72)*10,random.randrange(1,46)*10]
   foodSpawn = True
#Drawing
   playSurface.fill(white)
   for pos in snakeBody:
         pygame.draw.rect(playSurface,green,
         pygame.Rect(pos[0],pos[1],10,10))
   pygame.draw.rect(playSurface,brown,
   pygame.Rect(foodPos[0],foodPos[1],10,10))
   if snakePos[0] > 710 or snakePos[0] < 0:         #not 720 because then after 2 blocks of snake body game over comes but we want for one block
         gameOver()
   if snakePos[1] > 450 or snakePos[1] < 0:
         gameOver()
   for block in snakeBody[1:]:
         if snakePos[0] == block[0] and snakePos[1] == block[1]:
                 gameOver()
   showScore()
   pygame.display.flip()
   fpsController.tick(15)
