import pygame
import sys
import os
# 초기화
pygame.init()

# 화면 설정
screen = pygame.display.set_mode((800, 900))
pygame.display.set_caption("타자 연습 프로그램")

# 색상 설정
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (200, 200, 200)
RED = (255,0,0)
BLUE = (0, 0, 255)
# 폰트 설정
font_size = 24
# 폰트 설정
font = pygame.font.Font(None, 36)

# 연습할 문장
'''
sentence = """dic = {'STRAWBERRY':0,'BANANA':0,'LIME':0,'PLUM':0}\n
N = int(input())\n
for i in range(N):\n
	\tfruit,num = input().split()\n
	\tdic[fruit] += int(num)\n
check=0\n
for key,value in dic.items():\n
    \tif value==5:\n
        \t\tcheck=1\n
        \t\tbreak\n
if check==1:\n
    \tprint("YES")\n
else:\n
    \tprint("NO")\n"""
'''
sentence = """dic = {'STRAWBERRY':0,'BANANA':0,'LIME':0,'PLUM':0}
N = int(input())
for i in range(N):
	fruit,num = input().split()
	dic[fruit] += int(num)
check=0
for key,value in dic.items():
    if value==5:
        check=1
        break
if check==1:
    print("YES")
else:
    print("NO")"""

sentence_ll = list(sentence)
print(sentence_ll)
typed_text = ""
start_time = None
wpm = 0
current_char = ""
color_text = [1]*len(sentence)
blink = True
blink_time = 0
finished = False
# 메인 루프
running = True
while running:
    current_time = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_BACKSPACE:
                typed_text = typed_text[:-1]
            elif event.key == pygame.K_RETURN:
                typed_text += '\n'
            elif event.key == pygame.K_TAB:
                typed_text += '\t'
            elif event.key == pygame.K_SPACE:
                typed_text += ' '
            elif event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                pass
            else: # 
                if start_time is None: # 처음 키 누를 때, 시작시간 저장
                    start_time = pygame.time.get_ticks()
                typed_text += event.unicode #event 가 유저가 타이핑한 텍스트인데 이걸 unicode 로 바꿔서 text 에 저장!
                current_char = event.unicode
                #입력 텍스트 길이
                input_len = len(typed_text)
                #남은 텍스트
                remaining_text = sentence_ll[input_len:]
                print(input_len,len(sentence))
                
                
                # text 의 color (같으면 검은색0, 틀리면 빨간색2, 미완이면 회색1)
                if input_len <= len(sentence_ll):
                    if current_char == sentence_ll[input_len-1]: #같으면 검은색 (0)
                        color_text[input_len-1] = 0
                    else:
                        color_text[input_len-1] = 2

    if len(typed_text) == len(sentence)+1:
        finished = True
        print("True")
    
    large_font = pygame.font.Font(None, 72)  # 큰 폰트 설정

    if finished:
        finish_surface = large_font.render("FINISH", True, RED)
        screen.blit(finish_surface, ((800 - finish_surface.get_width()) // 2, 800 - finish_surface.get_height() // 2))
        pygame.display.flip()
        pygame.time.delay(2000)  # 2초간 "finish" 문구를 보여줌
        running = False  # 프로그램 종료
    # 화면 그리기
    screen.fill(WHITE)
    
    

    x_offset = 50
    y_offset = 50
    char_width = 12
    line_height = font_size + 10 

    
    #correct_surface = font.render(sentence, True, BLACK)
    #screen.blit(correct_surface, (50, 50))

    for i in range(len(sentence)):
        if sentence[i] == "\n":
            x_offset = 50
            y_offset += line_height
            continue
        color = BLACK if color_text[i] == 0 else RED if color_text[i] == 2 else GREY    
        # 글자 렌더링
        text_surface = font.render(sentence[i], True, color)
        screen.blit(text_surface, (x_offset, y_offset))
        x_offset += char_width
    
    #print(typed_text)
    if current_time - blink_time > 500:
        blink = not blink
        blink_time = current_time

    if blink:
        # 커서 위치 계산
        cursor_x = 50
        cursor_y = 50
        for char in typed_text:
            if char == '\n':
                cursor_x = 50
                cursor_y += line_height
            else:
                cursor_x += char_width
                if cursor_x >= 800 - 50:
                    cursor_x = 50
                    cursor_y += line_height

        pygame.draw.rect(screen, BLUE, (cursor_x, cursor_y, 2, font_size))

    
    '''
    # 입력한 텍스트와 남은 텍스트로 나누기
    input_len = len(typed_text)
    correct_text = typed_text
    remaining_text = sentence[input_len:]

    # 텍스트를 줄 단위로 나누기
    correct_lines = correct_text.split('\n')
    remaining_lines = remaining_text.split('\n')

    y_offset = 50  # 초기 y 위치
    line_height = font_size + 10  # 각 줄 사이의 간격

    for i, (correct_line, remaining_line) in enumerate(zip(correct_lines, remaining_lines)):
        # 진하게 입력한 텍스트 렌더링
        correct_surface = font.render(correct_line, True, BLACK)
        screen.blit(correct_surface, (50, y_offset + i * line_height))
        
        # 남은 텍스트가 있을 경우 희미하게 렌더링
        if remaining_line:
            remaining_surface = font.render(remaining_line, True, GREY)
            screen.blit(remaining_surface, (50 + correct_surface.get_width(), y_offset + i * line_height))

    # 남은 줄을 렌더링
    for j in range(i + 1, len(remaining_lines)):
        remaining_surface = font.render(remaining_lines[j], True, GREY)
        screen.blit(remaining_surface, (50, y_offset + (j * line_height)))
'''
    # 화면 업데이트
    pygame.display.flip()



# 종료
pygame.quit()
sys.exit()
