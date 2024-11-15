import pygame
import random
pygame.init()
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
fps = 45
b=1
counter = 0

def counter_round():
	global b,fps
	b +=1
	fps +=5  
	if b == 5:
		print('Game Finished')

class Sound():
	def __init__(self,sound):
		self.sound = sound

	def pulya_sound(self):
		 	self.sound = pygame.mixer.Sound("pulya.mp3")
		 	self.sound.set_volume(0.5)
		 	self.sound.play()

	def destroyed_ball(self):
		self.sound = pygame.mixer.Sound("puzir.mp3")
		self.sound.set_volume(1)
		self.sound.play()

	def new_raund_sound(self):

		self.sound = pygame.mixer.Sound("smena1.mp3")
		self.sound.set_volume(1)
		self.sound.play()

	def move_object(self):

		self.sound = pygame.mixer.Sound("move.mp3")
		self.sound.set_volume(0.5)
		self.sound.play()

class Write():
	def __init__(self,color = None,font =(None,32),text = None):

		self.text = text
		self.color = color or ((255,255,255))
		self.font = font

	def round(self):
		font = pygame.font.Font(self.font[0],self.font[1])
		text = font.render('RAUND:' + str(b),True,self.color)
		textRect = text.get_rect()
		textRect.center = (85,50)
		screen.blit(text,textRect)

	def destroyed_balls(self):
		font = pygame.font.Font(self.font[0],self.font[1])
		text = font.render('KILLED:' + str(counter),True,self.color)
		textRect = text.get_rect()
		textRect.center = (85,70)
		screen.blit(text,textRect)

	def totall_balls(self):
		global a
		font = pygame.font.Font(self.font[0],self.font[1])
		text = font.render('BALLS:' + str(len(balls)),True,self.color)
		textRect = text.get_rect()
		textRect.center = (87,90)
		screen.blit(text,textRect)


class puwka():
	def __init__(self,x,y,color= None,left = False,right = False):

		self.left = left
		self.right = right
		self.x = x
		self.y = y 
		if color == None:

			color = ((255,0,0))
		self.color = color

		self.image = pygame.Surface((100,600),pygame.SRCALPHA)

		pygame.draw.polygon(self.image, self.color, [[0 ,100], [35,50], [70,100]] )
		self.speed = 30


	def border_control(self):

		if self.x < 0:
			self.x= 0
		elif self.x + self.image.get_width() > 800:
			self.x = 820 - self.image.get_width()

	def control(self):

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				self.x -=  self.speed
				sound_object.move_object()
			if event.key == pygame.K_RIGHT:
				self.x  += self.speed 
				sound_object.move_object()

class Pulya(puwka):
	def __init__(self,x,y,color = None,rad=5,Shoot= False):
		super().__init__(x,y,color,Shoot)
		self.rad = rad
		self.x = x 
		self.y = y 
		self.Shoot = Shoot
		if color == None:
			color = ((255,5,5))
		self.color = color
		self.speed = 30
		self.mvspeed = 22
		self.image = pygame.Surface((self.rad*2,self.rad*2),pygame.SRCALPHA)
		pygame.draw.circle(self.image,self.color,(self.rad,self.rad),self.rad)
		
	def vistrel(self):

		if self.Shoot:
			self.y -= self.mvspeed

		if self.y < 0:
			self.y = 550
			self.Shoot = False

	def pulya_border_control(self):
		if self.x < 30:
			self.x = 30
		if self.x >750:
			self.x = 750

	def update(self):
		global counter
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				self.Shoot = True
				sound_object.pulya_sound()
		self.rect = pygame.Rect(self.x,self.y,self.rad*2,self.rad*2)
		for ball in balls:
			if self.rect.colliderect(ball.rect):
				balls.remove(ball)
				counter +=1
				sound_object.destroyed_ball()
			   
class Ball():
	def __init__(self,x,y,color= None,rad=22):

		self.rad = rad

		if color == None:
			color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))

		self.color = color

		self.image = pygame.Surface((self.rad * 2, self.rad * 2), pygame.SRCALPHA)

		pygame.draw.circle(self.image, self.color, (self.rad, self.rad), self.rad)

		self.vx = random.randint(-5, 5)

		self.vy = random.randint(1, 2)

		self.x = x if x and y else random.randint(self.rad, 800 - self.rad)

		self.y = y if x and y else random.randint(self.rad, 600 - self.rad)

		self.rect = pygame.Rect(self.x,self.y,self.rad*2,self.rad*2)

	def update(self):
        
		 friction = 1 
		 self.vy *= friction
		 self.y += self.vy
		 if self.y == 0:
		 	self.y = 0
		 	self.vy = -self.vy
		 elif self.y + self.rad * 2 > 600:
		 	self.x = random.randint(self.rad, 800 - self.rad)
		 	self.y = 600 - self.rad * 2
		 	self.y = self.rad /100
		 	self.vy = +self.vy
		 	self.rect = pygame.Rect(self.x,self.y,self.rad*2,self.rad*2)

sound_object = Sound(None)
write_object = Write()
pulya_object = Pulya(430,550)
puwka_object = puwka(400,495)
 
a = 10
balls = [Ball(None,None) for i in range(a)]

def new_raund():
	global a
	a +=1
	for ball in range(a):
	  balls.append(Ball(None,None))

running = True

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    puwka_object.control()
    pulya_object.control()
    pulya_object.update()
  for ball in balls:
   	ball.update()
  for ball in balls.copy():
  	if pulya_object.rect.colliderect(ball.rect):
  		counter +=1
  		sound_object.destroyed_ball()

  		balls.remove(ball)

  pulya_object.vistrel()

  puwka_object.border_control()

  pulya_object.pulya_border_control()

  screen.fill((0,0,0))

  for ball in balls:
    ball.update()

    screen.blit(ball.image,(ball.x,ball.y))

  write_object.destroyed_balls() 
  write_object.round()
  write_object.totall_balls()

  screen.blit(puwka_object.image,(puwka_object.x,puwka_object.y))
  screen.blit(pulya_object.image,(pulya_object.x,pulya_object.y)) 

  if len(balls) == 0:
  	counter_round()  
  	new_raund() 
  	sound_object.new_raund_sound()
  pygame.display.flip()

  clock.tick(fps)

pygame.quit()
