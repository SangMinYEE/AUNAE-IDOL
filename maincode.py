import pygame
import sys
import time 

pygame.init() # 초기화
screen_width=800
screen_height=600

# 창 화면
width, height = 800, 600
screen = pygame.display.set_mode((screen_width,screen_height))
background_image = pygame.image.load("D:/python응용/pygame/start_back_ground.png")
Clock = pygame.time.Clock()

#노래 불러오기


# 이미지의 사각 영역 가져오기
image_rect = background_image.get_rect()

# 이미지의 높이와 넓이 얻기
image_width = image_rect.width
image_height = image_rect.height

pygame.display.set_caption("리듬게임")

white = (255, 255, 255) # 배경색
black = (0, 0, 0)

font = pygame.font.Font("D:/python응용/pygame/NeoDunggeunmoPro-Regular.ttf", 30)

# 시작 버튼 이미지 
start_button_path="D:/python응용/pygame/button_start.png"
start_button_image=pygame.image.load(start_button_path)
button_width,button_height=start_button_image.get_size()
st_button_x, st_button_y=(305-160,300)

# 질문 버튼 이미지 
question_button_path="D:/python응용/pygame/button_question.png"
question_button_image=pygame.image.load(question_button_path)
button_width,button_height=question_button_image.get_size()
qu_button_x, qu_button_y=(305+150,296)

# 클릭 말풍선 이미지 
click_image_path="D:\python응용\pygame\click.png"
click_image=pygame.image.load(click_image_path)
cilck_width,click_height=click_image.get_size()

st_click_button_x,st_click_button_y=(1000,1000)
qu_click_button_x,qu_click_button_y=(1000,1000)

# 시작화면 함수
def start_screen():
    x=0 #화면 루프 변수 
    
    background_image = pygame.image.load("D:\python응용\pygame\start_back_ground.png")  # 실제 이미지 파일 경로로 대체해
    background_image = pygame.transform.scale(background_image, (width, height))
    screen.blit(background_image, (0, 0))


    # x가 image_width 보다 작아지면 화면을 새로 그림 
    

        # 화면 두개를 겹쳐서 화면이 이어져 있는것처럼 그림 

# 어두운 배경스타일 >> 흰색 폰트  

# rect 사각영역 가져옴 pygame의 메서드 객체의 크기 위치 얻음
# pygame 이용할 만한 메서드 정리  

    

    
    # 버튼을 그림
    screen.blit(start_button_image, (st_button_x, st_button_y))
    screen.blit(question_button_image, (qu_button_x, qu_button_y))
    

    text = font.render("리듬게임제목", True, white) # 시작화면 텍스트 렌더링
    # get_rext  해당 객체의 Rectangle(사각영역)을 반환 
    text_rect = text.get_rect(center=(width // 2, height // 2  -150))
    screen.blit(text, text_rect)

    start_button_rect=draw_button("시작",(305-65,437-100))
    question_button_rect=draw_button("설명하기",(550,437-100))

    pygame.display.update() # 화면 업뎃


    while True:
        for event in pygame.event.get(): # 이벤트에 있는 모든 이벤트 가져옴
            if event.type == pygame.QUIT: # 이벤트 타입이 윈도우 닫기 이벤트인지 확인
                pygame.quit()
                sys.exit()
            elif event.type==pygame.MOUSEBUTTONDOWN:
                # 이벤트 타입이 마우스버튼을 누르기 이벤트인지 확인 
                if start_button_rect.collidepoint(event.pos):

                    # 주어진 좌표가 rect영역에 있는지 확인 
                    # 마우스 버튼이 눌린 위치가 시작버튼 영역안에 있는지 확인 
                    return "next_start_game" # next를 반환 
                if question_button_rect.collidepoint(event.pos):
                    return "next_question"
        mouse_x,mouse_y=pygame.mouse.get_pos()
        # count가 1일때는 click 버튼을 나오게 함
        # count가 0일때는 click이 사라지게함 
        if start_button_rect.collidepoint(mouse_x,mouse_y):
        # 클릭 사진 나타남  
            screen.blit(click_image,(st_click_button_x-725,st_click_button_y-730))
          
        '''
        #시작버튼위에 커서가 있을때
            count 1증가시킴   
        #없을때
            count를 0으로 만든다
            >> count가 0이되면 click 사진을 지우기  
        '''

        # 시작버튼위에 커서가 있을때 click뜨게 함
        pygame.display.update()

                

# 시작 버튼 다음 화면
# 시작 배경음악 있어야 하나..?
# 시작 누르고 다음화면으로 넘어가서 음악고르는 화면
 

def next_start_screen():
# 게임 선택 배경화면 
    background_image = pygame.image.load("D:/python응용/pygame/next_back_grond.jpg")  # 실제 이미지 파일 경로로 대체해
    background_image = pygame.transform.scale(background_image, (width, height))
    screen.blit(background_image, (0, 0))

    return_button_rect=draw_button("<< back",(125,45))


    pygame.draw.rect(screen,(225,225,255),[50,110,320,270])

    music_albom_path="D:/python응용/pygame/music_albom_picture.png"
    music_albom_image=pygame.image.load(music_albom_path)
    music_albom_width,music_albom_height=music_albom_image.get_size()
    music_albom_x, music_albom_y=(60,120)

    music_choice=draw_button("music",(203,90))
    stage1_name=draw_button("<stage1>",(203,410))
    stage1_music=draw_button("-The Way to You-",(203,450))

    game_start_button_path = "D:/python응용/pygame/button_question_copy.png"
    game_start_button = pygame.image.load(game_start_button_path)
    game_start_button_width, game_start_button_height = game_start_button.get_size()
    screen.blit(game_start_button, (123, 480))

    game_start_button_rect=draw_button("start!",(203,515))

    screen.blit(music_albom_image, (music_albom_x,music_albom_y))

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==pygame.MOUSEBUTTONDOWN:
                if return_button_rect.collidepoint(event.pos):
                    return "start"
        mouse_x,mouse_y=pygame.mouse.get_pos()

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
    button_image = font.render(text, True, (0, 0, 0))
    button_rect = button_image.get_rect(center=position)
    screen.blit(button_image, button_rect)
    return button_rect # 꼭 반환시켜야함

current_state = start_screen()
next_state= next_start_screen() # 시작화면 표시 

running = True # True로 초기화
while running:
    for event in pygame.event.get(): # 사용자의 입력을 감지하고 동작처리
        if event.type == pygame.QUIT: # quit를 감지>> running을 False로 설정
            running = False

    if current_state == "next_start_game":
        next_start_screen()
    if current_state=="next_question":
        next_question_screen()

    if next_state=="start":
        start_screen()

    mouse_x,mouse_y=pygame.mouse.get_pos()


    
    pygame.display.flip()

pygame.quit()
sys.exit()
