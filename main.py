
#abbahagy: level 4 kész, győzelem kész
#megcsinálni:
#új szinthez: pálya rajzolás- 1.meghívás, 2.csinálás, 3.game over ellenőrzés, 4.level vége ell., 5.kaja helye,

import pygame
import random

pygame.init()

fps_clock = pygame.time.Clock()

screen_width = 400
screen_height = 440

screen = pygame.display.set_mode((screen_width, screen_height))

font = pygame.font.SysFont(None, 40)
win_font = pygame.font.SysFont(None, 80)

#színek
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
black = (0, 0, 0)
body_inner = (50,175,25)
body_outer = (100,100,200)
bg1 = (200,180,120)
bg2 = (160,140,80)
bg3 = (120,100,60)
bg4 = (80,70,50)

#változók
fps = 12
score = 0
level = 1
cell_size = 10
line_place = 40
direction = 0
clicked = False
start = False
game_over = False
between_lvl = False

new_food = True
nums = [1,2,4]
food_pos = [0,0]

win = False
win_level = 5

level1_end = 2
level2_end = 2
level3_end = 2
level4_end = 2

#négyzetek
    #csinál egy négyzetet
start_rect = pygame.Rect(screen_width/2-90, 60, 180, 90)
play_again_rect = pygame.Rect(screen_width/2-90, 110, 180, 90)
next_level_rect = pygame.Rect(screen_width/2-90, 120, 180, 90)

level2rect1 = pygame.Rect(80, 80, 238, cell_size)
level2rect2 = pygame.Rect(80, 330, 238, cell_size)

level3rect1 = pygame.Rect(60, 80, 80, cell_size)
level3rect2 = pygame.Rect(60, 80, cell_size, 80)
level3rect3 = pygame.Rect(260, 80, 80, cell_size)
level3rect4 = pygame.Rect(340, 80, cell_size, 80)
level3rect5 = pygame.Rect(60, 360, 80, cell_size)
level3rect6 = pygame.Rect(60, 280, cell_size, 80)
level3rect7 = pygame.Rect(260, 360, 80, cell_size)
level3rect8 = pygame.Rect(340, 280, cell_size, 90)
level3rect9 = pygame.Rect(190, 80, cell_size, 280)
level3rect10 = pygame.Rect(60, 210, 280, cell_size)

level4rect1 = pygame.Rect(30, 70, 340, 10)
level4rect2 = pygame.Rect(30, 100, 340, 10)
level4rect3 = pygame.Rect(30, 130, 340, 10)
level4rect4 = pygame.Rect(30, 160, 340, 10)
level4rect5 = pygame.Rect(30, 190, 340, 10)
level4rect6 = pygame.Rect(30, 220, 340, 10)
level4rect7 = pygame.Rect(30, 250, 340, 10)
level4rect8 = pygame.Rect(30, 280, 340, 10)
level4rect9 = pygame.Rect(30, 310, 340, 10)
level4rect10 = pygame.Rect(30, 340, 340, 10)
level4rect11 = pygame.Rect(30, 370, 340, 10)
level4rect12 = pygame.Rect(30, 400, 340, 10)

#kező kígyó helyei
snake_pos = [
    [int(screen_width/2), int(screen_height/2)],
    [int(screen_width/2), int(screen_height/2)+cell_size],
    [int(screen_width/2), int(screen_height/2)+cell_size*2],
    [int(screen_width/2), int(screen_height/2)+cell_size*3]
]


#start gomb csinálás
def draw_start():
    star_text = 'Start'
    # négyzet rajzol: hova, milyen színű, melyik négyzetet
    pygame.draw.rect(screen, red, start_rect)
    # csinál egy képet szöveggel: szöveg, ..., milyen színű legyen a kép
    start_img = font.render(star_text, True, black)
    # felrakja a képet
    screen.blit(start_img, (screen_width/2-30, 90))


#level 1: pálya és score felirat megrajzolása
def draw_lvl1(color, score):
    # kiszínezi egy színnel
    screen.fill(color)

    # létrehozza a szöveget az adatokkal
    lvl_text = f'lvl1: collect {level1_end} berries ({level1_end}/{score})'
    lvl_img = font.render(lvl_text, True, black)
    screen.blit(lvl_img, (5, 10))


