#Modules
import random
import pygame

pygame.init()

#Main Screen Diensions
disp_width = 800
disp_height = 600

#colors
white = (255,255,255)
black = (0,0,0)
red =   (255,0,0)
green = (0,255,0)
blue =  (0,0,255)
yellow = (255,255,0)
orange = (255,140,0)
pink =  (255,0,255)

#variables
gridsize = 20
block_size = 20
grid_loop = 1
colorArray = [red,green,blue,yellow,orange,pink]
lock = 1

#Display and Clock init
screen = pygame.display.set_mode((disp_width,disp_height))
pygame.display.set_caption("Flood It!-Py")  
clock = pygame.time.Clock()
screen.fill(white)


#Grid
def grid():
    for y in range(gridsize):
            for x in range(gridsize):
                rect = pygame.Rect(x*block_size+50, y*block_size+50, block_size, block_size)
                pygame.draw.rect(screen,random.choice(colorArray), rect)



#Flood
def flood(x,y,oldcolor,newcolor):
    thiscolor = screen.get_at((x,y))
    if(thiscolor == oldcolor):
        rect = pygame.Rect(x,y, block_size, block_size)
        pygame.draw.rect(screen,newcolor,rect)
        flood(x+block_size,y,oldcolor,newcolor)
        flood(x,y+block_size,oldcolor,newcolor)
        
#UI
def ui():
    pygame.draw.rect(screen,red,(700,50,50,50))
    pygame.draw.rect(screen,blue,(700,110,50,50))
    pygame.draw.rect(screen,green,(700,170,50,50))
    pygame.draw.rect(screen,yellow,(700,230,50,50))
    pygame.draw.rect(screen,orange,(700,290,50,50))
    pygame.draw.rect(screen,pink,(700,350,50,50))
        
    
                
                                      
#Game Loop
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            clk_col = screen.get_at((pos))
            print(pos,clk_col)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                lock = 1
            if event.key == pygame.K_KP1:
                oldcolor = screen.get_at((50,50))
                flood(50,50,oldcolor,red)
            if event.key == pygame.K_KP2:
                oldcolor = screen.get_at((50,50))
                flood(50,50,oldcolor,green)
            if event.key == pygame.K_KP3:
                oldcolor = screen.get_at((50,50))
                flood(50,50,oldcolor,blue)
            if event.key == pygame.K_KP4:
                oldcolor = screen.get_at((50,50))
                flood(50,50,oldcolor,yellow)
            if event.key == pygame.K_KP5:
                oldcolor = screen.get_at((50,50))
                flood(50,50,oldcolor,orange)
            if event.key == pygame.K_KP6:
                oldcolor = screen.get_at((50,50))
                flood(50,50,oldcolor,pink)
    ui()


    if lock == 1:
        grid()
        lock = 0
  
    pygame.display.update()
    clock.tick(60)
pygame.quit()
quit()
