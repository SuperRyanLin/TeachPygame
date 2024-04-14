import random
import pygame
import sys
from pygame.locals import *

# global macros
FPS = 30  # frames per second, the general speed of the program
WINDOWWIDTH = 1080  # size of window's width in pixels
WINDOWHEIGHT = 810  # size of windows' height in pixels

# initial screen
DISPLAYSURF = pygame.display.set_mode(
    (WINDOWWIDTH, WINDOWHEIGHT))  # fullscreen window
info = pygame.display.Info()

# graph = pygame.image.load("圖.jpg") # load image to variable

class BG(pygame.sprite.Sprite):
    def __init__(self, picfilepath):
        self.bg = pygame.image.load(picfilepath)
        self.visible = False  # 預設為不可見
        super().__init__()
        self.rect = self.bg.get_rect()

        w = self.bg.get_width()
        h = self.bg.get_height()
        self.bg = pygame.transform.scale(
            self.bg, (info.current_w, info.current_h))

    def out(self):  # 是否出現
        DISPLAYSURF.blit(self.bg, (0, 0))

    def bye(self):
        self.visible = False

class Picture(pygame.sprite.Sprite):
    def __init__(self, picfilepath):
        self.picture = pygame.image.load(picfilepath)
        self.visible = False  # 預設為不可見
        super().__init__()
        self.rect = self.picture.get_rect()  # self.rect.x #self.rect.y = 123456 指定座標

    def pos(self, posx, posy):
        self.rect.x = posx
        self.rect.y = posy

    def out(self):  # 出現
        DISPLAYSURF.blit(self.picture, (self.rect.x,
                         self.rect.y))

    def bye(self):  # 消失
        self.visible = False

    def size(self, ezis):  # 尺寸
        self.picture = pygame.transform.scale(
            self.picture, (self.picture.get_width() * ezis, self.picture.get_height() * ezis))


"""
群祖名 = pygame.sprite.Group()
群組名.add(圖片名稱)

"""
A_main = BG("C:/Users/s1011/Desktop/自主學習/A/A-main.PNG")
A_1_main = BG("C:/Users/s1011/Desktop/自主學習/A/A-1/A-1-main.PNG")
#A_2_main = BG("C:/Users/s1011/Desktop/自主學習/A/A-2/A-2().PNG")  # 要改
A_3_main = BG("C:/Users/s1011/Desktop/自主學習/A/A-3/A-3-main.PNG")
A_4_main = BG("C:/Users/s1011/Desktop/自主學習/A/A-4/A-4-main.PNG")
A_5_main = BG("C:/Users/s1011/Desktop/自主學習/A/A-5/A-5-main.PNG")
A_6_main = BG("C:/Users/s1011/Desktop/自主學習/A/A-6/A-6-main.PNG")

L_change = Picture("C:/Users/s1011/Desktop/自主學習/IMG_3780.PNG")
R_change = Picture("C:/Users/s1011/Desktop/自主學習/IMG_3781.PNG")
back = Picture("C:/Users/s1011/Desktop/自主學習/IMG_3782.PNG")
tools = Picture("C:/Users/s1011/Desktop/自主學習/A/tools.PNG")
L_change.size(0.27)
R_change.size(0.27)
back.size(0.3)
tools.size(0.27)
R_change.pos(1035, 315)
L_change.pos(15, 315)
back.pos(33, 550)
tools.pos(0, 647)

A_cup = Picture("C:/Users/s1011/Desktop/自主學習/A/A-cup.PNG")
A_closet = Picture("C:/Users/s1011/Desktop/自主學習/A/A-closet.png")
A_cupBl = Picture("C:/Users/s1011/Desktop/自主學習/A/A-cupBL.PNG")
A_down = Picture("C:/Users/s1011/Desktop/自主學習/A/A-down.PNG")
A_mid = Picture("C:/Users/s1011/Desktop/自主學習/A/A-mid.PNG")
A_up = Picture("C:/Users/s1011/Desktop/自主學習/A/A-up.PNG")
A_tele = Picture("C:/Users/s1011/Desktop/自主學習/A/A-tele.PNG")
A_juice = Picture("C:/Users/s1011/Desktop/自主學習/A/A-juice.PNG")
A_juiceBl = Picture("C:/Users/s1011/Desktop/自主學習/A/A-juiceBlood.PNG")
A_cup.pos(533, 314)
A_cupBl.pos(533, 314)  # 沒在A群組裡
A_closet.pos(139, 443)
A_down.pos(707, 447)
A_mid.pos(707, 293)
A_up.pos(705, 143)
A_juice.pos(405, 269)
A_juiceBl.pos(405, 269)  # 沒在A群組裡
A_tele.pos(158, 366)

Aall = pygame.sprite.Group(A_cup, A_cupBl,  A_closet, A_down,
                           A_mid, A_up, A_tele, A_juice, A_juiceBl)
A = pygame.sprite.Group(A_cup, A_closet, A_down,
                        A_mid, A_up, A_tele, A_juice, R_change, L_change)
for x in Aall.sprites():
    x.size(0.27)

