import pygame
from pygame.locals import*
def initializeboard(gameDisplay):
    bg = pygame.Surface(gameDisplay.get_size())
    bg = bg.convert()
    pygame.draw.line(bg,rd,(0,250),(750,250))
    pygame.draw.line(bg,rd,(250,250),(250,1000))
    pygame.draw.line(bg,rd,(500,250),(500,1000))
    pygame.draw.line(bg,rd,(0,500),(750,500))
    pygame.draw.line(bg,rd,(0,750),(750,750))
    return bg



def modifyinfo(a,mx,my,c,gameDisplay,bg):
    if (c)%2 == 0:
        turn = 'O'
    else:
        turn = 'X'

    pygame.display.update()
    font = pygame.font.Font(None,100)
    text1 = font.render(turn,1,gr)
    if mx < 250 and my < 500 and my > 250:
        a[0][0] = turn
        gameDisplay.blit(text1,(125,375))
    elif mx > 250 and mx <500 and my < 500 and my > 250:
        a[0][1] = turn
        gameDisplay.blit(text1,(375,375))
    elif mx > 500 and my < 500 and my > 250:
        a[0][2] = turn
        gameDisplay.blit(text1,(625,375))
    elif mx < 250 and my > 500 and my < 750:
        a[1][0] = turn
        gameDisplay.blit(text1,(125,625))
    elif mx > 250 and mx < 500 and my > 500 and my < 750:
        a[1][1] = turn
        gameDisplay.blit(text1,(375,625))
    elif mx > 500 and my > 500 and my < 750:
        a[1][2] = turn
        gameDisplay.blit(text1,(625,625))
    elif mx < 250 and my > 750:
        a[2][0] = turn
        gameDisplay.blit(text1,(125,875))
    elif mx > 250 and mx <500 and my > 750:
        a[2][1] = turn
        gameDisplay.blit(text1,(375,875))
    elif mx >500 and my > 750:
        a[2][2] = turn
        gameDisplay.blit(text1,(625,875))

    pygame.display.flip()
    ch = gamecheck()
    if ch == 1:
          crashed = True

def showboard(c,a,mx,my,gameDisplay,bg):
    pygame.display.flip()
    modifyinfo(a,mx,my,c,gameDisplay,bg)


def gamecheck():
    ch = 0
    for i in range(0,3):
        if a[i][0] == a[i][1] == a[i][2]== 'O' or a[i][0] == a[i][1] == a[i][2]== 'X':
            ch = 1
            t = a[i][0]
            break
    for i in range(0,3):
        if a[0][i] == a[1][i] == a[2][i] == 'O' or a[i][0] == a[i][1] == a[i][2]== 'X':
            ch = 1
            t = a[0][i]
            break
    if a[0][0] == a[1][1] == a[2][2] == 'O' or a[0][0] == a[1][1] == a[2][2] == 'X':
        ch = 1
        t = a[0][0]
    elif a[0][2] == a[1][1] == a[2][0] == 'O' or a[0][2] == a[1][1] == a[2][0] == 'X':
        ch = 1
        t = a[0][2]
    if ch == 1:
        font = pygame.font.Font(None,48)
        text = font.render('Winner is '+t,1,wt)
        gameDisplay.blit(text,(20,100))




ch = 0
bl = (0,0,0)
wt = (255,255,255)
clock = pygame.time.Clock()
crashed = False
rd = (255,0,0)
gr = (0,255,0)
nt = 0
pygame.init()
c = 0
gameDisplay = pygame.display.set_mode((750,1000))
gameDisplay.fill((0,0,0))
pygame.display.set_caption('Tic-Tac-Toe')
bg = initializeboard(gameDisplay)
a = [ ['a' for i in range(3)] for j in range(3)]
gameDisplay.fill(bl)
gameDisplay.blit(bg,(0,0))
font = pygame.font.Font(None,96)
text = font.render('Tic-Tac-Toe' ,1,(238,130,238))
gameDisplay.blit(text,(200,20))
font = pygame.font.Font(None,30)
text = font.render('X first' ,1,wt)
gameDisplay.blit(text,(10,210))
while not crashed:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    crashed = True
            e = pygame.event.wait()
            if event.type==pygame.MOUSEMOTION:
                    mx = 30
                    my = 30
            if event.type == pygame.MOUSEBUTTONDOWN:
                    mx,my = pygame.mouse.get_pos()
                    if my>250:
                        c += 1
                        nt += 1
                        print(nt)

    ch = showboard(c,a,mx,my,gameDisplay,bg)

    if nt >= 9:
        crashed = True


pygame.quit()
quit()