#level 2: pálya és score felirat megrajzolása
def draw_lvl2(color, score):
    screen.fill(color)

    #pálya plusz vonalai
    pygame.draw.rect(screen, black, level2rect1)
    pygame.draw.rect(screen, black, level2rect2)

    lvl_text = f'lvl{level}: collect {level2_end} berries ({level2_end}/{score})'
    lvl_img = font.render(lvl_text, True, black)
    screen.blit(lvl_img, (5, 10))


#level 3: pálya és score felirat megrajzolása
def draw_lvl3(color, score):
    screen.fill(color)

    lvl_text = f'lvl{level}: collect {level3_end} berries ({level3_end}/{score})'
    lvl_img = font.render(lvl_text, True, black)
    screen.blit(lvl_img, (5, 10))

    pygame.draw.rect(screen, black, level3rect1)
    pygame.draw.rect(screen, black, level3rect2)
    pygame.draw.rect(screen, black, level3rect3)
    pygame.draw.rect(screen, black, level3rect4)
    pygame.draw.rect(screen, black, level3rect5)
    pygame.draw.rect(screen, black, level3rect6)
    pygame.draw.rect(screen, black, level3rect7)
    pygame.draw.rect(screen, black, level3rect8)
    pygame.draw.rect(screen, black, level3rect9)
    pygame.draw.rect(screen, black, level3rect10)


#level 4: pálya és score felirat megrajzollás
def draw_lvl4(color, score):
    screen.fill(color)

    lvl_text = f'lvl{level}: collect {level4_end} berries ({level4_end}/{score})'
    lvl_img = font.render(lvl_text, True, black)
    screen.blit(lvl_img, (5, 10))

    pygame.draw.rect(screen, black, level4rect1)
    pygame.draw.rect(screen, black, level4rect2)
    pygame.draw.rect(screen, black, level4rect3)
    pygame.draw.rect(screen, black, level4rect4)
    pygame.draw.rect(screen, black, level4rect5)
    pygame.draw.rect(screen, black, level4rect6)
    pygame.draw.rect(screen, black, level4rect7)
    pygame.draw.rect(screen, black, level4rect8)
    pygame.draw.rect(screen, black, level4rect9)
    pygame.draw.rect(screen, black, level4rect10)
    pygame.draw.rect(screen, black, level4rect11)
    pygame.draw.rect(screen, black, level4rect12)


#kígyó megrajzolás
def draw_snake():
    head = 1
    for x in snake_pos:
        if head == 0:
            # megrajzolja a nagy négyzetet
            pygame.draw.rect(screen, body_outer, (x[0], x[1], cell_size, cell_size))
            # a nagy négyzetbe belerakja a kicsit. Eltolja egyel, és kisebb lesz kettővel
            pygame.draw.rect(screen, body_inner, (x[0]+1, x[1]+1, cell_size-2, cell_size-2))
        if head == 1:
            # megrajzolja a fejet
            pygame.draw.rect(screen, red, (x[0], x[1], cell_size, cell_size))
            head = 0