A_1_downclose = Picture("C:/Users/s1011/Desktop/自主學習/A/A-1/A-1-dwcl.PNG")
A_1_downopen = Picture("C:/Users/s1011/Desktop/自主學習/A/A-1/A-1-dwop.PNG")
A_1_upclose = Picture("C:/Users/s1011/Desktop/自主學習/A/A-1/A-1-upclose.PNG")
A_1_upopen = Picture("C:/Users/s1011/Desktop/自主學習/A/A-1/A-1-upopen.PNG")
A_1_tipe = Picture("C:/Users/s1011/Desktop/自主學習/A/A-1/A-1-tipe.PNG")
A_1_fire = Picture("C:/Users/s1011/Desktop/自主學習/A/A-1/A-1-fire.PNG")
A_1_upopen.pos(287, 170)
A_1_upclose.pos(287, 170)
A_1_downopen.pos(287, 358)
A_1_downclose.pos(287, 358)
A_1_tipe.pos(450, 410)
A_1_fire.pos(429, 240)

A1all = pygame.sprite.Group(
    A_1_downclose, A_1_downopen, A_1_upclose, A_1_upopen, A_1_tipe, A_1_fire,)
A1 = pygame.sprite.Group(back)

for x in A1all.sprites():
    x.size(0.27)

A_3_cup = Picture("C:/Users/s1011/Desktop/自主學習/A/A-3/A-3-cup.PNG")
A_3_cupBl = Picture("C:/Users/s1011/Desktop/自主學習/A/A-3/A-3-cupB.PNG")
A_3_candle = Picture("C:/Users/s1011/Desktop/自主學習/A/A-3/A-3-candle.PNG")
A_3_hd = Picture("C:/Users/s1011/Desktop/自主學習/A/A-3/A-3-hd.PNG")
A_3_heart = Picture("C:/Users/s1011/Desktop/自主學習/A/A-3/A-3-heart.PNG")
A_3_J = Picture("C:/Users/s1011/Desktop/自主學習/A/A-3/A-3-J.PNG")
A_3_JB = Picture("C:/Users/s1011/Desktop/自主學習/A/A-3/A-3-JB.PNG")
A_3_on = Picture("C:/Users/s1011/Desktop/自主學習/A/A-3/A-3-on.PNG")
A_3_off = Picture("C:/Users/s1011/Desktop/自主學習/A/A-3/A-3-off.PNG")
A_3_tooth = Picture("C:/Users/s1011/Desktop/自主學習/A/A-3/A-3-tooth.PNG")
A_3_cup.pos(627, 243)
A_3_cupBl.pos(627, 243)
A_3_candle.pos(645, 461)
A_3_hd.pos(279, 202)
A_3_heart.pos(317, 205)
A_3_J.pos(181, 87)
A_3_JB.pos(181, 87)
A_3_on.pos(402, 480)
A_3_off.pos(402, 480)
A_3_tooth.pos(345, 361)

A3all = pygame.sprite.Group(A_3_cup, A_3_cupBl, A_3_J, A_3_JB,
                            A_3_candle, A_3_hd, A_3_heart, A_3_on, A_3_off, A_3_tooth)
A3 = pygame.sprite.Group(A_3_cup, A_3_JB, A_3_off, back)

for x in A3all.sprites():
    x.size(0.27)

A_4_B1 = Picture("C:/Users/s1011/Desktop/自主學習/A/A-4/A-4-B1.PNG")
A_4_B2 = Picture("C:/Users/s1011/Desktop/自主學習/A/A-4/A-4-B2.PNG")
A_4_B3 = Picture("C:/Users/s1011/Desktop/自主學習/A/A-4/A-4-B3.PNG")
A_4_close = Picture("C:/Users/s1011/Desktop/自主學習/A/A-4/A-4-close.PNG")
A_4_open = Picture("C:/Users/s1011/Desktop/自主學習/A/A-4/A-4-open.PNG")
A_4_paper = Picture("C:/Users/s1011/Desktop/自主學習/A/A-4/A-4-paper.PNG")
A_4_B1.pos(204, 195)
A_4_B2.pos(396, 193)
A_4_B3.pos(283, 261)
A_4_close.pos(482, 372)
A_4_open.pos(482, 303)
A_4_paper.pos(567, 352)

A4all = pygame.sprite.Group(A_4_B1, A_4_B2, A_4_B3,
                            A_4_close, A_4_open, A_4_paper)
A4 = pygame.sprite.Group(A_4_B1, A_4_B2, A_4_B3, back)

for x in A4all.sprites():
    x.size(0.27)

A_4_1_diary1 = BG("C:/Users/s1011/Desktop/自主學習/A/A-4/A-4-1/diary1.PNG")
A_4_1_diary2 = BG("C:/Users/s1011/Desktop/自主學習/A/A-4/A-4-1/diary2.PNG")
A_4_1_diary3 = BG("C:/Users/s1011/Desktop/自主學習/A/A-4/A-4-1/diary3.PNG")
A_4_1_diary4 = BG("C:/Users/s1011/Desktop/自主學習/A/A-4/A-4-1/diary4.PNG")
A_4_1_right = Picture("C:/Users/s1011/Desktop/自主學習/A/A-4/A-4-1/right.PNG")
A_4_1_left = Picture("C:/Users/s1011/Desktop/自主學習/A/A-4/A-4-1/left.PNG")
A_4_1_right.pos(1014, 66)
A_4_1_left.pos(0, 63)

