import pygame as pg

pg.init()

win =   pg.display.set_mode((500, 480))
pg.display.set_caption("1st game")

class player(object):

    def __init__(self, x, y, width, height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.vel=5
        self.jumpCount=5
        self.stepCount=0
        self.left=False
        self.right=False
        self.isJump=False

    def draw(self, win):
        if self.stepCount + 1 >= 27:
            self.stepCount = 0

        if self.left:
            win.blit(walkLeft[self.stepCount // 3], (self.x, self.y))
            self.stepCount += 1

        elif self.right:
            win.blit(walkRight[self.stepCount // 3], (self.x, self.y))
            self.stepCount += 1

        else:
            win.blit(char, (self.x, self.y))



walkRight = [pg.image.load('R1.png'), pg.image.load('R2.png'), pg.image.load('R3.png'), pg.image.load('R4.png'), pg.image.load('R5.png'), pg.image.load('R6.png'), pg.image.load('R7.png'), pg.image.load('R8.png'), pg.image.load('R9.png')]
walkLeft = [pg.image.load('L1.png'), pg.image.load('L2.png'), pg.image.load('L3.png'), pg.image.load('L4.png'), pg.image.load('L5.png'), pg.image.load('L6.png'), pg.image.load('L7.png'), pg.image.load('L8.png'), pg.image.load('L9.png')]
bg = pg.image.load('bg.jpg')
char = pg.image.load('standing.png')

clock=pg.time.Clock()
run = True

def gameWindow():

    win.blit(bg,(0,0))
    man.draw(win)
    pg.display.update()




while run:

    man = player(45, 400, 64, 64)

    clock.tick(27)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    keys= pg.key.get_pressed()

    if keys[pg.K_LEFT] and man.x> man.vel:
        man.left=True
        man.right=False
        man.x  -=  man.vel

    elif keys[pg.K_RIGHT] and man.x < 500-man.width-man.vel:
        man.left = False
        man.right = True
        man.x += man.vel

    else:
        man.left=False
        man.right=False
        man.stepCount=0

    if not (man.isJump):
        if keys[pg.K_SPACE]:
            man.isJump=True
            man.left=False
            man.right=False
            man.stepCount=0


    else:
            if man.jumpCount >= -5:
             neg=1

            if man.jumpCount<0:
                    neg = -1
                    man.y -= (man.jumpCount ** 2 ) * 0.5 * neg
                    man.jumpCount -= 1

            else:
              man.isJump= False
              man.jumpCount= 5


    gameWindow()

pg.quit()