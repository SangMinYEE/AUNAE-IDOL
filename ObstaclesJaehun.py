'''
랜덤함수 이용시 장애물 가까운 부분 고치기
'''

import pygame
import sys
import random

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("집사를 찾아서")

game_back_ground_path = pygame.image.load("./pygame-2--main/bg/image_game.png")
game_back_ground = pygame.transform.scale(game_back_ground_path, (2771, height))
bg_x = 0

try:
    pygame.mixer.music.load("./pygame-2--main/bgm/AcousticBeat.ogg")
except:
    print("ogg 파일이 맞지 않거나, 오디오 기기가 접속되어 있지 않습니다")

white = (255, 255, 255)
black = (0, 0, 0)

# 장애물 설정 1
obstacle_width, obstacle_height = 50, 50
obstacle_speed = 12
obstacle_timer = pygame.time.get_ticks()
obstacles = []  # 여러 장애물 저장
obstacle_image = pygame.image.load("./pygame-2--main/obstacles/IMG_2388.png")
obstacle_image = pygame.transform.scale(obstacle_image, (obstacle_width, obstacle_height))

# 장애물 설정 2
obstacle_2_width, obstacle_2_height = 100, 100
obstacle_2_speed = 17
obstacle_2_timer = pygame.time.get_ticks()
obstacles_2 = []  # 여러 장애물 저장
obstacle_2_image = pygame.image.load("./pygame-2--main/obstacles/IMG_2386.png")
obstacle_2_image = pygame.transform.scale(obstacle_2_image, (obstacle_2_width, obstacle_2_height))

# 캐릭터 설정
character_width, character_height = 60, 60
character_x, character_y = width // 3 - character_width // 2, height - character_height * 2
character_image = [
        pygame.image.load("./pygame-2--main/black_cat/black_cat0.png"),
        pygame.image.load("./pygame-2--main/black_cat/black_cat1.png"),
        pygame.image.load("./pygame-2--main/black_cat/black_cat2.png"),
        pygame.image.load("./pygame-2--main/black_cat/black_cat3.png")
    ]
chr = 0
character_image[0] = pygame.transform.scale(character_image[0], (character_width, character_height))
character_image[1] = pygame.transform.scale(character_image[1], (character_width, character_height))
character_image[2] = pygame.transform.scale(character_image[2], (character_width, character_height))
character_image[3] = pygame.transform.scale(character_image[3], (character_width, character_height))

#점프
character_jump = False
f_jump = False
default_count = 11
jump_count = default_count

# 체력 설정
Heart = 3

# 무적 상태 설정
invincible_duration = 1500
invincible_timer = 0
is_invincible = False

# 반짝임 설정
blink_duration = 1500
blink_timer = 0
is_blinking = False

font = pygame.font.Font(None, 36)

if pygame.mixer.music.get_busy() == False:
        pygame.mixer.music.play(-1)