diary = pygame.sprite.Group(A_4_1_diary1, A_4_1_diary2, A_4_1_diary3, A_4_1_diary4)

A41 = pygame.sprite.Group(A_4_1_right, A_4_1_left)
#背景問題!!!!!!!!!!!
for x in A41.sprites():
    x.size(0.27)

A_6_close = Picture("C:/Users/s1011/Desktop/自主學習/A/A-6/A-6-close.PNG")
A_6_open = Picture("C:/Users/s1011/Desktop/自主學習/A/A-6/A-6-open.PNG")
A_6_paper = Picture("C:/Users/s1011/Desktop/自主學習/A/A-6/A-6-paper.PNG")
A_6_swordB = Picture("C:/Users/s1011/Desktop/自主學習/A/A-6/A-6-sword.PNG")
A_6_close.pos(150, 67)
A_6_open.pos(0, 7)
A_6_paper.pos(594, 463)
A_6_swordB.pos(231, 347)

A6all = pygame.sprite.Group(A_6_close, A_6_open, A_6_paper, A_6_swordB)
A6 = pygame.sprite.Group(back)

for x in A6all.sprites():
    x.size(0.27)

# B背景放這
B_main = BG("C:/Users/s1011/Desktop/自主學習/B/B-main.PNG")
B_1_main = BG("C:/Users/s1011/Desktop/自主學習/B/B-1/B_1_main.PNG")

B_clock = Picture("C:/Users/s1011/Desktop/自主學習/B/B-clock.PNG")
B_closetclose = Picture("C:/Users/s1011/Desktop/自主學習/B/B-closetclose.PNG")
B_closeopen = Picture("C:/Users/s1011/Desktop/自主學習/B/B-closetopen.PNG")
B_doorclose = Picture("C:/Users/s1011/Desktop/自主學習/B/B-doorclose.PNG")
B_dooropen = Picture("C:/Users/s1011/Desktop/自主學習/B/B-dooropen.PNG")
B_hand = Picture("C:/Users/s1011/Desktop/自主學習/B/B-hand.PNG")
B_irondoor = Picture("C:/Users/s1011/Desktop/自主學習/B/B-irondoor.PNG")
B_people = Picture("C:/Users/s1011/Desktop/自主學習/B/B-people.PNG")
# B_photo = Picture("C:/Users/s1011/Desktop/自主學習/B/B-.PNG")
B_swordA = Picture("C:/Users/s1011/Desktop/自主學習/B/B-swordA.PNG")
B_1handL = Picture("C:/Users/s1011/Desktop/自主學習/B/B-1handL.PNG")
B_1handR = Picture("C:/Users/s1011/Desktop/自主學習/B/B-1handR.PNG")
B_1legR = Picture("C:/Users/s1011/Desktop/自主學習/B/B-1legR.PNG")
B_1legL = Picture("C:/Users/s1011/Desktop/自主學習/B/B-1legL.PNG")
B_2handL = Picture("C:/Users/s1011/Desktop/自主學習/B/B-2handL.PNG")
B_2handR = Picture("C:/Users/s1011/Desktop/自主學習/B/B-2handR.PNG")
B_2legR = Picture("C:/Users/s1011/Desktop/自主學習/B/B-2legR.PNG")
B_2legL = Picture("C:/Users/s1011/Desktop/自主學習/B/B-2legL.PNG")
B_3handL = Picture("C:/Users/s1011/Desktop/自主學習/B/B-3handL.PNG")
B_3handR = Picture("C:/Users/s1011/Desktop/自主學習/B/B-3handR.PNG")
B_3legR = Picture("C:/Users/s1011/Desktop/自主學習/B/B-3legR.PNG")
B_3legL = Picture("C:/Users/s1011/Desktop/自主學習/B/B-3legL.PNG")
# B的鏡子部分還沒匯進電腦
B_clock.pos(238, 54)
B_1handL.pos(407, 269)
B_1handR.pos(278, 424)
B_1legL.pos(505, 296)
B_1legR.pos(517, 404)
B_2handL.pos(406, 284)
B_2handR.pos(319, 422)
B_2legL.pos(479, 325)
B_2legR.pos(466, 389)
B_3handL.pos(410, 271)
B_3handR.pos(325, 425)
B_3legL.pos(484, 327)
B_3legR.pos(467, 390)
B_closetclose.pos(174, 526)
B_closeopen.pos(174, 526)
B_doorclose.pos(749, 134)
B_dooropen.pos(749, 134)
B_irondoor.pos(172, 230)
B_people.pos(173, 232)
B_hand.pos(215, 537)
B_swordA.pos(208, 536)

Ball = pygame.sprite.Group(B_swordA, B_clock, B_people, B_3legR, B_3legL, B_3handR, B_3handL, B_2legR, B_2legL, B_2handR, B_2handL, B_1legR,
                           B_1legL, B_1handR, B_1handL, B_closetclose, B_closeopen, B_doorclose, B_dooropen, B_hand, B_irondoor)
B = pygame.sprite.Group(B_clock, R_change, L_change)

for x in Ball.sprites():
    x.size(0.27)

