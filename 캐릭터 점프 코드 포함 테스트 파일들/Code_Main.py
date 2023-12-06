import pygame, sys,random,time

screen_width = 1600
screen_height = 900

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue =(0,0,255)

pygame.init()

#스크린
pygame.display.set_caption("파이썬 리듬게임")
screen = pygame.display.set_mode((screen_width,screen_height))
background_image = pygame.image.load("background.png")
Clock = pygame.time.Clock()

#노래 불러오기
#bg_sound = pygame.mixer.Sound("lofi_chill.ogg")
#game_sound = pygame.mixer.Sound("AcousticBeat.ogg")

# 이미지의 사각 영역 가져오기
image_rect = background_image.get_rect()

# 이미지의 높이와 넓이 얻기
image_width = image_rect.width
image_height = image_rect.height

#버튼 이미지 불러오기
go_button_image = pygame.image.load("go.png")
back_button_image = pygame.image.load("back.png")

#버튼이미지의 높이와 넓이 얻기

back_button_rect = back_button_image.get_rect(topleft=(0, 0))
go_button_rect = go_button_image.get_rect(topleft=(300,300))

#노트(장애물) 크기
note_width = 50
note_height = 50
note_speed = 1
note_array = [1,1,1,1,1,1,1,1,1,1,1,1,1,1]

#캐릭터 설정
character_width = 50
character_height = 50
character_x = screen_width // 2 - character_width // 2 # 캐릭터 왼쪽 모서리 X좌표
character_y = screen_height - character_height # 캐릭터 윗쪽 모서리 Y좌표
#점프 확인 & fghj 점프 확인 부울 타입
character_jump = False

f_jump = False
g_jump = False
h_jump = False
j_jump = False
#점프 시 캐릭터가 10,9,8,...-8,-9,-10으로 움직임
default_count = 10
jump_count = default_count

###################### 0. 가장 첫번째 화면 출력###################
def mainMenu():
    #배경음악 시작
    #bg_sound.play(-1)
    global state,start_button,explain_game
    screen.fill(white)
    start_button = pygame.draw.rect(screen,red,[500,300,600,100])
    explain_game = pygame.draw.rect(screen,blue,[500,600,600,100])
    state = "start_screen"
    pygame.display.flip()
###################################################################

############ 1-1게임 대기 화면 || 빨간 버튼 클릭 시, 게임 화면에서 뒤로가기 클릭시 화면###############
def gameStart():
    #배경음 멈추기
    #if bg_sound.play(-1):
     #   bg_sound.stop()
    global state
    screen.fill(blue)
    screen.blit(back_button_image,[0,0])
    screen.blit(go_button_image,[300,300])
    state = "choose_mode"
    pygame.display.flip()
################################################################################

#########################1-2게임 설명 화면 || 파란버튼 클릭시 화면##################
def gameExplain():
    #배경음 멈추기
    #if bg_sound.play(-1):
        #bg_sound.stop()
    global state
    screen.fill(green)
    screen.blit(back_button_image,[0,0])
    state = "explanation"
    pygame.display.flip()
#################################################################

#변수 초기화
red_note = pygame.Rect(screen_width - note_width, random.randint(0, screen_height - note_height), note_width, note_height)
start_time=0
x=0 #화면 루프 변수


##########################2 게임 플레이 화면#############################
def gameMode():
    global state,x,character_jump,character_y,jump_count,start_time,red_note,f_jump,g_jump,h_jump,j_jump
    #시간측정
    elapsed_time = time.time() - start_time

    # x가 image_width보다 작아지면 화면을 새로 그림(루프)
    if(x<=-image_width):
        x=0
    
    #화면 두개를 겹쳐서 화면이 이어져 있는 것처럼 그림
    screen.blit(background_image,[x,0])
    screen.blit(background_image,[x+image_width,0])
    
    #뒤로가기 버튼
    screen.blit(back_button_image,[0,0])
    x-=5
    #################################### 점프 #####################################
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
                character_y -= (jump_count ** 3) * 0.2
                jump_count -= 1
            
            elif jump_count >= 0 :
                character_y -= (jump_count ** 3) * 0.2
                jump_count -= 1
            
            else:
                character_jump = False
                g_jump = False
                jump_count = default_count         
        #h 눌렀을 때 점프 스타일
        elif (h_jump == True):
            if jump_count >= -default_count and jump_count < 0:
                character_y -= (jump_count ** 3)*0.25
                jump_count -= 1
        
            elif jump_count >= 0 :
                character_y -= (jump_count ** 3)*0.25
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

###################################점프 끝#####################################    
    #캐릭터 그리기
    char_rect = pygame.draw.rect(screen, red, (character_x, character_y, character_width, character_height))

    #######장애물 그리기#######
    #장애물 생성
    if elapsed_time>=2:
        red_note = pygame.Rect(screen_width - note_width,  screen_height - note_height, note_width, note_height)
        start_time = time.time()
    #장애물 이동
    for i in range(len(note_array)):    
        pygame.draw.rect(screen, green, red_note)
        red_note.x -= note_speed #노트 오른쪽에서 왼쪽으로 이동
    #충돌발생코드
    if char_rect.colliderect(red_note):
        print("충돌하였습니다.")
    #현재상태
    state = "game_mode"
    pygame.display.flip()
#################################################################################



#시작화면 그리기
mainMenu()




############################무한 반복#########################
while True:
    global state,start_button,explain_game
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            #빨간 버튼 눌렀을 때 화면출력 (게임시작)
            if state == "start_screen" and start_button.collidepoint(event.pos):
                gameStart()

            #파란 버튼 눌렀을 때 화면출력
            elif state == "start_screen" and explain_game.collidepoint(event.pos):
                gameExplain()
            #뒤로 가기 버튼 눌렀을 때 현재 화면 상태에 따라 메인메뉴냐 게임시작화면이냐를 결정
            elif state != "start_screen" and back_button_rect.collidepoint(event.pos):
                if state == "choose_mode" or state == "explanation":
                    mainMenu()
                elif state == "game_mode":
                    gameStart()
                    x=0
            #게임시작 화면에서 버튼 클릭시 게임을 시작        
            elif state == "choose_mode" and go_button_rect.collidepoint(event.pos):
                #game_sound.play(-1)
                gameMode()
    
    #게임 모드 상태일 때 게임을 루핑한다.
    if state == "game_mode":
        gameMode()
    
        
        
        
    Clock.tick(60)
    
    