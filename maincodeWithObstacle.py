import pygame
import sys
import time 
import random

pygame.init() # 초기화
screen_width=800
screen_height=600

# 창 화면
width, height = 800, 600
screen = pygame.display.set_mode((screen_width,screen_height))
Clock = pygame.time.Clock()

pygame.display.set_caption("리듬게임")

white = (255, 255, 255) # 배경색
black = (0, 0, 0)

font = pygame.font.Font("./pygame-2--main/font/NeoDunggeunmoPro-Regular.ttf", 30)

title_path="./pygame-2--main/bg/title.png"
title_image=pygame.image.load(title_path)
title_image.get_size()
title_x,title_y=(130, 100)

# 시작 버튼 이미지 
start_button_path="./pygame-2--main/button/button_start.png"
start_button_image=pygame.image.load(start_button_path)
button_width,button_height=start_button_image.get_size()
st_button_x, st_button_y=(305-160,300+100)

# 질문 버튼 이미지 
question_button_path="./pygame-2--main/button/button_question.png"
question_button_image=pygame.image.load(question_button_path)
button_width,button_height=question_button_image.get_size()
qu_button_x, qu_button_y=(305+150,296+100)

# 클릭 말풍선 이미지 
click_image_path="./pygame-2--main/button/click.png"
click_image=pygame.image.load(click_image_path)
cilck_width,click_height=click_image.get_size()

st_click_button_x,st_click_button_y=(1000,1000)
qu_click_button_x,qu_click_button_y=(1000,1000)

# 시작화면 함수
def start_screen():
     
    
    background_image = pygame.image.load("./pygame-2--main/bg/start_back_ground.png")  # 실제 이미지 파일 경로로 대체해
    background_image = pygame.transform.scale(background_image, (width, height))
    screen.blit(background_image, (0, 0)) 
    # 버튼을 그림
    screen.blit(start_button_image, (st_button_x, st_button_y))
    screen.blit(question_button_image, (qu_button_x, qu_button_y))
    screen.blit(title_image,(title_x,title_y))
    start_button_rect=draw_button("시작",(305-65,437))
    question_button_rect=draw_button("설명하기",(550,437))

    pygame.display.update() # 화면 업뎃

    while True:
        for event in pygame.event.get(): # 이벤트에 있는 모든 이벤트 가져옴
            if event.type == pygame.QUIT: # 이벤트 타입이 윈도우 닫기 이벤트인지 확인
                pygame.quit()
                sys.exit()
            elif event.type==pygame.MOUSEBUTTONDOWN:
                # 이벤트 타입이 마우스버튼을 누르기 이벤트인지 확인 
                if start_button_rect.collidepoint(event.pos):
                    return "story" 
                if question_button_rect.collidepoint(event.pos):
                    return "next_question"
            mouse_x,mouse_y=pygame.mouse.get_pos()
            if start_button_rect.collidepoint(mouse_x,mouse_y):
                screen.blit(click_image,(st_click_button_x-725,st_click_button_y-730+100))
        pygame.display.update()
        
def story_screen():
    background_path = pygame.image.load("./pygame-2--main/story_image/story_1.png")  # 실제 이미지 파일 경로로 대체해
    background_image = pygame.transform.scale(background_path, (width, height))
    screen.blit(background_image, (0, 0))

    next_button_text=font.render("next >",True,(255,255,255))
    next_button_rect=next_button_text.get_rect(center=(720,530))
    screen.blit(next_button_text,next_button_rect)
    skip_button_text=font.render("skip >>",True,(255,255,255))
    skip_button_rect=skip_button_text.get_rect(center=(720,50))
    screen.blit(skip_button_text,skip_button_rect)
    
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==pygame.MOUSEBUTTONDOWN:
                    # 이벤트 타입이 마우스버튼을 누르기 이벤트인지 확인 
                if next_button_rect.collidepoint(event.pos):
                    return "next1_story"
                if skip_button_rect.collidepoint(event.pos):
                    return "game_ready"
                
def next1_story():
    story2_image = pygame.image.load("./pygame-2--main/story_image/story_2.png")  
    story2_image = pygame.transform.scale(story2_image, (width, height))
    screen.blit(story2_image, (0, 0))

    next_button_text=font.render("next >",True,(255,255,255))
    next_button_rect=next_button_text.get_rect(center=(720,530))
    screen.blit(next_button_text,next_button_rect)

    pygame.display.update()
    
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==pygame.MOUSEBUTTONDOWN:
                # 이벤트 타입이 마우스버튼을 누르기 이벤트인지 확인 
                if next_button_rect.collidepoint(event.pos):
                    return "next2_story"