B_1_amra = Picture("C:/Users/s1011/Desktop/自主學習/B/B-1/B_1_amra.PNG")
B_1_BlMir = Picture("C:/Users/s1011/Desktop/自主學習/B/B-1/B_1_BlMir.PNG")
B_1_BlNeck = Picture("C:/Users/s1011/Desktop/自主學習/B/B-1/B_1_BlNeck.PNG")
B_1_fire = Picture("C:/Users/s1011/Desktop/自主學習/B/B-1/B_1_fire.PNG")
B_1_hand = Picture("C:/Users/s1011/Desktop/自主學習/B/B-1/B_1_hand.PNG")
B_1_point = Picture("C:/Users/s1011/Desktop/自主學習/B/B-1/B_1_point.PNG")
B_1_amra.pos(402, 215)
B_1_BlMir.pos(387, 119)
B_1_BlNeck.pos(527, 354)
B_1_fire.pos(594, 337)
B_1_hand.pos(405, 351)
B_1_point.pos(262, 0)

B1all = pygame.sprite.Group(B_1_point, B_1_hand, B_1_fire, B_1_BlNeck, B_1_BlMir, B_1_amra)
B1 = pygame.sprite.Group(B_1_point, back)

for x in B1all.sprites():
    x.size(0.27)

C_main = BG("C:/Users/s1011/Desktop/自主學習/C/C-main.PNG")

C_bloodA = Picture("C:/Users/s1011/Desktop/自主學習/C/C-bloodA.PNG")
C_BloodB = Picture("C:/Users/s1011/Desktop/自主學習/C/C-bloodB.PNG")
C_body = Picture("C:/Users/s1011/Desktop/自主學習/C/C-body.PNG")
C_boxclose = Picture("C:/Users/s1011/Desktop/自主學習/C/C-boxclose.PNG")
C_boxopen = Picture("C:/Users/s1011/Desktop/自主學習/C/C-boxopen.PNG")
C_head = Picture("C:/Users/s1011/Desktop/自主學習/C/C-head.PNG")
C_heart = Picture("C:/Users/s1011/Desktop/自主學習/C/C-heart.PNG")
C_key = Picture("C:/Users/s1011/Desktop/自主學習/C/C-key.PNG")
C_light = Picture("C:/Users/s1011/Desktop/自主學習/C/C-light.PNG")
C_lighton = Picture("C:/Users/s1011/Desktop/自主學習/C/C-lighton.PNG")
C_swordA = Picture("C:/Users/s1011/Desktop/自主學習/C/C-swordA.PNG")
C_swordB = Picture("C:/Users/s1011/Desktop/自主學習/C/C-swordB.PNG")
C_swordC = Picture("C:/Users/s1011/Desktop/自主學習/C/C-swordC.PNG")

Call = pygame.sprite.Group(C_bloodA, C_BloodB, C_body, C_boxclose, C_boxopen,
                           C_head, C_heart, C_key, C_light, C_lighton, C_swordA, C_swordB, C_swordC)
C = pygame.sprite.Group(L_change, R_change)

D_main = BG("C:/Users/s1011/Desktop/自主學習/D/D-main.PNG")
D_1_main = BG("C:/Users/s1011/Desktop/自主學習/D/D-1/D-1-main.PNG")
D_2_main = BG("C:/Users/s1011/Desktop/自主學習/D/D-2/D-2-main.PNG")
D_3_main = BG("C:/Users/s1011/Desktop/自主學習/D/D-3/D-3-main.PNG")
D_4_main = BG("C:/Users/s1011/Desktop/自主學習/D/D-4/D-4-main.PNG")

D_board = Picture("C:/Users/s1011/Desktop/自主學習/D/D-board.PNG")
D_plant = Picture("C:/Users/s1011/Desktop/自主學習/D/D-plant.PNG")
D_light = Picture("C:/Users/s1011/Desktop/自主學習/D/D-light.PNG")
D_girl = Picture("C:/Users/s1011/Desktop/自主學習/D/D-girl.PNG")
D_board.pos(135, 133)
D_plant.pos(213, 365)
D_light.pos(732, 172)
D_girl.pos(477, 303)

Dall = pygame.sprite.Group(D_board, D_light, D_plant, D_girl)
D = pygame.sprite.Group(D_board, D_light, D_plant, D_girl, L_change, R_change)

for x in Dall.sprites():
    x.size(0.27)

D_1_elec = Picture("C:/Users/s1011/Desktop/自主學習/D/D-1/D-1-elec.PNG")
D_1_elecCut = Picture ("C:/Users/s1011/Desktop/自主學習/D/D-1/D-1-elecCut.PNG")
D_1_elecRe = Picture("C:/Users/s1011/Desktop/自主學習/D/D-1/D-1-elecRe.PNG")
D_1_light = Picture("C:/Users/s1011/Desktop/自主學習/D/D-1/D-1-light.PNG")
D_1_OF = Picture("C:/Users/s1011/Desktop/自主學習/D/D-1/D-1-OF.PNG")
D_1_off = Picture("C:/Users/s1011/Desktop/自主學習/D/D-1/D-1-off.PNG")
D_1_on = Picture("C:/Users/s1011/Desktop/自主學習/D/D-1/D-1-on.PNG")
D_1_elec.pos(295, 257)
D_1_elecCut.pos(295, 257)
D_1_elecRe.pos(295, 257)
D_1_light.pos(196, 282)
D_1_OF.pos(588, 144)
D_1_off.pos(588, 144)
D_1_on.pos(588, 144)

