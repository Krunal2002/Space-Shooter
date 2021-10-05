import pygame
import random
import math
# from pygame.constants import MOUSEMOTION

pygame.init()

#Window size
main_screen = pygame.display.set_mode((800,700))

#Changed title and icon of app
icon = pygame.image.load('icon.jpg')
icon = pygame.transform.scale(icon, (20,20))
background = pygame.image.load('bg.png')
background = pygame.transform.scale(background, (800, 700))

pygame.display.set_caption('Space Shooter')
pygame.display.set_icon(icon)


#Sound
shootSound = pygame.mixer.Sound("bulletSound.wav")
explodeSound = pygame.mixer.Sound("explSound.wav")
crashSound =  pygame.mixer.Sound("crash.ogg")
gameMusic = pygame.mixer.music.load("music.ogg")
#-------------------

running = True
score = 0

#For displaying plane on screen
plane = pygame.image.load('plane.png')
plane = pygame.transform.scale(plane, (60, 60))
planeX = 350
planeY = 550

directionX = 0
directionY = 0 

def handlePlane(X, Y):
    main_screen.blit(plane, (X,Y))
#---------------


#For Shooting Bullet
bullet = pygame.image.load('bullet1.png')
bullet = pygame.transform.scale(bullet, (60, 60))
bulletX = 0
bulletY = 850
fireBullet = False


def shoot_bullet(x,y):
    global fireBullet
    fireBullet = True
    main_screen.blit(bullet, (x,y))
#---------------


#For Astroids
astroid1 = []
astroidX = []
astroidY = []
speedX = []
speedY = []

# astroid2 = pygame.image.load('astroid.png')
# astroid4 = pygame.image.load('astroid3.png')
# astroid5 = pygame.image.load('astroid4.png')
# astroid6 = pygame.image.load('astroid5.png')
# astroid7 = pygame.image.load('astroid6.png')

totalAstroid = 6

for i in range(totalAstroid):
    astroid1.append(pygame.image.load('astroid.png'))
    astroid1.append(pygame.image.load('astroid6.png'))
    astroid1.append(pygame.image.load('astroid3.png'))
    astroid1.append(pygame.image.load('astroid4.png'))
    astroid1.append(pygame.image.load('astroid5.png'))
    astroid1[i] = pygame.transform.scale(astroid1[i], (80,80))
    astroidX.append(random.randrange(0,750))
    astroidY.append(random.randrange(0,10))
    speedX.append(random.randrange(0, 3))
    speedY.append(random.randrange(2,5))


def showAstroid(X, Y, i):
    main_screen.blit(astroid1[i], (X,Y))
#---------------


#Checking for collision
def isCollision(astroidX, astroidY, bulletX, bulletY):
    distance = math.sqrt((math.pow(astroidX-bulletX,2))+(math.pow(astroidY-bulletY,2)))

    if distance < 30:
        return True
    else: 
        return False
#---------------


#For showing score
font = pygame.font.Font('freesansbold.ttf', 25)

def showScore(score):
    text = font.render("Score: "+ str(score), True, (255,255,255))
    main_screen.blit(text,(10,10))
#---------------


#For Player Life
life = 3
miniPlane = pygame.transform.scale(plane, (30,30))
def DrawLives(surf, x, y, lives, img):
    for i in range(lives):
        img_rect= img.get_rect()
        img_rect.x = x + 40 * i
        img_rect.y = y
        surf.blit(img, img_rect)
#---------------

#Crash
def isCrash(astroidX, astroidY, planeX, planeY):
    distance = math.sqrt(math.pow(planeX-astroidX,2) + math.pow(planeY-astroidY,2))

    if distance < 30:
        return True
    else: 
        return False
#---------------


#Game Over
overFont = pygame.font.Font("C:\Windows\Fonts\Arial.ttf", 50)
replay = pygame.font.Font("C:\Windows\Fonts\Arial.ttf", 30)

def showGameOver():
    overText = overFont.render("Game Over", True, (255,255,255))
    replayText = replay.render("Restart Game:[r]", True, (255,255,255))
    main_screen.blit(overText,(250,250))
    main_screen.blit(replayText,(270,450))
    pygame.mixer.music.stop()
#---------------


#explosion
expl = []

expl1 = pygame.image.load('expl0.png')
expl2 = pygame.image.load('expl1.png')
expl3 = pygame.image.load('expl2.png')
expl4 = pygame.image.load('expl3.png')
expl5 = pygame.image.load('expl4.png')
expl6 = pygame.image.load('expl5.png')
expl7 = pygame.image.load('expl6.png')
expl8 = pygame.image.load('expl7.png')


