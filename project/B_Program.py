import pygame
from Parent import *
import sys
from datetime import datetime
import db
import time

# 데이터베이스 연결
conn = db.create_connection()



class Program(Screen):
    def draw(self):
        self.screen.fill(WHITE)
        draw_text('Start Program practice', font, BLACK, self.screen, 400, 300)
        pygame.display.update()
class Play:
    def run(self):
        correct_cnt = 0
        current = datetime.now()
        session_start_time = current.strftime("%Y-%m-%d %H:%M:%S")
        sTime = time.time() 
        key_data = {}
        total_keystrokes = 0
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
        font = pygame.font.Font(None, 24)

        #font_path = os.path.join(os.path.dirname(__file__), "NANUMGOTHIC.TTF")
        #font = pygame.font.Font(font_path, 20)

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
                                correct_cnt += 1
                            else:
                                color_text[input_len-1] = 2
            tmp_total_keystrokes = len(typed_text)
            tmp_correct_cnt = correct_cnt
            tmp_elapsed_time = (time.time()-sTime)/60

            if tmp_total_keystrokes==0:
                real_accuracy = 0
            else:
                real_accuracy = (tmp_correct_cnt/tmp_total_keystrokes)*100
            real_wpm = (tmp_total_keystrokes/5)/tmp_elapsed_time
            
            # 하단 좌측에 출력할 텍스트 좌표
            left_bottom_x = 20
            left_bottom_y = screen.get_height() - 40  

            # 하단 우측에 출력할 텍스트 좌표
            right_bottom_x = screen.get_width() - 200  
            right_bottom_y = screen.get_height() - 40  

            
  

            if len(typed_text) == len(sentence)+1:
                total_keystrokes = len(typed_text)
                finished = True
                print("True")
            
            #large_font = pygame.font.Font(font_path, 72)
            large_font = pygame.font.Font(None, 72)  # 큰 폰트 설정

            if finished:
                finish_surface = large_font.render("FINISH", True, RED)
                screen.blit(finish_surface, ((800 - finish_surface.get_width()) // 2, 800 - finish_surface.get_height() // 2))
                pygame.display.flip()
                pygame.time.delay(2000)  # 2초간 "finish" 문구를 보여줌
                running = False  # 프로그램 종료
            # 화면 그리기
            screen.fill(WHITE)
            # Real Accuracy 텍스트 생성
            accuracy_text = font.render("Real Accuracy: {:.2f}%".format(real_accuracy), True, BLACK)
            # Real Accuracy 텍스트 화면에 표시 (하단 좌측)
            screen.blit(accuracy_text, (left_bottom_x, left_bottom_y))

            # Real WPM 텍스트 생성
            wpm_text = font.render("Real WPM: {:.2f}".format(real_wpm), True, BLACK)
            # Real WPM 텍스트 화면에 표시 (하단 우측)
            screen.blit(wpm_text, (right_bottom_x, right_bottom_y))
            

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

            # 화면 업데이트
            pygame.display.flip()
        elapsed_time = (time.time() - sTime)/60
        accuracy = (correct_cnt/total_keystrokes)*100
        wpm = (total_keystrokes/5)/elapsed_time
        print(session_start_time, total_keystrokes, correct_cnt,elapsed_time,accuracy,wpm)
        ## DB에 insert 할것.


        return "main_screen"
        # 종료
        #pygame.quit()
        #sys.exit()


if __name__ == "__main__":
    app = Play()
    app.run()