
import os
import random
import pygame

class PlayerSprite(pygame.sprite.Sprite):
  
  def __init__(self):
    super().__init__()

    self.image = pygame.image.load("rocket.png").convert_alpha()
    self.image.set_colorkey([255,255,255])

    self.rect = self.image.get_rect()

  def move(self,dx,dy):
    if dx!=0:
      self.move_single_axis(dx,0)
    if dy!=0:
      self.move_single_axis(0,dy)

  def move_single_axis(self, dx, dy):

    self.rect.x += dx
    self.rect.y += dy


os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()

pygame.display.set_caption("Jump to escape!")
screen  = pygame.display.set_mode((420,340))

clock = pygame.time.Clock()
player = PlayerSprite()
player_sprite = PlayerSprite()
colour = (0,128,255)

running = True

colour = (0,128,255)

while running:
  clock.tick(60)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

    if (event.type == pygame.KEYDOWN) and (event.key ==     pygame.K_SPACE):
      if colour == (0,128,255):
          colour = (255,100,0)
      else:
        colour = (0,128,255)

user_input = pygame.key.get_pressed()

if user_input[pygame.K.UP]:
  player.move(0,-2)

if user_input[pygame.K.DOWN]:
  player.move(0,2)

screen.fill((0,0,0))
pygame.draw.rect(screen,colour,pygame.rect)
pygame.display.flip()

all_sprites_list = pygame.sprite.Group()

player_sprite.rect.x = 100
player_sprite.rect.y = 100

all_sprites_list.draw(screen)

pygame.quit()