while True:
    chr += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    # 장애물1 등장 시간 랜덤(2~10)
    obstacle_interval_random = random.randrange(20,110)
    obstacle_interval = obstacle_interval_random * 100 #0.1초
    # 장애물2 등장 시간 랜덤(4~12)
    obstacle_2_interval_random = random.randrange(40,130)
    obstacle_2_interval = obstacle_2_interval_random * 100 #0.1초

    # 캐릭터 F점프
    if keys[pygame.K_f] and not character_jump:
        character_jump = True
        f_jump = True

    if (character_jump == True):
    # f 눌렀을때 점프 스타일
        if (f_jump == True):
            if jump_count >= -default_count and jump_count < 0:
                character_y += (jump_count ** 2) * 0.5
                jump_count -= 1
            
            elif jump_count >= 0 :
                character_y -= (jump_count ** 2) * 0.5
                jump_count -= 1
            
            else:
                character_jump = False
                f_jump = False
                jump_count = default_count

    # 새로운 장애물을 생성할 시간인지 확인
    current_time = pygame.time.get_ticks()
    if current_time - obstacle_timer > obstacle_interval:
        obstacle_x = width
        obstacle_y = height - character_height * 2+40
        obstacles.append((obstacle_x, obstacle_y))
        obstacle_timer = current_time

    if current_time - obstacle_2_timer > obstacle_2_interval:
        obstacle_2_x = width
        obstacle_2_y = height - (character_height * 2) - 60
        obstacles_2.append((obstacle_2_x, obstacle_2_y))
        obstacle_2_timer = current_time

    # 장애물 위치 업데이트
    for i in range(len(obstacles)):
        obstacles[i] = (obstacles[i][0] - obstacle_speed, obstacles[i][1])

    for i in range(len(obstacles_2)):
        obstacles_2[i] = (obstacles_2[i][0] - obstacle_2_speed, obstacles_2[i][1])

    # 화면에서 벗어난 장애물 제거
    obstacles = [obs for obs in obstacles if obs[0] + obstacle_width > 0]
    obstacles_2 = [obs for obs in obstacles_2 if obs[0] + obstacle_2_width > 0]
    '''
    obs는 obstacles 리스트의 각 요소를 나타냅니다.
    obs[0]는 장애물의 x 좌표를 나타냅니다.
    obstacle_width는 장애물의 가로 길이를 나타냅니다.
    따라서 obs[0] + obstacle_width는 장애물의 오른쪽 끝 부분의 x 좌표를 나타냅니다
    '''
    # 무적 업데이트
    if is_invincible and current_time - invincible_timer > invincible_duration:
        is_invincible = False
    
    # 반짝임 업데이트
    if is_blinking and current_time - blink_timer > blink_duration:
        is_blinking = False

    # 장애물1과 충돌 확인
    for obstacle in obstacles:
        obstacle_rect = pygame.Rect(obstacle[0], obstacle[1], obstacle_width, obstacle_height)
        character_rect = pygame.Rect(character_x, character_y, character_width, character_height)

        if character_rect.colliderect(obstacle_rect):
            if not is_invincible:
                Heart -= 1
                is_invincible = True
                invincible_timer = current_time
                is_blinking = True
                blink_timer = current_time
            elif Heart <= 0:
                # 체력이 0이면 캐릭터를 화면 밖으로 이동(캐릭터 사라짐)
                character_x = -100
                if pygame.mixer.music.get_busy() == True:
                    pygame.mixer.music.stop()

    # 장애물2와 충돌 확인
    for obstacle_2 in obstacles_2:
        obstacle_2_rect = pygame.Rect(obstacle_2[0], obstacle_2[1], obstacle_2_width, obstacle_2_height)
        character_rect = pygame.Rect(character_x, character_y, character_width, character_height)

        if character_rect.colliderect(obstacle_2_rect):
            if not is_invincible:
                Heart -= 1
                is_invincible = True
                invincible_timer = current_time
                is_blinking = True
                blink_timer = current_time
            elif Heart <= 0:
                # 체력이 0이면 캐릭터를 화면 밖으로 이동(캐릭터 사라짐)
                character_y = -1000
                if pygame.mixer.music.get_busy() == True:
                    pygame.mixer.music.stop()

    bg_x -= 5
    
    if bg_x < -game_back_ground.get_width():
        bg_x = 0

    screen.blit(game_back_ground, (bg_x, 0))
    screen.blit(game_back_ground, (bg_x + game_back_ground.get_width(), 0))

    # 장애물1과 장애물2가 겹치면 장애물이 사라지도록 함
    for obstacle_1 in obstacles:
        obstacle_1_rect = pygame.Rect(obstacle_1[0], obstacle_1[1], obstacle_width, obstacle_height)
    
        for obstacle_2 in obstacles_2:
            obstacle_2_rect = pygame.Rect(obstacle_2[0], obstacle_2[1], obstacle_2_width, obstacle_2_height)

            if obstacle_1_rect.colliderect(obstacle_2_rect):
                # 겹치는 경우, 둘 중 하나를 삭제
                if random.choice([True, False]):
                    obstacles.remove(obstacle_1)
                else:
                    obstacles_2.remove(obstacle_2)
    


    # 장애물 그리기
    for obstacle in obstacles:
        screen.blit(obstacle_image, (obstacle[0], obstacle[1]))

    for obstacle_2 in obstacles_2:
        screen.blit(obstacle_2_image, (obstacle_2[0], obstacle_2[1]))

    # 캐릭터 그리기
    if not is_blinking or (is_blinking and current_time % 200 < 100):
        screen.blit(character_image[chr%4], (character_x, character_y))

    # 체력 표시
    stamina_text = font.render(f"Heart: {Heart}", True, black)
    screen.blit(stamina_text, (width - 150, 20))

    # 무적 표시
    if is_invincible:
        invincible_text = font.render("Invincible!", True, black)
        screen.blit(invincible_text, (width - 150, 60))

    # 화면 업데이트
    pygame.display.flip()

    # 프레임 속도 조절
    pygame.time.Clock().tick(30)