from numpy import transpose

def solved(board):
    for i in range(9):
        for j in range(9):
            if board[i][j]==0:
                return (i,j)
    return True


def solver(board):
    if solved(board):
        return True
    else:
        i,j=solved(board)
        for numb in range(1,10):
            if check_viability(board,numb,(i,j) ):
                board[i][j]=numb

                if solver(board): #recursive. continues since this point  
                    #so in this recursive this line is returned on a descending way. which means that is awaiting to co throw or to be asigned to zero
                    return True
                board[i][j]= 0 #set to zero and continues to next viable value in this position
    
    return False


def check_viability(board, val, pos):
    row,colum=pos
    for j in range(9):
        if board[row][j]==val and j!=colum :
            return False

    trans= transpose(board)
    for i in range(9):
        if trans[colum][i]==val and i!=row :
            return False

    x=row//3
    y=colum//3
    for i in range(x*3,x*3+3):
        for j in range(y*3,y*3+3):
            if board[i][j]==val and (i,j)!=pos:
                return False
    return True 


def solved(board):
    for i in range(9):
        for j in range(9):
            if i==8:
                coco=2
            if board[i][j]==0:
                return (i,j)
    return board


def check_viability(board, value, pos):
    row,colum=pos
    linha= list(filter(lambda x: x==value,board[row]))
    if len(linha)>= 1 :
        return False

    trans= transpose(board)
    coluna= list(filter(lambda x: x==value, trans[colum]) )
    if len(coluna)>=1 :
        return False
    x=row//3
    y=colum//3
    for i in range(x*3,x*3+3):
        for j in range(y*3,y*3+3):
            if board[i][j]==value and (i,j)!=pos:
                return False
    return True


def solved_board(board):
    if solved(board)==board:
        return board
    else:
        i,j=solved(board)
        for numb in range(1,10):
            if check_viability(board,numb,(i,j) ):
                board[i][j]=numb

                if solved_board(board): #recursive. continues since this point  
                    #so in this recursive this line is returned on a descending way. which means that is awaiting to co throw or to be asigned to zero
                    return board
                board[i][j]= 0 #set to zero and continues to next viable value in this position
    
    return None 