D1all =  pygame.sprite.Group(D_1_on, D_1_off, D_1_OF, D_1_light, D_1_elec, D_1_elecCut, D_1_elecRe)
D1 = pygame.sprite.Group(D_1_elec, D_1_off, back)

for x in D1all.sprites():
    x.size(0.27)

D_2_mouth = Picture("C:/Users/s1011/Desktop/自主學習/D/D-2/D-2-mouth.PNG")
D_2_moithBl = Picture("C:/Users/s1011/Desktop/自主學習/D/D-2/D-2-mouthBl.PNG")
D_2_mouth.pos(516, 473)
D_2_moithBl.pos(515, 463)

D2all = pygame.sprite.Group(D_2_mouth, D_2_moithBl)
D2 = pygame.sprite.Group(D_2_mouth, back)

for x in D2all.sprites():
    x.size(0.27)

D_2_1 = BG("C:/Users/s1011/Desktop/自主學習/D/D-2/D-2-1.PNG")

D_3_paper = Picture("C:/Users/s1011/Desktop/自主學習/D/D-3/D-3-paper.PNG")
D_3_paperOpen = Picture("C:/Users/s1011/Desktop/自主學習/D/D-3/D-3-paperOpen.PNG")
D_3_paper.pos(279, 452)
D_3_paperOpen.pos(90, 84)

D3all = pygame.sprite.Group(D_3_paper, D_3_paperOpen)
D3 = pygame.sprite.Group(back)

for x in D3all.sprites():
    x.size(0.27)

d = [A_main, B_main, C_main, D_main]

BG4 = pygame.sprite.Group(A_main, B_main, C_main, D_main)

front1 = BG("C:/Users/s1011/Desktop/自主學習/1.PNG")
front2 = BG("C:/Users/s1011/Desktop/自主學習/2.PNG")
front3 = BG("C:/Users/s1011/Desktop/自主學習/3.PNG")
front4 = BG("C:/Users/s1011/Desktop/自主學習/4.PNG")
front5 = BG("C:/Users/s1011/Desktop/自主學習/5.PNG")
front6 = BG("C:/Users/s1011/Desktop/自主學習/6.PNG")
front7 = BG("C:/Users/s1011/Desktop/自主學習/7.PNG")
front8 = BG("C:/Users/s1011/Desktop/自主學習/8.PNG")
front9 = BG("C:/Users/s1011/Desktop/自主學習/9.PNG")

front = [front1, front2,front3, front4, front5, front6, front7, front8,front9]
frontall = pygame.sprite.Group(front1, front2,front3, front4, front5, front6, front7, front8,front9)

# sound = pygame.mixer.Sound("音效.mp3") # load sound effect to variable
bgn = 0
ft = 0
iron = True
door = True


def right():
    global bgn
    d[bgn].visible = False
    bgn += 1
    if bgn == 4:
        bgn = 0
    d[bgn].visible = True
    if bgn == 1:
        B_doorclose.visible = door
        B_dooropen.visible = not door       
        B_irondoor.visible = iron
        B_closetclose.visible = True
        B_closeopen.visible = False
    else:
        B_doorclose.bye()      
        B_irondoor.bye()
        B_closetclose.bye()
        B_closeopen.bye()


def left():
    global bgn
    d[bgn].visible = False
    bgn -= 1
    if bgn == -1:
        bgn = 3
    d[bgn].visible = True
    if bgn == 1:
        B_doorclose.visible = door
        B_dooropen.visible = not door    
        B_irondoor.visible = iron
        B_closetclose.visible = True
        B_closeopen.visible = False
    else:
        B_doorclose.bye()      
        B_irondoor.bye()
        B_closetclose.bye()
        B_closeopen.bye()

