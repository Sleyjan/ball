import pygame
import random
pygame.init()
screen = pygame.display.set_mode((800,600))


clock = pygame.time.Clock()
fps = 60

class puwka():
	def __init__(self,x,y,color= None):

		self.x = x
		self.y = y 
		if color == None:

			color = ((0,255,0))
		self.color = color

		self.image = pygame.Surface((100,600),pygame.SRCALPHA)

		pygame.draw.polygon(self.image, self.color, [[0 ,100], [35,50], [70,100]] )

		def moving(self):
			pass


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

	def update(self):
        
		 friction = 1 
		 # self.vx *= friction 
		 self.vy *= friction
		 #self.x += self.vx
		 self.y += self.vy

        
		 #if self.x < 0:
		 #	self.x = 0
		 	#self.vx = -self.vx
		 #elif self.x + self.rad * 2 > 800:
		 	#self.x = 800 - self.rad * 2
		 #	self.vx = -self.vx

		 if self.y == 0:
		 	self.y = 0
		 	self.vy = -self.vy
		 elif self.y + self.rad * 2 > 600:

		 	self.x = random.randint(self.rad, 800 - self.rad)
		 	self.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
		 	self.y = 600 - self.rad * 2
		 	self.y = self.rad /100
		 	self.vy = +self.vy


puwka_object = puwka(400,495)

balls = [Ball(None,None) for i in range(8)]
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
 	
  screen.fill((0,0,0))

  for ball in balls:
    ball.update()

    screen.blit(ball.image,(ball.x,ball.y))

  screen.blit(puwka_object.image,(puwka_object.x,puwka_object.y))


  

  pygame.display.flip()

  clock.tick(fps)

pygame.quit()
