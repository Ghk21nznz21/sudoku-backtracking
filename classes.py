import pygame


class Grid:
    board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7] ]
   
    def __init__(self, rows: int, cols: int, width: int, height: int):
        ''' Initiate board instances.
        2 Instances have to be created, so 1 can hold the board solved and the other for the player. 
        Board var is also created to maintain the inicial board comun to all instances of the game, so it cant be changed '''
        self.rows = rows
        self.cols = cols
        self.width = width
        self.height = height
        
        self.board_ini= [ [self.board[i][j] for j in range(cols)] for i in range(rows) ]         
        self.cubes = [ [Cube(Grid.board[i][j], i, j, width, height) for j in range(self.cols)] for i in range(self.rows)]
        self.selected=None # POS( row,col) 
     
    def draw(self, win):  
        ''' draw lines and cubes '''
        gap = self.width / 9  
        for i in range(self.rows+1):
            if i % 3 == 0 and i != 0:
                thick = 4
            else:
                thick = 1
            pygame.draw.line(win, (0,0,0), (0, i*gap), (self.width, i*gap), thick) 
            pygame.draw.line(win, (0, 0, 0), (i * gap, 0), (i * gap, self.height), thick)
    
        for i in range(self.rows):
            for j in range(self.cols):
                self.cubes[i][j].draw_to_cube(win)  

    def mouse_clicked_pos(self, pos):   
        if pos[0] < self.width and pos[1] < self.height:
            gap = self.width / 9
            x = pos[0] // gap
            y = pos[1] // gap
            return (int(y),int(x))
        else:
            return None
    
    def mouse_clicked(self, row, col):  
        ''' set all to false. set clicked to true '''
        for i in range(self.rows):
            for j in range(self.cols):
                self.cubes[i][j].pressed=False  
        self.cubes[row][col].pressed=True   
        self.selected= (row,col)

    def sketch(self, temp):
        ''' allow player to draw number sketches on the cubes '''
        row, col = self.selected
        self.cubes[row][col].set_temporary(temp)       
    
    def convert_to_value(self, val, val_resolution):
        ''' Compare Move to Solved board -> act acordly '''
        i,j=self.selected
        if val== val_resolution:
            self.cubes[i][j].value=val
            return True       
        self.cubes[i][j].set_val(0)
        self.cubes[i][j].set_temporary(0)
        return False

    def clear(self):       
        ''' Delete button '''
        row, col = self.selected
        if self.cubes[row][col].value == 0:
            self.cubes[row][col].set_temporary(0)   
    
    def tip(self):
        ''' Player stuck helper '''
        for i in range(9):
            for j in range(9):
                if self.cubes[i][j].value==0:
                    return i,j
        return (10,10)
            
    def finished(self):  
       lista= [ item.value for sublist in self.cubes for item in sublist]
       return 0 in lista
       

class Cube:
    def __init__(self, value, row, col, width, height): 
        self.value = value
        self.temp = 0 	#temporary value ->if next event is Enter then becomes a value 
        self.width = width
        self.height = height
        self.row = row
        self.col = col 
        self.pressed = False
             
    def draw_to_cube(self, window):
        fnt = pygame.font.SysFont("Times New Roman", 28)
        gap= self.width /9 #gap = cube height or cube width . cube pos in the window to draw input value 
        x = self.col * gap
        y = self.row * gap 
        #draw sketch or value 
        if self.value==0 and self.temp !=0:
            text = fnt.render(str(self.temp), 1, (128, 128, 128))
            window.blit(text, (x+5, y+5))
        if self.value !=0:
            text = fnt.render(str(self.value), 1, (0, 0, 0))
            window.blit(text, (x + (gap/2 - text.get_width()/2), y + (gap/2 - text.get_height()/2)))
        if self.pressed:  # if pressed then cube becomes red and thicker
            pygame.draw.rect(window, (255,0,0), (x,y, gap ,gap), 3 ) 

    #setter
    def set_val(self, value):
        self.value=value
    
    #setter
    def set_temporary(self, temp):
        self.temp=temp