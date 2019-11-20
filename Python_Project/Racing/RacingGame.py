import pygame, random, sys, os, time
from pygame.locals import *

#initiatoin  of window in Pygame
pygame.init()
display_width=800
diplay_height=600

# Defining color
grey = [119, 118, 110]
black = [0, 0, 0]
white=[255, 255, 255]
light_white=[224, 229, 225]
red = [255, 0, 0]
bright_red=[224, 15, 15]
blue = [132, 112 , 255]
bright_blue=[0 ,0 , 255]
green=[0 , 200 , 0]
bright_green=[0 , 255 , 0]

pause=False
# Displaying window  size and it's title
Display= pygame.display.set_mode((display_width,diplay_height))
title=pygame.display.set_caption("Racing Game")
clock=pygame.time.Clock()


# Loading image from system
carImage=pygame.image.load('car13.png')
bckGroundimage1=pygame.image.load("left.png")
bckGroundimage2=pygame.image.load("right.png")
w2=pygame.image.load("y3.jpeg")
intro_img=pygame.image.load("into_image.jpg")





# Creating first page of game using intro loop
def intro_loop():
    intro=True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        # showing "Car game "  on ittro page
        Display.blit(intro_img,(0,0))
        Largetext = pygame.font.Font("freesansbold.ttf", 100)
        Textrect = Largetext.render("CAR GAME", 1, black)
        Textrect_pos = (170,200)
        Display.blit(Textrect, Textrect_pos)


        # Definning Buttons on Intro page
        button("START", 150, 520, 90, 40, green, bright_green, "play")
        button("QUIT", 550, 520, 90, 40, red, bright_red, "quit")
        button("INSTRUCTION", 300, 520, 200, 40, blue, bright_blue, "intro")
        pygame.display.update()
        clock.tick(50)



# definning button function and action of every button.
def button(msg,x,y,w,h,ic,ac,action=None):
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()

    if x+w>mouse[0]>x and y+h >mouse[1]>y:
        pygame.draw.rect(Display,ac,(x,y,w,h))
        if click[0]==1 and action!= None:

            if action=="play":
                game_loop()

            elif action=="quit":
                pygame.quit()
                quit()
                sys.exit()

            elif action == "intro":
                 instruction()

            elif action == "back":
                intro_loop()

            elif action == "pause":
                paused()

            elif action=="restart":
                game_loop()

            elif action=="main_menu":
                intro_loop()


    else:
        pygame.draw.rect(Display,ic,(x,y,w,h))

    smalltext=pygame.font.Font("freesansbold.ttf",20)
    textsurf, textrect = text_object(msg, smalltext)
    textrect.center = ((x+(w/2)),(y+(h/2)))
    Display.blit(textsurf, textrect)


#definning instruction function on page of  Starting
def instruction():
    instruction = True
    while instruction:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()


        Display.blit(intro_img, (0, 0))


        # Showing text instructin on  instruction_page
        large_text =pygame.font.Font("freesansbold.ttf", 60)
        small_text=pygame.font.Font("freesansbold.ttf", 20)
        medium_text=pygame.font.Font("freesansbold.ttf", 40)

        para = small_text.render("This is a simple car game in which you need dodge and coming car", 1, black)
        position = ((100 ,130))
        Display.blit(para,position)

        Instruction = large_text.render("INSTRUCTION", 1, white)
        Instruction_pos = (180, 50)
        Display.blit(Instruction, Instruction_pos)

        L_arr = small_text.render("LEFT ARROW : TURN LEFT", 1, black)
        L_arr_pos = (150, 265)
        Display.blit(L_arr, L_arr_pos)

        R_arr = small_text.render("RIGHT ARROW : TURN RIGHT", 1, black)
        R_arr_pos = (150, 315)
        Display.blit(R_arr, R_arr_pos)

        Acc = small_text.render(" A : ACCELERATION", 1, black)
        Acc_pos = (150, 365)
        Display.blit(Acc, Acc_pos)

        Br = small_text.render(" B : BREAK", 1, black)
        Br_pos = (150, 415)
        Display.blit(Br, Br_pos)

        Pa = small_text.render(" P : PAUSE", 1, black)
        Pa_pos = (150, 465)
        Display.blit(Pa, Pa_pos)

        Co = medium_text.render(" CONTROL", 1, black)
        Co_pos = (150, 205)
        Display.blit(Co, Co_pos)


        # Back button on instruction page
        button("Back", 550, 480, 60, 40, red, bright_red, "back")
        pygame.display.update()
        clock.tick(30)




