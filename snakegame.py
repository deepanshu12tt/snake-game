import pygame
import random
pygame.init()##initialize pygame all modules
pygame.mixer.music.load('faded.mp3')
pygame.mixer.music.play()
#colrs
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)
screen_width=900
screen_height=500
gamewindow=pygame.display.set_mode((screen_width,screen_height))##creating window
bjimg=pygame.image.load("snake.jpg")
bjimg=pygame.transform.scale(bjimg,(screen_width,screen_height)).convert_alpha()
pygame.display.set_caption("Snakes with deepanshu")##giving title
pygame.display.update()##if u make any changes this will update all the changes
#game specicif variables
clock=pygame.time.Clock()
font=pygame.font.SysFont(None,55)
snake_size=25
def text_screen(text,color,x,y):
    screen_text=font.render(text,True,color)
    gamewindow.blit(screen_text,[x,y])
def plot_snake(amewindow,color,snake_list,size):
    for x,y in snake_list:
        pygame.draw.rect(gamewindow,color,[x,y,snake_size,snake_size])
def gameloop():
    snake_list=[]
    snake_length=1
    exit_game=False
    game_over=False
    snake_x=45
    snake_y=55
    snake_size=25
    fps=50
    velocity_x=0
    velocity_y=0
    food_x= random.randint(20,screen_width/2)
    food_y= random.randint(20,screen_height/2)
    score=0
    while not exit_game:
        if game_over:
            gamewindow.fill(white)
            text_screen("Game over!Press Enter to continue",red,100,250)
            for event in pygame.event.get():

                if event.type==pygame.QUIT:
                        exit_game=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        gameloop()
        else:

            for event in pygame.event.get():

                if event.type==pygame.QUIT:
                        exit_game=True
                if event.type==pygame.KEYDOWN:
                     if event.key==pygame.K_RIGHT:
                          velocity_x=10
                          velocity_y=0
                     if event.key==pygame.K_LEFT:
                         velocity_x=-10
                         velocity_y=0

                     if event.key==pygame.K_UP:
                          velocity_y=-10
                          velocity_x=0

                     if event.key==pygame.K_DOWN:
                         velocity_y=10
                         velocity_x=0
            snake_x+=velocity_x
            snake_y+=velocity_y
            if abs(snake_x-food_x)<6 and abs(snake_x-food_x)<6:
                score+=1
                food_x= random.randint(20,screen_width/2)
                food_y= random.randint(20,screen_height/2)
                snake_length+=3
            gamewindow.fill(white)
            gamewindow.blit(bjimg,(0,0))
            text_screen("score:"+str(score*10),red,5,5)
            pygame.draw.rect(gamewindow,red,[food_x,food_y,snake_size,snake_size])
            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)
            if len(snake_list)>snake_length:
                del snake_list[0]
            if head in snake_list[:-1]:
                game_over=True
            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over=True
            plot_snake(gamewindow,black,snake_list,snake_size)
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()
gameloop()