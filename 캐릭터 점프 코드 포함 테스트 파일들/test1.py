import pygame
import sys

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Jumping Character")

white = (255, 255, 255)
red = (255, 0, 0)

character_width = 50
character_height = 50
character_x = screen_width // 2 - character_width // 2 # 캐릭터 왼쪽 모서리 X좌표
character_y = screen_height - character_height # 캐릭터 윗쪽 모서리 Y좌표
character_jump = False
default_count = 10
jump_count = default_count

running = True

clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_SPACE] and not character_jump:
        character_jump = True

    if (character_jump == True):
        
        if jump_count >= -default_count and jump_count < 0:
            
            character_y += (jump_count ** 2) * 0.5 
            jump_count -= 1
            
        elif jump_count >= 0 :
            
            character_y -= (jump_count ** 2) * 0.5 
            jump_count -= 1
            
        else:
            character_jump = False
            jump_count = default_count

    screen.fill(white)
    pygame.draw.rect(screen, red, (character_x, character_y, character_width, character_height))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()