def next2_story():
    story2_image = pygame.image.load("./pygame-2--main/story_image/story_3.png")  
    story2_image = pygame.transform.scale(story2_image, (width, height))
    screen.blit(story2_image, (0, 0))

    next_button_text=font.render("next >",True,(255,255,255))
    next_button_rect=next_button_text.get_rect(center=(720,530))
    screen.blit(next_button_text,next_button_rect)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==pygame.MOUSEBUTTONDOWN:
                # 이벤트 타입이 마우스버튼을 누르기 이벤트인지 확인 
                if next_button_rect.collidepoint(event.pos):
                    print("클릭")
                    return "next3_story"    

def next3_story():
    screen.fill(white)
    
    story3_image = pygame.image.load("./pygame-2--main/story_image/story_button.png")  
    story3_image = pygame.transform.scale(story3_image, (width, height))
    screen.blit(story3_image, (0, -20))
    start_button_rect=draw_button("        ",(width//2,280))
    start_button_rect=draw_button("        ",(width//2,300))
    start_button_rect=draw_button("        ",(width//2,320))
 


    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==pygame.MOUSEBUTTONDOWN:
                mouse_x,mouse_y=pygame.mouse.get_pos()
                if start_button_rect.collidepoint(mouse_x,mouse_y):
                    return "game_ready"
            mouse_x,mouse_y=pygame.mouse.get_pos()
            if start_button_rect.collidepoint(mouse_x,mouse_y):
                screen.blit(click_image,(550,150))
        pygame.display.update()
        

cat_x=0    
def next_start_screen():
    global cat_x
    # 게임 선택 배경화면 
    background_path = pygame.image.load("./pygame-2--main/bg/next_back_grond.jpg")  # 실제 이미지 파일 경로로 대체해
    background_image = pygame.transform.scale(background_path, (width, height))
    screen.blit(background_image, (0, 0))

    return_button_rect=draw_button("<< back",(125,45))


    pygame.draw.rect(screen,(225,225,255),[50,110,320,270])

    music_albom_path="./pygame-2--main/music_albom_picture.png"
    music_albom_image=pygame.image.load(music_albom_path)
    music_albom_width,music_albom_height=music_albom_image.get_size()
    music_albom_x, music_albom_y=(60,120)

    music_choice=draw_button("music",(203,90))
    stage1_name=draw_button("<stage1>",(203,410))
    stage1_music=draw_button("-The Way to You-",(203,450))

    game_start_button_path = "./pygame-2--main/button/button_question_copy.png"
    game_start_button = pygame.image.load(game_start_button_path)
    gameStart_rect = game_start_button.get_rect(topleft=(123, 480))
    screen.blit(game_start_button, (123, 480))

    game_start_button_rect=draw_button("start!",(203,515))

    screen.blit(music_albom_image, (music_albom_x,music_albom_y))

    black_cat_image = pygame.image.load("./pygame-2--main/black_cat/black_cat0.png")
    black_cat_image = pygame.transform.scale(black_cat_image,(300,300))
    three_color_cat_image = pygame.image.load("./pygame-2--main/three_color_cat/three_color_cat0.png")
    three_color_cat_image = pygame.transform.scale(three_color_cat_image,(300,300))
    cheese_cat_image = pygame.image.load("./pygame-2--main/cheese_cat/cheese_cat0.png")
    cheese_cat_image = pygame.transform.scale(cheese_cat_image,(300,300))
    screen.blit(three_color_cat_image,(430,30))
    pygame.display.update()
    cat_x=0
    catlist =[three_color_cat_image,black_cat_image,cheese_cat_image]
    draw_button("<고양이를 선택하세요!>",(590,80))

    cat_select_button_path = "./pygame-2--main/tuna/l0_tuna1.png"
    cat_select_button_right = pygame.image.load(cat_select_button_path)
    game_start_button_width, game_start_button_height = cat_select_button_right.get_size()
    screen.blit(cat_select_button_right, (730,190))

    cat_select_button_path = "./pygame-2--main/tuna/l0_tuna1.png"
    cat_select_button_left = pygame.image.load(cat_select_button_path)
    game_start_button_width, game_start_button_height = cat_select_button_left.get_size()
    screen.blit(cat_select_button_left, (415,190))


    pygame.display.update()


    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==pygame.MOUSEBUTTONDOWN:
                if(mouse_x>=700 and mouse_x <= 700+60 and mouse_y >= 190-30 and mouse_y<= 190+30):
                    cat_x+=1
                    screen.blit(catlist[cat_x%3],(430,30))
                if(mouse_x>=415-30 and mouse_x <= 415+30 and mouse_y >= 190-30 and mouse_y<= 190+30):
                    cat_x-=1
                    screen.blit(catlist[cat_x%3],(430,30))
                
                if return_button_rect.collidepoint(event.pos):
                    return "start"
                if gameStart_rect.collidepoint(event.pos):
                    return "game_mode"
            mouse_x,mouse_y=pygame.mouse.get_pos()
            pygame.display.update()

######################################게임 중인 화면########################################
def game_mode():
    global cat_x
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
    
    screen.fill(white)
    #점프 확인 & fghj 점프 확인 부울 타입
    character_jump = False

    f_jump = False
    g_jump = False
    h_jump = False
    j_jump = False
    #점프 시 캐릭터가 10,9,8,...-8,-9,-10으로 움직임
    default_count = 10
    jump_count = default_count    
    x1=0 #고양이 이미지 변수
    x2=0 #스크린 이동 변수
    character_width, character_height = 60, 60 #고양이 크기
    character_x, character_y = width // 3 - character_width // 2, height - character_height * 2 #고양이 위치

    try:
        game_music = pygame.mixer.Sound("./pygame-2--main/bgm/AcousticBeat.ogg")
    except:
        print("ogg 파일이 맞지 않거나, 오디오 기기와 접속되어 있지 않습니다.")
    # 노래 반복 재생
    game_music.play(-1)
    #각 고양이 별 이미지 로드 및 크기 조절
    black_cat_image1 = pygame.image.load("./pygame-2--main/black_cat/black_cat1.png")
    black_cat_image2 = pygame.image.load("./pygame-2--main/black_cat/black_cat2.png")
    black_cat_image3 = pygame.image.load("./pygame-2--main/black_cat/black_cat3.png")
    black_cat_image1 = pygame.transform.scale(black_cat_image1,(character_width,character_height))
    black_cat_image2 = pygame.transform.scale(black_cat_image2,(character_width,character_height))
    black_cat_image3 = pygame.transform.scale(black_cat_image3,(character_width,character_height))

    three_color_cat_image1 = pygame.image.load("./pygame-2--main/three_color_cat/three_color_cat1.png")
    three_color_cat_image2 = pygame.image.load("./pygame-2--main/three_color_cat/three_color_cat2.png")
    three_color_cat_image3 = pygame.image.load("./pygame-2--main/three_color_cat/three_color_cat3.png")
    three_color_cat_image1 = pygame.transform.scale(three_color_cat_image1,(character_width,character_height))
    three_color_cat_image2 = pygame.transform.scale(three_color_cat_image2,(character_width,character_height))
    three_color_cat_image3 = pygame.transform.scale(three_color_cat_image3,(character_width,character_height))
    
    cheese_cat_image1 = pygame.image.load("./pygame-2--main/cheese_cat/cheese_cat1.png")
    cheese_cat_image2 = pygame.image.load("./pygame-2--main/cheese_cat/cheese_cat2.png")
    cheese_cat_image3 = pygame.image.load("./pygame-2--main/cheese_cat/cheese_cat3.png")
    cheese_cat_image1 = pygame.transform.scale(cheese_cat_image1,(character_width,character_height))
    cheese_cat_image2 = pygame.transform.scale(cheese_cat_image2,(character_width,character_height))
    cheese_cat_image3 = pygame.transform.scale(cheese_cat_image3,(character_width,character_height))
    
    #게임 플레이 시 배경 이미지 파일
    bg_image = pygame.image.load("./pygame-2--main/bg/image_game.png")
    bg_image_rect = bg_image.get_rect()
    bg_image_width = bg_image_rect.width
    #catlist =[three_color_cat_image,black_cat_image,cheese_cat_image]
    color_cat_list = [[three_color_cat_image1,three_color_cat_image2,three_color_cat_image3],
                      [black_cat_image1,black_cat_image2,black_cat_image3],
                      [cheese_cat_image1,cheese_cat_image2,cheese_cat_image3]]
    #캐릭터의 x,y좌표
    character_rect = pygame.Rect(character_x, character_y, 60, 60)

    while True:
        #화면창종료표시
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            
        if(x2<-bg_image_width):
            x2=0
        screen.blit(bg_image,(x2,0))
        screen.blit(bg_image,(x2+bg_image_width,0))
        x2-=3
        # 장애물1 등장 시간 랜덤(2~10)
        obstacle_interval_random = random.randrange(20,110)
        obstacle_interval = obstacle_interval_random * 100 #0.1초
        # 장애물2 등장 시간 랜덤(4~12)
        obstacle_2_interval_random = random.randrange(40,130)
        obstacle_2_interval = obstacle_2_interval_random * 100 #0.1초
        
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
        
        # 무적 업데이트
        if is_invincible and current_time - invincible_timer > invincible_duration:
            is_invincible = False
        
        # 반짝임 업데이트
        if is_blinking and current_time - blink_timer > blink_duration:
            is_blinking = False
            
        # 체력 표시
        stamina_text = font.render(f"Heart: {Heart}", True, black)
        screen.blit(stamina_text, (width - 150, 20))

        # 무적 표시
        if is_invincible:
            invincible_text = font.render("Invincible!", True, black)
            screen.blit(invincible_text, (width - 150, 60))
        
        x1 += 1
                # 캐릭터 그리기
        if not is_blinking or (is_blinking and current_time % 200 < 100):
            screen.blit(color_cat_list[cat_x%3][x1%3],(character_x,character_y))
        keys = pygame.key.get_pressed()
            
    #캐릭터 점프 fghj 눌렀을때
        if keys[pygame.K_f] and not character_jump:
            character_jump = True
            f_jump = True
        elif keys[pygame.K_g] and not character_jump:
            character_jump = True
            g_jump = True
        elif keys[pygame.K_h] and not character_jump:
            character_jump = True
            h_jump = True
        elif keys[pygame.K_j] and not character_jump:
            character_jump = True
            j_jump = True
    
    #### fghj 키마다 점프 스타일   #### 
        if (character_jump == True):
        #f 눌렀을때 점프 스타일
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
        #g 눌렀을 때 점프 스타일
            elif (g_jump == True):
            
                if jump_count >= -default_count and jump_count < 0:
                    character_y += (jump_count ** 2) * 0.2
                    jump_count -= 1
            
                elif jump_count >= 0 :
                    character_y -= (jump_count ** 2) * 0.2
                    jump_count -= 1
            
                else:
                    character_jump = False
                    g_jump = False
                    jump_count = default_count         
        #h 눌렀을 때 점프 스타일
            elif (h_jump == True):
                if jump_count >= -default_count and jump_count < 0:
                    character_y -= (jump_count ** 3)*0.05
                    jump_count -= 1
        
                elif jump_count >= 0 :
                    character_y -= (jump_count ** 3)*0.05
                    jump_count -= 1
            
                else:
                    character_jump = False
                    h_jump = False
                    jump_count = default_count

        #j 눌렀을 때 점프 스타일
            elif (j_jump == True):
                if jump_count >= -default_count and jump_count < 0:
                    character_y += (jump_count ** 2) 
                    jump_count -= 1
            
                elif jump_count >= 0 :
                    character_y -= (jump_count ** 2)
                    jump_count -= 1
            
                else:
                    character_jump = False
                    j_jump = False
                    jump_count = default_count
        
        pygame.display.update()
        Clock.tick(30)
##############################여기까지 게임화면##############################3


    
# 시작 버튼 다음 화면
# 시작 배경음악 있어야 하나..?
# 시작 누르고 다음화면으로 넘어가서 음악고르는 화면


# 설명버튼 다음화면
# 설명에 들어가야할 내용
# 뒤로가기 키 설정 
# 일시정지 키 설정 
# 키를 이용하여 캐릭터를 어떻게 움직일 수 있는지 설명
def next_question_screen():
    screen.fill(white)

    text=font.render("설명",True,(0,0,0))
    text_rect=text.get_rect(center=(width// 2,height//2))
    screen.blit(text,text_rect)

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()


# 버튼그림,rect반환시킴

def draw_button(text, position):
    font_color=(0,0,0)
    button_image = font.render(text, True, font_color)
    button_rect = button_image.get_rect(center=position)
    screen.blit(button_image, button_rect)
    return button_rect # 꼭 반환시켜야함

current_state ="start"

running = True # True로 초기화
while running:
    for event in pygame.event.get(): # 사용자의 입력을 감지하고 동작처리
        if event.type == pygame.QUIT: # quit를 감지>> running을 False로 설정
            running = False

    if current_state == "start":
        current_state = start_screen()
    elif current_state == "story":
        current_state = story_screen()
    elif current_state == "next_question":
        current_state = next_question_screen()
    elif current_state == "next1_story":
        current_state = next1_story()
    elif current_state == "next2_story":
        current_state = next2_story()
    elif current_state == "next3_story":
        current_state = next3_story()
    elif current_state == "game_ready":
        current_state = next_start_screen()
    elif current_state == "game_mode":
        current_state = game_mode()
    

    mouse_x,mouse_y=pygame.mouse.get_pos()    
    pygame.display.flip()

pygame.quit()
sys.exit()