#creating pause function on racing page
def paused():

    while paused:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()

        Display.blit(intro_img,(0,0))
        large_text=pygame.font.Font("freesansbold.ttf",90)
        x=large_text.render("PAUSED" , 1, black)
        large_text_pos=(255,150)
        Display.blit(x,large_text_pos)



        #buttons on pause page
        button("CONTINUE",150,450,130,40,green,bright_green,"resume")
        button("RESTART", 350, 450, 130, 40, red, bright_red, "restart")
        button("MAIN MENU", 550, 450, 130, 40, blue, bright_blue, "main_menu")

        pygame.display.update()
        clock.tick(20)


#Fixing background images position
def background():
    Display.blit(bckGroundimage1, (0,0))
    Display.blit(bckGroundimage1, (0,100))
    Display.blit(bckGroundimage1, (0, 200))

    Display.blit(bckGroundimage2, (650,0 ))
    Display.blit(bckGroundimage2, (650, 200))
    Display.blit(bckGroundimage2, (650, 400))

    Display.blit(w2,(355,0))
    Display.blit(w2, (355,100))
    Display.blit(w2, (355,300))

    Display.blit(w2, (355,400))
    Display.blit(w2, (355,500))





#Creating fucntion for showing " Game Over !! "
def text_object(text,font):
    textsurface=font.render(text,1,white)
    return textsurface,textsurface.get_rect()

def msg_display(text):
    largetext=pygame.font.Font("freesansbold.ttf",60)
    textsurf,textrect=text_object(text,largetext)
    textrect.center=((diplay_height)/1.5 ,(display_width)/3)
    Display.blit(textsurf,textrect)
    pygame.display.update()
    time.sleep(4)
    game_loop()

def crash():
    msg_display("Game Over !!")




#Definnig function for Score_board.
def score_system(passed,score):
    font=pygame.font.SysFont(None,35)
    text=font.render("Passed" + str(passed),True, black)
    score=font.render("Score " + str(score) ,True, bright_blue)
    Display.blit(text,(0,60))
    Display.blit(score, (0, 30))



#Defining car position in window
def car(x,y):
    Display.blit(carImage ,(x,y))



#function for other cars and their speed
def obstacels(obs_startx, obs_starty, obs):

    if obs==0:
        obs_pic=pygame.image.load("car15.png")

    if obs == 1:
        obs_pic = pygame.image.load("car1.png")

    if obs == 2:
        obs_pic = pygame.image.load("car2.png")

    if obs == 3:
        obs_pic = pygame.image.load("car3.png")

    if obs == 4:
        obs_pic = pygame.image.load("car6.png")

    if obs == 5:
        obs_pic = pygame.image.load("car5.png")

    if obs == 6:
        obs_pic = pygame.image.load("car6.png")

    Display.blit(obs_pic,(obs_startx,obs_starty))




def game_loop():

    x= (295)                                            # Position of car in x axes
    y= (440)
                                                        # Position of car in y axes
    x_change=0
    obstacels_spped = 30                               # speed of car coming from front
    obs = 0
    y_change = 0
    obs_startx = random.randrange(200,500)              # only in this range coming car will exist otherwise game will over.
    obs_starty = -750
    obs_width = 190
    obs_height = 190
    passed = 0
    score = 0
    level = 0


    bumped = False
    while not bumped:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -20


                if event.key == pygame.K_RIGHT:
                    x_change=20

                if event.key == pygame.K_a:
                    obstacels_spped+= 2

                if event.key == pygame.K_a:
                    obstacels_spped-= 2

            if event.type == pygame.K_UP:
                if event.key ==pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change=0


        x+=x_change

        Display.fill(grey)
        background()


        obs_starty-= (obstacels_spped /4)
        obstacels(obs_startx , obs_starty , obs)
        obs_starty+= obstacels_spped


        # calling score system  and car position
        score_system(passed,score)
        car(x, y)


        #  Displaying text "Game Over" when car move out of road.
        if x < 35 or x > 585:
            crash()


        # Set the position of the comming car from front side. in x and y axis
        if obs_starty > 600:
            obs_starty = 0 - obs_height
            obs_startx = random.randrange(100, (display_width-400))
            obs=random.randrange(0,7)

            # Incrementing the counting of Score and passed car
            passed=passed+1
            score=passed*10
            if int(passed)%10==0:
                level = level + 1
                obstacels_spped+20

                # Showing "level" in game_loop page
                largetext = pygame.font.Font("freesansbold.ttf", 60)
                level_text= largetext.render("Level "+str(level) , 1 ,white)
                position =(300,220)
                Display.blit(level_text, position)
                pygame.display.update()
                time.sleep(1)


        # Crashing car when car  touch to each other
        if y < obs_starty + 150:
            if x > obs_startx and x < obs_startx or x + 125 > obs_startx and  x + 160 < obs_startx + obs_width :
                crash()


        # Pause button on our game_loop page
        button("PAUSE",695,0,105,25,red,bright_red,"pause")
        pygame.display.update()
        clock.tick(60)

intro_loop()
game_loop()
pygame.quit()
quit()