#játék vége ellenőrzése
def check_game_over(game_over):
    # megnézi hogy kiment e a pályáról
    if snake_pos[0][0] < 0 or snake_pos[0][0] > screen_width-cell_size or snake_pos[0][1] < line_place or snake_pos[0][1] > screen_height-cell_size:
        game_over = True

    # megnézi hogy magába ment e a kígyó
    head = 0
    for x in snake_pos:
        if x == snake_pos[0] and head >0:
            game_over = True
        head += 1

    # szintenként megnézi hogy nem ér e hozzá a vonalakhoz
    if level == 2:
        if snake_pos[0][0] >= 80 and snake_pos[0][0] <= 318 and (snake_pos[0][1] == 80 or snake_pos[0][1] == 330):
            game_over = True
    if level == 3:
        if level3rect1.collidepoint(snake_pos[0]) or level3rect2.collidepoint(snake_pos[0]) or \
                level3rect3.collidepoint(snake_pos[0]) or level3rect4.collidepoint(snake_pos[0]) or \
                level3rect5.collidepoint(snake_pos[0]) or level3rect6.collidepoint(snake_pos[0]) or \
                level3rect7.collidepoint(snake_pos[0]) or level3rect8.collidepoint(snake_pos[0]) or \
                level3rect9.collidepoint(snake_pos[0]) or level3rect10.collidepoint(snake_pos[0]):
            game_over = True
    if level == 4:
        if level4rect1.collidepoint(snake_pos[0]) or level4rect2.collidepoint(snake_pos[0]) or \
                level4rect3.collidepoint(snake_pos[0]) or level4rect4.collidepoint(snake_pos[0]) or \
                level4rect5.collidepoint(snake_pos[0]) or level4rect6.collidepoint(snake_pos[0]) or \
                level4rect7.collidepoint(snake_pos[0]) or level4rect8.collidepoint(snake_pos[0]) or \
                level4rect9.collidepoint(snake_pos[0]) or level4rect10.collidepoint(snake_pos[0]) or \
                level4rect11.collidepoint(snake_pos[0]) or level4rect12.collidepoint(snake_pos[0]):
            game_over = True

    return game_over


#game over szöveg és play again gomb rajzolása
def draw_game_over():
    game_over_text = 'Game over!'
    pygame.draw.rect(screen, red, (int(screen_width/2-90),int(screen_height/2),180,90))
    game_over_img = font.render(game_over_text, True, black)
    screen.blit(game_over_img, (int(screen_width/2)-80, int(screen_height/2)+30))

    play_again_text = 'Play again?'
    pygame.draw.rect(screen, red, play_again_rect)
    play_again_img = font.render(play_again_text, True, black)
    screen.blit(play_again_img, (int(screen_width/2)-80, 140))


#megnézi, hogy level vége van e
def check_level_end():
    global between_lvl
    global win
    if score == level1_end and level == 1:
        between_lvl = True
    if score ==  level2_end and level == 2:
        between_lvl = True
    if score == level3_end and level == 3:
        between_lvl = True
    if score == level4_end and level == 4:
        between_lvl = True
        win = True


#megrajzolja a level complete és a next level feliratot
def draw_next_level():
    game_over_text = 'Level completed!'
    pygame.draw.rect(screen, red, (int(screen_width / 2 - 130), int(screen_height / 2), 250, 90))
    game_over_img = font.render(game_over_text, True, black)
    screen.blit(game_over_img, (int(screen_width / 2) - 120, int(screen_height / 2) + 30))

    next_level_text = 'Next level'
    pygame.draw.rect(screen, red, next_level_rect)
    next_level_img = font.render(next_level_text, True, black)
    screen.blit(next_level_img, (int(screen_width / 2 + 50) - 120, 150))


#győzelem ellenőrzés
def draw_win():
    # leírás a draw_start-ban
    game_over_text = 'You won!'
    pygame.draw.rect(screen, red, (int(screen_width / 2 - 130), int(screen_height / 2-80), 250, 90))
    game_over_img = win_font.render(game_over_text, True, black)
    screen.blit(game_over_img, (int(screen_width / 2) - 130, int(screen_height / 2) - 60))


