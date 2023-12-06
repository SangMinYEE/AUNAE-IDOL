import pygame
import random
import time

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)

note_width = 50
note_height = 50
note_speed = 1

note_array = [1,1,1,1,1,0,1,0,0,1,1,1,0,0,0,1,0,0,1,0,0,1,0]
notes = []

red_note = pygame.Rect(screen_width - note_width, random.randint(0, screen_height - note_height), note_width, note_height)

blue_note = pygame.Rect(screen_width - note_width, random.randint(0, screen_height - note_height), note_width, note_height)

clock = pygame.time.Clock()

start_time = time.time()

running = True
while running:
    #이벤트처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #경과 시간
    elapsed_time = time.time() - start_time
    #1초 보다 더 지날때
    if elapsed_time >= 1:
        for i in range(len(note_array)):#23번 반복
            if note_array[i] == 1:
                #빨간노트 생성
                red_note = pygame.Rect(screen_width - note_width, random.randint(0, screen_height - note_height), note_width, note_height)
            elif note_array[i] == 0:
                #파란노트 생성
                blue_note = pygame.Rect(screen_width - note_width, random.randint(0, screen_height - note_height), note_width, note_height)

                #시작시간 초기화
        start_time = time.time()

    screen.fill(white)
    for i in range(len(note_array)):
        if note_array[i] == 1:
            pygame.draw.rect(screen, red, red_note)
            red_note.x -= note_speed #노트 오른쪽에서 왼쪽으로 이동
        elif note_array[i] == 0:
            pygame.draw.rect(screen, blue, blue_note)
            blue_note.x -= note_speed 


    clock.tick(30)

    pygame.display.flip()

pygame.quit()