for i in range(0,8):
    expl.append(expl1)
    expl.append(expl2)
    expl.append(expl3)
    expl.append(expl4)
    expl.append(expl5)
    expl.append(expl6)
    expl.append(expl7)
    expl[i] = pygame.transform.scale(expl[i], (75, 75))

def explode(X, Y):
    explodeSound.play()
    for i in range(0,8):
        main_screen.blit(expl[i], (X,Y))
#---------------


#player explosion
playerExpl = []

playerExpl1 = pygame.image.load('playerExpl1.png')
playerExpl2 = pygame.image.load('playerExpl2.png')
playerExpl3 = pygame.image.load('playerExpl3.png')
playerExpl4 = pygame.image.load('playerExpl4.png')
playerExpl5 = pygame.image.load('playerExpl5.png')
playerExpl6 = pygame.image.load('playerExpl6.png')
playerExpl7 = pygame.image.load('playerExpl7.png')


for i in range(0,8):
    playerExpl.append(playerExpl1)
    playerExpl.append(playerExpl2)
    playerExpl.append(playerExpl3)
    playerExpl.append(playerExpl4)
    playerExpl.append(playerExpl5)
    playerExpl.append(playerExpl6)
    playerExpl.append(playerExpl7)
    playerExpl[i] = pygame.transform.scale(playerExpl[i], (75, 75))

def playerExplode(X, Y):
    for i in range(0,8):
        main_screen.blit(playerExpl[i], (X,Y))
#---------------


#Ready Screen
def ready():
    ready = pygame.mixer.Sound('ready.ogg')
    ready.play()
    pygame.time.wait(3000)
    pygame.mixer.music.play(-1)
#---------------

ready()

# Game Loop
while running: 

    #Background
    main_screen.fill((0,0,0))
    main_screen.blit(background, (0,0))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.mixer.music.stop()
            running = False

        #On pressing keys
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                directionX = -5
            if event.key == pygame.K_RIGHT:
                directionX = 5
            if event.key == pygame.K_UP:
                directionY = -4
            if event.key == pygame.K_DOWN:
                directionY = 4


            if event.key == pygame.K_r:
                score = 0
                life = 3
                running = True
                pygame.mixer.music.play(-1)
                for i in range(totalAstroid):
                    astroidX[i] = random.randrange(0,750)
                    astroidY[i] = random.randrange(0,10)
            
            if event.key == pygame.K_q:
                pygame.mixer.music.stop()
                running = False


        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            if fireBullet is False:
                bulletX = planeX
                bulletY = planeY - 20
                shoot_bullet(bulletX-20, bulletY)
                shootSound.play()


        #On releasing keys
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT: 
                directionX = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                directionY = 0


        # if event.type == MOUSEMOTION:
        #     planeX, planeY = event.pos


    #Boundery for plane
    if planeX > 770:
        planeX = 770
    if planeX < 20:
        planeX = 20
    if planeY > 620:
        planeY = 620
    if planeY < 420:
        planeY = 420
    #------------
        

    #Plane direction
    planeX += directionX
    planeY += directionY
    handlePlane(planeX - 20, planeY - 20)
    #---------------


    #Astrois spawn
    for i in range(totalAstroid):
        if life<=0 :
            showGameOver()
            break

        showAstroid(astroidX[i], astroidY[i], i)
        astroidX[i] += speedX[i]
        astroidY[i] += speedY[i]

        if astroidX[i] >= 800 or astroidX[i] <= -50 or astroidY[i] >= 700:
            astroidX[i] = random.randrange(0,650)
            astroidY[i] = random.randrange(0,10)
            speedX[i] = random.randrange(0,3)
            speedY[i] = random.randrange(2,5)

        # Checking collision
        collision = isCollision(astroidX[i], astroidY[i], bulletX-10, bulletY)
        
        if collision:
            fireBullet = False
            bulletY = 520
            explode(astroidX[i], astroidY[i])

            score+=1
            astroidX[i] = random.randrange(0,750)
            astroidY[i] = random.randrange(0,10)

        crash = isCrash(astroidX[i], astroidY[i], planeX - 10, planeY)
        if crash:
            life-=1
            playerExplode(planeX - 20, planeY)
            crashSound.play()

            astroidX[i] = random.randrange(0,750)
            astroidY[i] = random.randrange(0,10)

    #-------------


    #Bullet
    if fireBullet is True:
        bulletY -= 8
        shoot_bullet(bulletX-20, bulletY)
        # shoot_bullet(bulletX-35, bulletY)
    if bulletY <= 0:
        bulletY = -100
        fireBullet = False
    #--------------

    DrawLives(main_screen, 680, 10, life, miniPlane)
    showScore(score)
    pygame.display.update()


pygame.quit()