def main():
    # initial settings
    global FPSCLOCK, DISPLAYSURF, BASICFONT
    pygame.init()
    FPSCLOCK = pygame.time.Clock()

    BASICFONT = pygame.font.Font('freesansbold.ttf', 16)  # font settings

    mousex = 0  # used to store x coordinate of mouse event =儲存滑鼠x座標
    mousey = 0  # used to store y coordinate of mouse event =儲存滑鼠Y座標
    pygame.display.set_caption("Karma")  # the title of the game window 視窗名稱
    front1.visible = True
    amra = 0

    global iron
    global door

    # main game loop
    while True:
        flag = False
        mouseClicked = False
        # DISPLAYSURF.fill(BGCOLOR) # fill the window with the chosen background color
        events = pygame.event.get()

        for x in frontall.sprites():
            ok = False
            if x.visible == True:
                x.out()
            for event in events:
                if event.type == pygame.MOUSEBUTTONUP:
                    if x.rect.collidepoint(event.pos) and x.visible == True:
                        print("yes")
                        ok = True
                        global ft
                        front[ft].visible = False
                        ft += 1
                        if ft == 9:
                            A_main.visible = True
                            amra = 0
                            break
                        front[ft].visible = True 

                if ok: break
            if ok: break
                    


        # 四個大背景的出現消失
        for x in BG4.sprites():
            if x.visible == True:
                x.out()
                L_change.out()
                L_change.visible = True
                R_change.out()
                R_change.visible = True

        # 還沒寫好的四大場景轉換
        
        
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                if L_change.rect.collidepoint(event.pos) and L_change.visible == True:
                    left()
                    flag = True

        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                if R_change.rect.collidepoint(event.pos) and R_change.visible == True:
                    right()
                    flag = True

        if flag: continue
       

        # 點到櫃子切換背景
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                if A_closet.rect.collidepoint(event.pos) and A_closet.visible == True:
                    A_1_main.visible = True
                    A_1_downclose.visible = True
                    A_1_upclose.visible = True
                    A_1_downopen.visible = False
                    A_1_upopen.visible = False
                        

        # A_1_main出現消失其他物件出現
        if A_1_main.visible == True:
            A_main.visible = False
            A_1_main.out()
            A_1_main.visible = True
            back.out()
            back.visible = True
            for event in events:
                if flag: break
                if event.type == pygame.MOUSEBUTTONUP:
                    if back.rect.collidepoint(event.pos) and back.visible == True:
                        A_main.visible = True
                        A_1_main.visible = False                        
                        back.bye()

            for event in events:
                if flag: break
                if event.type == pygame.MOUSEBUTTONUP:
                    if (A_1_downopen.rect.collidepoint(event.pos) and A_1_downopen.visible == True) or (A_1_downclose.rect.collidepoint(event.pos) and A_1_downclose.visible == True):
                        (A_1_downclose.visible, A_1_downopen.visible) = (
                            A_1_downopen.visible, A_1_downclose.visible)
                    if (A_1_upopen.rect.collidepoint(event.pos) and A_1_upopen.visible == True) or (A_1_upclose.rect.collidepoint(event.pos) and A_1_upclose.visible == True):
                        (A_1_upclose.visible, A_1_upopen.visible) = (
                            A_1_upopen.visible, A_1_upclose.visible)
            
            if A_1_downclose.visible == True:
                A_1_tipe.visible = False
                A_1_downclose.out()
            if A_1_upclose.visible == True:
                A_1_fire.visible = False
                A_1_upclose.out()
            if A_1_downopen.visible == True:
                A_1_downopen.out()
                A_1_tipe.visible = True
                A_1_tipe.out()
                
            if A_1_upopen.visible == True:
                A_1_upopen.out()
                A_1_fire.visible = True
                A_1_fire.out()

        # 點到果汁機切換場景
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                if A_juice.rect.collidepoint(event.pos) and A_juice.visible == True:
                    A_3_main.visible = True
                    

        # 果汁機場景
        if A_3_main.visible == True:
            A_3_main.out()
            A_main.visible = False
            A_3_main.visible = True
            back.out()
            back.visible = True
            for event in events:
                if event.type == pygame.MOUSEBUTTONUP:
                    if back.rect.collidepoint(event.pos) and back.visible == True:
                        A_main.visible = True
                        A_3_main.visible = False
                        back.bye()
                        
        # 點到上櫃子切換場景
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                if A_up.rect.collidepoint(event.pos) and A_up.visible == True:
                    A_4_main.visible = True
                    A_4_close.visible = True
                    A_4_open.visible = False
                    
        
        if A_4_main.visible == True:
            A_4_main.out()
            A_main.visible = False
            A_4_main.visible = True
            back.out()
            back.visible = True
            for event in events:
                if event.type == pygame.MOUSEBUTTONUP:
                    if back.rect.collidepoint(event.pos) and back.visible == True:
                        A_main.visible = True
                        A_4_main.visible = False
                        back.bye()
                    if A_4_open.rect.collidepoint(event.pos) and A_4_open.visible == True:
                        A_4_close.visible = True
                        A_4_open.visible = False
                        print(A_4_open.visible, A_4_close.visible)
                    elif A_4_close.rect.collidepoint(event.pos) and A_4_close.visible == True:
                        A_4_close.visible = False
                        A_4_open.visible = True
                        
                        
            
            if A_4_close.visible == True:
                A_4_paper.visible = False
                A_4_close.out()
            if A_4_open.visible == True:
                A_4_open.out()
                A_4_paper.visible = True
                A_4_paper.out()        

            ############
            for event in events:
                if flag: break
                if event.type == pygame.MOUSEBUTTONUP:
                    if A_4_B1.rect.collidepoint(event.pos) and A_4_B1.visible == True:
                        A_4_1_diary1.visible = True

        if A_4_1_diary1.visible == True:
            A_main.visible = False
            A_4_main.visible = False
            A_4_1_diary1.out()
            A_4_1_diary1.visible= True
            back.out()
            back.visible = True
            for event in events:
                if event.type == pygame.MOUSEBUTTONUP:
                    if back.rect.collidepoint(event.pos) and back.visible == True:
                        A_4_main.visible = True
                        A_4_1_diary1.visible = False
                        back.bye()    

        # 點到中櫃子切換場景
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                if A_mid.rect.collidepoint(event.pos) and A_mid.visible == True:
                    A_5_main.visible = True
                    
            
        if A_5_main.visible == True:
            A_5_main.out()
            A_main.visible = False
            A_5_main.visible = True
            back.out()
            back.visible = True
            for event in events:
                if event.type == pygame.MOUSEBUTTONUP:
                    if back.rect.collidepoint(event.pos) and back.visible == True:
                        A_main.visible = True
                        A_5_main.visible = False
                        back.bye()
                        
        # 點到下櫃子切換場景
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                if A_down.rect.collidepoint(event.pos) and A_down.visible == True:
                    A_6_main.visible = True
                    A_6_close.visible = False
                    A_6_open.visible = True
                    

        if A_6_main.visible == True:
            A_main.visible = False
            A_6_main.out()
            A_6_main.visible = True
            back.out()
            back.visible = True
            for event in events:
                if flag: break
                if event.type == pygame.MOUSEBUTTONUP:
                    if back.rect.collidepoint(event.pos) and back.visible == True:
                        A_main.visible = True
                        A_6_main.visible = False
                        back.bye()
                    if (A_6_open.rect.collidepoint(event.pos) and A_6_open.visible == True) or (A_6_close.rect.collidepoint(event.pos) and A_6_close.visible == True):
                        (A_6_close.visible, A_6_open.visible) = (
                            A_6_open.visible, A_6_close.visible)
            
            if A_6_close.visible == True:
                A_6_paper.visible = False
                A_6_swordB.visible = False
                A_6_close.out()
            if A_6_open.visible == True:
                A_6_open.out()
                A_6_paper.visible = True
                A_6_paper.out()
                A_6_swordB.visible = True
                A_6_swordB.out()
                
        if A_main.visible == True:
            for x in A.sprites():
                x.visible = True
                x.out()
        if A_main.visible == False:
            for x in A.sprites():
                x.bye()
        if A_1_main.visible == True:
            for x in A1.sprites():
                x.visible = True
                x.out()
        if A_1_main.visible == False:
            for x in A1.sprites():
                x.bye()
        if A_3_main.visible == True:
            for x in A3.sprites():
                x.visible = True
                x.out()
        if A_3_main.visible == False:
            for x in A3.sprites():
                x.bye()
        if A_4_main.visible == True:
            for x in A4.sprites():
                x.visible = True
                x.out()
        if A_4_main.visible == False:
            for x in A4.sprites():
                x.bye()



        # B櫃子開關
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                if (B_closetclose.rect.collidepoint(event.pos) and B_closetclose.visible == True) or (B_closeopen.rect.collidepoint(event.pos) and B_closeopen.visible == True):
                    (B_closeopen.visible, B_closetclose.visible) = (
                        B_closetclose.visible, B_closeopen.visible)
        
        if B_closetclose.visible == True:
            B_hand.visible = False
            B_swordA.visible = False
            B_closetclose.out()

        if B_closeopen.visible == True:
            B_closeopen.out()
            B_hand.visible = True
            B_hand.out()
            B_swordA.visible = True
            B_swordA.out()

        # B門開關
        for event in events:
            if flag: break
            if event.type == pygame.MOUSEBUTTONUP:
                if B_doorclose.rect.collidepoint(event.pos) and B_doorclose.visible == True:
                    B_doorclose.visible = False
                    B_dooropen.visible = True
                    door = False
                    flag = True       



        if B_dooropen.visible == True:
            B_doorclose.visible = False
            B_dooropen.out()
            R_change.out()               
            if event.type == pygame.MOUSEBUTTONUP:
                    if B_dooropen.rect.collidepoint(event.pos) and B_dooropen.visible == True:                            
                        amra = 1 
            if amra == 1:
                for event in events:
                    if flag: break
                    if event.type == pygame.MOUSEBUTTONUP:
                        if B_dooropen.rect.collidepoint(event.pos) and B_dooropen.visible == True:
                            B_1_main.visible = True

        if B_1_main.visible == True:
            B_main.visible = False
            B_1_main.out()
            B_1_main.visible = True
            B_1_point.out()
            B_1_point.visible = True
            back.out()
            back.visible = True
            B_irondoor.visible = False
            for event in events:
                if flag: break
                if event.type == pygame.MOUSEBUTTONUP:
                    if back.rect.collidepoint(event.pos) and back.visible == True:
                        B_closetclose.visible = True
                        B_main.visible = True
                        B_1_main.visible = False
                        B_doorclose.visible = False
                        B_dooropen.visible = True
                        B_irondoor.visible = iron

                        B_1_amra.visible = False
                        B_1_point.visible = False
                        B_1_BlMir.visible = False
                        B_1_BlNeck.visible = False

                        B_dooropen.out()
                        back.bye()

        
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                if B_1_point.rect.collidepoint(event.pos) and B_1_point.visible == True:
                    B_1_point.visible = False
                    B_1_amra.visible = True
                    B_1_hand.visible = True
                    print(B_1_hand.visible)
                if B_1_amra.rect.collidepoint(event.pos) and B_1_amra.visible == True:
                    B_1_BlMir.visible = True
                    B_1_BlNeck.visible = True


        if B_1_amra.visible == True:
            B_1_amra.out()
            B_1_hand.out()

        if B_1_BlMir.visible == True:
            B_1_BlNeck.out()
            B_1_BlMir.out()
        
        # B鐵門開關
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                if B_irondoor.rect.collidepoint(event.pos) and B_irondoor.visible == True:
                    B_irondoor.visible = False
                    iron = B_irondoor.visible
                    B_people.visible = True

        if B_people.visible == True:
            B_irondoor.visible = False
            B_people.out()
        if B_irondoor.visible == True:
            B_irondoor.out()

        if B_main.visible == True:
            for x in B.sprites():
                x.visible = True
                x.out()
        if B_main.visible == False:
            for x in Ball.sprites():
                x.bye()

        if B_1_main.visible == True:
            for x in B1.sprites():
                x.visible = True
                x.out()
        if B_1_main.visible == False:
            for x in B.sprites():
                x.bye()

        #燈
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                if D_light.rect.collidepoint(event.pos) and D_light.visible == True:
                    D_1_main.visible = True
        
        if D_1_main.visible == True:
            D_main.visible = False
            D_1_main.out()
            D_1_main.visible= True
            back.out()
            back.visible = True
            for event in events:
                if flag: break
                if event.type == pygame.MOUSEBUTTONUP:
                    if back.rect.collidepoint(event.pos) and back.visible == True:
                        D_main.visible = True
                        D_1_main.visible = False
                        back.bye()        
        #人
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                if D_girl.rect.collidepoint(event.pos) and D_girl.visible == True:
                    D_2_main.visible = True
        if D_2_main.visible == True:
            D_main.visible = False
            D_2_main.out()
            D_2_main.visible= True
            back.out()
            back.visible = True
            for event in events:
                if flag: break
                if event.type == pygame.MOUSEBUTTONUP:
                    if back.rect.collidepoint(event.pos) and back.visible == True:
                        D_main.visible = True
                        D_2_main.visible = False
                        back.bye()
                        
            for event in events:
                if flag: break
                if event.type == pygame.MOUSEBUTTONUP:
                    if D_2_mouth.rect.collidepoint(event.pos) and D_2_mouth.visible == True:
                        D_2_1.visible = True
                        
        if D_2_1.visible == True:
            D_main.visible = False
            D_2_main.visible = False
            D_2_1.out()
            D_2_1.visible= True
            back.out()
            back.visible = True
            for event in events:
                if flag: break
                if event.type == pygame.MOUSEBUTTONUP:
                    if back.rect.collidepoint(event.pos) and back.visible == True:
                        D_2_main.visible = True
                        D_2_1.visible = False
                        back.bye()
        #樹
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                if D_plant.rect.collidepoint(event.pos) and D_plant.visible == True:
                    D_3_main.visible = True
                    D_3_paper.visible = True
                    #D_3_paperOpen.visible = False
        if D_3_main.visible == True:
            D_main.visible = False
            D_3_main.out()
            D_3_main.visible = True
            back.out()
            back.visible = True
            for event in events:
                if flag: break
                if event.type == pygame.MOUSEBUTTONUP:
                    if back.rect.collidepoint(event.pos) and back.visible == True:
                        D_main.visible = True
                        D_3_main.visible = False
                        D_2_main.visible = False
                        back.bye()
                    '''if (D_3_paper.rect.collidepoint(event.pos) and D_3_paper.visible == True) or (D_3_paperOpen.rect.collidepoint(event.pos) and D_3_paperOpen.visible == True):
                            (D_3_paperOpen.visible, D_3_paper.visible) = (
                                D_3_paper.visible, D_3_paperOpen.visible)'''
                            
            if D_3_paperOpen.visible == True:
                D_3_paperOpen.out()           
            if D_3_paper.visible == True:
                D_3_paper.out()
        #板子
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                if D_board.rect.collidepoint(event.pos) and D_board.visible == True:
                    D_4_main.visible = True
                    
        if D_4_main.visible == True:
            D_main.visible = False
            D_4_main.out()
            D_4_main.visible= True
            back.out()
            back.visible = True
            for event in events:
                if flag: break
                if event.type == pygame.MOUSEBUTTONUP:
                    if back.rect.collidepoint(event.pos) and back.visible == True:
                        D_main.visible = True
                        D_4_main.visible = False
                        back.bye()
        if D_main.visible == True:
            D_main.out()
            for x in D.sprites():
                x.visible = True
                x.out()
        if D_main.visible == False:
            for x in D.sprites():
                x.bye()
        if D_1_main.visible == True:
            D_1_main.out()
            for x in D1.sprites():
                x.visible = True
                x.out()
        if D_1_main.visible == False:
            for x in D1.sprites():
                x.bye()
        if D_2_main.visible == True:
            D_2_main.out()
            for x in D2.sprites():
                x.visible = True
                x.out()
        if D_2_main.visible == False:
            for x in D2.sprites():
                x.bye()
        if D_3_main.visible == True:
            D_3_main.out()
            for x in D3.sprites():
                x.visible = True
                x.out()
        if D_3_main.visible == False:
            for x in D3.sprites():
                x.bye()
    
        # 背景迴圈還沒寫

        checkForQuit()

        # Redraw the screen and wait a clock tick.
        pygame.display.update()
        FPSCLOCK.tick(FPS)

# program exiting functions begin


def terminate():
    pygame.quit()
    sys.exit()


def checkForQuit():
    for event in pygame.event.get(QUIT):  # get all the QUIT events
        terminate()  # terminate if any QUIT events are present
    for event in pygame.event.get(KEYUP):  # get all the KEYUP events
        if event.key == K_ESCAPE:
            terminate()  # terminate if the KEYUP event was for the Esc key
            pygame.event.post(event)  # put the other KEYUP event objects back
# program exiting functions end


if __name__ == '__main__':  # start the program
    main()