run = True
while run:
    fps_clock.tick(fps)

    if level == 1:
        draw_lvl1(bg1, score)
    if level == 2:
        draw_lvl2(bg2, score)
    if level == 3:
        draw_lvl3(bg3, score)
    if level == 4:
        draw_lvl4(bg4, score)
    # rajzol egy vonalat az adatok alá
    pygame.draw.line(screen, black, (0, line_place), (screen_width, line_place), 2)

    #kilépés és direction megadás
    # lekéri az eventeket és ezen megy végig
    for event in pygame.event.get():
        # ha X-re kattintunk, akkor a run false lesz
        if event.type == pygame.QUIT:
            run = False
        # megnézi hogy egy gomb nyomva van e
        if event.type == pygame.KEYDOWN:
            # megnézi hogy melyik gomb van lenyomva, és hogy nehogy magába vissza forduljon
            if event.key == pygame.K_UP and direction != 3 and snake_pos[0][1]-cell_size != snake_pos[1][1]:
                direction = 1
            if event.key == pygame.K_DOWN and direction != 1 and snake_pos[0][1]+cell_size != snake_pos[1][1]:
                direction = 3
            if event.key == pygame.K_RIGHT and direction != 4 and snake_pos[0][0]+cell_size != snake_pos[1][0]:
                direction = 2
            if event.key == pygame.K_LEFT and direction != 2 and snake_pos[0][0]-cell_size != snake_pos[1][0]:
                direction = 4

    #új kaja helyánek megadása
    if new_food:
        # megadja minden szintnek külön, hogy hol lehet és lesz a kaja
        if level == 1:
            food_pos[0] = cell_size * random.randint(0, int(screen_width/cell_size-1))
            food_pos[1] = cell_size * random.randint(int(line_place/cell_size), int(screen_height/cell_size-1))
            new_food = False
        if level == 2:
            food_pos[0] = cell_size * random.randint(0, int(screen_width / cell_size - 1))
            food_pos[1] = cell_size * random.randint(int(line_place / cell_size), int(screen_height / cell_size - 1))
            # addig marad a while ciklusokban amíg nem falon lesz a kaja
            while new_food:
                # a collidepoint azt nézi hogy érintkezik e
                if level2rect1.collidepoint(food_pos) or level2rect2.collidepoint(food_pos):
                    food_pos[0] = cell_size * random.randint(0, int(screen_width / cell_size - 1))
                    food_pos[1] = cell_size * random.randint(int(line_place / cell_size), int(screen_height / cell_size - 1))
                else:
                    new_food = False
        if level == 3:
            food_pos[0] = cell_size * random.randint(0, int(screen_width / cell_size - 1))
            food_pos[1] = cell_size * random.randint(int(line_place / cell_size), int(screen_height / cell_size - 1))
            while new_food:
                if level3rect1.collidepoint(food_pos) or level3rect2.collidepoint(food_pos) or \
                level3rect3.collidepoint(food_pos) or level3rect4.collidepoint(food_pos) or \
                level3rect5.collidepoint(food_pos) or level3rect6.collidepoint(food_pos) or \
                level3rect7.collidepoint(food_pos) or level3rect8.collidepoint(food_pos) or \
                level3rect9.collidepoint(food_pos) or level3rect10.collidepoint(food_pos):
                    food_pos[0] = cell_size * random.randint(0, int(screen_width / cell_size - 1))
                    food_pos[1] = cell_size * random.randint(int(line_place / cell_size), int(screen_height / cell_size - 1))
                else:
                    new_food = False
        if level == 4:
            food_pos[0] = cell_size * random.randint(0, int(screen_width / cell_size - 1))
            food_pos[1] = cell_size * random.randint(int(line_place / cell_size), int(screen_height / cell_size - 1))
            while new_food:
                if level4rect1.collidepoint(food_pos) or level4rect2.collidepoint(food_pos) or \
                level4rect3.collidepoint(food_pos) or level4rect4.collidepoint(food_pos) or \
                level4rect5.collidepoint(food_pos) or level4rect6.collidepoint(food_pos) or \
                level4rect7.collidepoint(food_pos) or level4rect8.collidepoint(food_pos) or \
                level4rect9.collidepoint(food_pos) or level4rect10.collidepoint(food_pos) or \
                level4rect11.collidepoint(food_pos) or level4rect12.collidepoint(food_pos):
                    food_pos[0] = cell_size * random.randint(0, int(screen_width / cell_size - 1))
                    food_pos[1] = cell_size * random.randint(int(line_place / cell_size), int(screen_height / cell_size - 1))
                else:
                    new_food = False
    # megrajzolja a kaját az adott pozícióba
    pygame.draw.rect(screen, red, (food_pos[0], food_pos[1], cell_size, cell_size))

    #kaja megevés megoldás
    # megnézi hogy megettük e a kaját, és ha igen akkor rajzol egy új testrészt
    if snake_pos[0] == food_pos:
        new_food = True
        score += 1
        new_piece = [0,0]
        if direction == 1:
            new_piece[0] = snake_pos[-1][0]
            new_piece[1] = snake_pos[-1][1]+cell_size
        if direction == 3:
            new_piece[0] = snake_pos[-1][0]
            new_piece[1] = snake_pos[-1][1]-cell_size
        if direction == 2:
            new_piece[0] = snake_pos[-1][0]+cell_size
            new_piece[1] = snake_pos[-1][1]
        if direction == 1:
            new_piece[0] = snake_pos[-1][0]-cell_size
            new_piece[1] = snake_pos[-1][1]
        # hozzá adja az új testrészt
        snake_pos.append(new_piece)

    if win:
        draw_win()

    game_over = check_game_over(game_over)

    #game over esetén újra indítás
    if game_over:
        draw_game_over()
        # megnézi hogy kattintottunk e valahova
        if event.type == pygame.MOUSEBUTTONDOWN and not clicked:
            clicked = True
        if event.type == pygame.MOUSEBUTTONUP and clicked:
            clicked = False
            # lekéri a kattintás pozicíóját, és listában tárolja
            pos = pygame.mouse.get_pos()
            # megnézi, hogy a play again-re nyomtunk e
            if play_again_rect.collidepoint(pos) and game_over:
                # ha arra nyomtunk, akkor vissza állít mindent a kezdő állásba
                snake_pos = [
                    [int(screen_width / 2), int(screen_height / 2)],
                    [int(screen_width / 2), int(screen_height / 2) + cell_size],
                    [int(screen_width / 2), int(screen_height / 2) + cell_size * 2],
                    [int(screen_width / 2), int(screen_height / 2) + cell_size * 3]
                ]
                score = 0
                direction = 0
                start = False
                game_over = False
                new_food = True
                between_lvl = False
                level = 1

    # amíg nem vagyünk két szint között, addig ellenőrzi
    if not between_lvl:
        check_level_end()

    if between_lvl and not win:
        draw_next_level()

    #elindítja a következő levelt ha a gombra megyünk
    if between_lvl:
        if event.type == pygame.MOUSEBUTTONDOWN and not clicked:
            clicked = True
        if event.type == pygame.MOUSEBUTTONUP and clicked:
            clicked = False
            pos = pygame.mouse.get_pos()
            if next_level_rect.collidepoint(pos):
                if level == 2 or level == 3:
                    snake_pos = [
                        [40, 50],
                        [30, 50],
                        [20, 50],
                        [10, 50]
                    ]
                else:
                    snake_pos = [
                        [int(screen_width / 2), int(screen_height / 2)],
                        [int(screen_width / 2), int(screen_height / 2) + cell_size],
                        [int(screen_width / 2), int(screen_height / 2) + cell_size * 2],
                        [int(screen_width / 2), int(screen_height / 2) + cell_size * 3]
                    ]
                score = 0
                direction = 2
                start = False
                game_over = False
                new_food = True
                between_lvl = False
                level += 1

    #start gomb működése
    if not start:
        draw_start()
        if event.type == pygame.MOUSEBUTTONDOWN and not clicked:
            clicked = True
        if event.type == pygame.MOUSEBUTTONUP and clicked:
            clicked = False
            pos = pygame.mouse.get_pos()
            if start_rect.collidepoint(pos):
                start = True
                if level == 3 or level == 4:
                    direction = 2
                else:
                    direction = random.choice(nums)

    #kígyó mozgatása direction alapján
    if start and not game_over and not between_lvl:
        if direction >= 1:
            snake_pos = snake_pos[-1:] + snake_pos[:-1]
        if direction == 1:
            snake_pos[0][0] = snake_pos[1][0]
            snake_pos[0][1] = snake_pos[1][1] - cell_size
        if direction == 3:
            snake_pos[0][0] = snake_pos[1][0]
            snake_pos[0][1] = snake_pos[1][1] + cell_size
        if direction == 2:
            snake_pos[0][0] = snake_pos[1][0] + cell_size
            snake_pos[0][1] = snake_pos[1][1]
        if direction == 4:
            snake_pos[0][0] = snake_pos[1][0] - cell_size
            snake_pos[0][1] = snake_pos[1][1]

    #csak játék közben rajzolja és ha nem két szint között van
    if start and not between_lvl:
        draw_snake()

    pygame.display.update()

pygame.quit()

