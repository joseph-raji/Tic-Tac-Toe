
from turtle import width
import pygame, sys
from pygame.locals import *
from button import Button
import random



# Main Window ========
pygame.init()

window = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Background.png")

def get_font(size): 
    return pygame.font.Font("assets/font.ttf", size)

# ==========================

commence=False
def play(commence,useMinimax):
    keepGameRunning = True
    
    #Constantes:
    bot = 'X'
    player = 'O'
    screenWidth = 600
    screenHeight = 600
    fps = 30
    bgColor = pygame.Color( 255, 255, 255 )

    #Chargement des images
    fond = pygame.image.load( "img/tictactoe.png" )
    X_img= pygame.image.load( "img/X.png")
    O_img= pygame.image.load( "img/O.png")

    pygame.init()
    timer = pygame.time.Clock()
    window = pygame.display.set_mode( ( screenWidth, screenHeight ) )
    pygame.display.set_caption( "Tic tac toe" )


    #set background to white
    window.fill( bgColor )
    window.blit( fond, ( 0, 0 ) ) # draw at (0,0)


    #On definit le board comme un dictionnaire
    board = {1: ' ', 2: ' ', 3: ' ',
            4: ' ', 5: ' ', 6: ' ',
            7: ' ', 8: ' ', 9: ' '}

    #On recupere le click du joueur
    def click_joueur():
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()

            if event.type == MOUSEBUTTONDOWN:
                mouseX, mouseY = event.pos  
                x,y=0,0
                pos=0
                for i in range(0,3):
                    for j in range(0,3):
                        if 200*i<mouseX<600 and 200*j<mouseY<600:
                            x,y=i+1,j+1
                #print(x,y)
                if y==1 :
                    pos=x+y-1
                if y==2:
                    pos=x+y+1
                if y==3:
                    pos=x+y+3
                return pos

    def playerMove():
        position = None
        while position==None:
            position=click_joueur()
            if position!= None:
                insertLetter('O',position)


    def spaceIsFree(position):
        if board[position] == ' ':
            return True
        else:
            return False

    def insertLetter(letter, position):
        if spaceIsFree(position):
            board[position] = letter

            if position==1:
                x,y=25,25
            if position==2:
                x,y=225,25
            if position==3:
                x,y=425,25

            if position==4:
                x,y=25,225
            if position==5:
                x,y=225,225
            if position==6:
                x,y=425,225
        
            if position==7:
                x,y=25,425
            if position==8:
                x,y=225,425
            if position==9:
                x,y=425,425

            #############################
            if letter == 'X':
                window.blit(X_img, (x,y))
            if letter == 'O':
                window.blit(O_img, (x, y))
            pygame.display.update()

            fin_de_partie(letter)
            return
        else:
            playerMove()
        
    #Pr afficher le texte
    def texte(text):
        myfont = pygame.font.SysFont("monospace", 60)
        label=myfont.render(text,1,(0,0,0),(255,255,255))
        window.blit(label,(175,275))
        pygame.display.update()

    ## Dans cette fonction, dans chacun de ces deux cas (draw ou win), on fait appelle de nouveau a play() pour redemarer la partie
    def fin_de_partie(letter):
        if checkForWin():
            if letter == 'X':
                texte("Bot Win!")
                pygame.time.delay(1000)
                play(not commence,useMinimax)
            else:            
                texte("You Win!")
                pygame.time.delay(1000)
                play(not commence,useMinimax)
        if (checkDraw()):
            texte("DRAW!")
            pygame.time.delay(1000)
            play(not commence,useMinimax)

    def checkForWin():
        if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
            return True
        elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
            return True
        elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '):
            return True
        elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
            return True
        elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
            return True
        elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
            return True
        elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
            return True
        elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):
            return True
        else:
            return False

    def checkWhichMarkWon(mark):
        if board[1] == board[2] and board[1] == board[3] and board[1] == mark:
            return True
        elif (board[4] == board[5] and board[4] == board[6] and board[4] == mark):
            return True
        elif (board[7] == board[8] and board[7] == board[9] and board[7] == mark):
            return True
        elif (board[1] == board[4] and board[1] == board[7] and board[1] == mark):
            return True
        elif (board[2] == board[5] and board[2] == board[8] and board[2] == mark):
            return True
        elif (board[3] == board[6] and board[3] == board[9] and board[3] == mark):
            return True
        elif (board[1] == board[5] and board[1] == board[9] and board[1] == mark):
            return True
        elif (board[7] == board[5] and board[7] == board[3] and board[7] == mark):
            return True
        else:
            return False

    def checkDraw():
        for key in board.keys():
            if (board[key] == ' '):
                return False
        return True

    def compMove():
        if (useMinimax==True):
            bestScore = -800
            bestMove = 0
            for key in board.keys():
                if (board[key] == ' '):
                    board[key] = bot
                    score = minimax(board, False)
                    board[key] = ' '
                    if (score > bestScore):
                        bestScore = score
                        bestMove = key
        
            insertLetter(bot, bestMove)
        else:
            liste_cases_vides=[]
            for key in board.keys():
                if spaceIsFree(key):
                    liste_cases_vides.append(key)
            print("voila la liste: ", liste_cases_vides)
            key=random.choice(liste_cases_vides)
            insertLetter(bot, key)

        return


    def minimax(board,  isMaximizing):
        #On check d'abord la fin de match
        if (checkWhichMarkWon(bot)):
            return 1
        elif (checkWhichMarkWon(player)):
            return -1
        elif (checkDraw()):
            return 0
        #On execute minimax
        if (isMaximizing):
            bestScore = -800
            for key in board.keys():
            #Pr chaque cle du tableau, si la position est vide, on place un piont a cette position et on boucle minimax en jouant a la place de l'adversaire.
            #Ainsi de suite, on testera toute les sous positions jusqu'a arriver a une configuration qui maximisera notre score
                if (board[key] == ' '):
                    board[key] = bot
                    score = minimax(board,  False)
                    board[key] = ' '
                    if (score > bestScore):
                        bestScore = score
            return bestScore

        else:
            bestScore = 800
            for key in board.keys():
                if (board[key] == ' '):
                    board[key] = player
                    score = minimax(board,  True)
                    board[key] = ' '
                    if (score < bestScore):
                        bestScore = score
            return bestScore

    if (commence == False):
        while not checkForWin():
            pygame.display.update()
            compMove()
            playerMove()

    if (commence == True):
        while not checkForWin():
            pygame.display.update()
            playerMove()
            compMove()


def main_menu():
    while True:
        window.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("TIC TAC TOE", True, "#000000")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        MINIMAX_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250), 
                            text_input="PLAY MINIMAX", font=get_font(75), base_color="#d7fcd4", hovering_color="#000000")
        RANDOM_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400), 
                            text_input="PLAY DUMMY", font=get_font(75), base_color="#d7fcd4", hovering_color="#000000")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="#000000")

        window.blit(MENU_TEXT, MENU_RECT)

        for button in [MINIMAX_BUTTON, RANDOM_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(window)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if MINIMAX_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play(commence,True)
                if RANDOM_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play(commence,False)
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
main_menu()