import pygame
from var_handlers import format_time

def window_draw(win, board,time, strikes):
    ''' Draw GAME Screen'''

    win.fill((255,255,255))
    fnt = pygame.font.SysFont("Times New Romam", 28)
    tex = fnt.render("Time: " + format_time(time), 1, (0,0,0))
    win.blit(tex, (540 - 160, 560))
    text = fnt.render("X " * strikes, 1, (255, 0, 0))
    win.blit(text, (20, 560))
    board.draw(win) #method of the class Grid not a pygame method 


def buttom(window,texto):      
    ''' Draw Play Again Screen'''

    window.fill( (0,0,0))
    width,height= pygame.display.get_surface().get_size()
    fnt = pygame.font.SysFont("Times New Romam", 28)
    text = fnt.render(texto, 1, (255, 0, 0))
    text_rect = text.get_rect( center=( width//2 , height//2)  )
    window.blit(text, text_rect)
    
    again_text= fnt.render('Play Again',True,(0,250,0))
    width_text= text.get_rect().width/2 #same as get_rect().height

    box= [width//3-again_text.get_rect().width/2, height//1.5-again_text.get_rect().height/2,again_text.get_rect().width,again_text.get_rect().height]
    pygame.draw.rect(window,(0,100,0),box )
    window.blit(again_text,(box[0],box[1]))
    mouse= pygame.mouse.get_pos()
    click= pygame.mouse.get_pressed()

    if  box[0]<mouse[0]<box[0]+box[2] and box[1]<mouse[1]<box[1]+box[3]:
        t2= fnt.render('Play Again',True,(150,0,0))  
        window.blit(t2,(box[0],box[1])) #if mouse inside the box/rect will create the same rect with a darker color on top of the previous
        if click[0]==1: # mouse movement (0,0,0) if clicked the zero turns into a one. depending of the buttom clicked
            return True 
               
                       
def draw_end(window,texto): #loop forever untill a return -> the output/return will be add to run ->continuing the second loop or not
    ''' GAME ENDED SCREEN ''' 
    while True:
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                return False  
        window.fill((0,0,0))   #adding the screen of the paused game
        bol= buttom(window,texto)
        pygame.display.update()
        if bol== True:   #if boll is True then 'Play Again' was pressed
            return True #stop the pause screen and restarts game
    return False
    
 