import pygame as pg
from pygame.constants import MOUSEBUTTONDOWN
from pygame.draw import rect;

pg.init();
pg.font.init();

LARGURA = 800
ALTURA = 800

BRANCO = (255,255,255)
AZUL = (55, 194, 203)

global escolha;
escolha = "x";
global vez;
vez = "p1";
global tabuleiro;
global rect1;
global rect2;
global rect3;
global rect4;
global rect5;
global rect6;
global rect7;
global rect8;
global rect9;

#areas clicaveis
#1
rect1 = pg.Rect((149,187), (164,147));
rect2 = pg.Rect((321,187), (164,147));
rect3 = pg.Rect((497,187), (164,147));
#2
rect4 = pg.Rect((149,347), (160,167));
rect5 = pg.Rect((497,187), (164,147));
rect6 = pg.Rect((497,347), (164,167));
#3
rect7 = pg.Rect((149,528), (160,167));
rect8 = pg.Rect((321,528), (164,167));
rect9 = pg.Rect((497,528), (164,167));

tabRect = [rect1,rect2,rect3,
            rect4,rect5,rect6,
            rect7,rect8,rect9];


JANELA = pg.display.set_mode((LARGURA,ALTURA));#seto o tamanho da tela
pg.display.set_caption("jogo da velha");# nome da janela

def desenhaTabuleiro(JANELA,pg,pontP1,pontP2):

    #deixa o fundo roxo
    JANELA.fill((112,38,205));

    fonte = pg.font.SysFont("Robot", 30);
    lbPontP1 = fonte.render(f"Pontuação P1: {pontP1}", 1, BRANCO);
    lbPontP2 = fonte.render(f"Pontuação P2: {pontP2}", 1, BRANCO);

    JANELA.blit(lbPontP1, (56, 36));
    JANELA.blit(lbPontP2, (573, 36));


    #desenha retangulo
    '''
    pg.draw.rect(JANELA, (83,116,116), (55,124, 689,623));
    pg.draw.rect(JANELA, (88,124,124), (88,155, 624,564));
    '''

    #teste area 
    '''
    pg.draw.rect(JANELA, BRANCO, (149,187, 160,147));
    pg.draw.rect(JANELA, BRANCO, (321,187, 164,147));
    pg.draw.rect(JANELA, BRANCO, (497,187, 164,147));

    pg.draw.rect(JANELA, BRANCO, (149,347, 160,167));
    pg.draw.rect(JANELA, BRANCO, (321,347, 164,167));
    pg.draw.rect(JANELA, BRANCO, (497,347, 164,167));

    pg.draw.rect(JANELA, BRANCO, (149,528, 160,167));
    pg.draw.rect(JANELA, BRANCO, (321,528, 164,167));
    pg.draw.rect(JANELA, BRANCO, (497,528, 164,167));'''

    #colunas
    pg.draw.line(JANELA, AZUL, (314,186), (314,694), 10);
    pg.draw.line(JANELA, AZUL, (490,186), (490,694), 10);

    #linhas
    pg.draw.line(JANELA, AZUL, (149,339.61), (660,339.61), 10);
    pg.draw.line(JANELA, AZUL, (149,520.61), (660,520.61), 10);

def renderizaJanela(JANELA,pg,pontP1,pontP2):

    desenhaTabuleiro(JANELA,pg,pontP1,pontP2);

    pg.display.update();

def desenhaPeca(JANELA,pg,vez,x, y):
    if(vez == "p1"):
        img = pg.image.load("./img/x.png").convert_alpha();
        imgR = pg.transform.scale(img, (100,100));
        JANELA.BLIT(imgR, (x-50, y-50));
    else:
        img = pg.image.load("./img/circulo.png").convert_alpha();
        imgR = pg.transform.scale(img, (100,100));
        JANELA.BLIT(imgR, (x-50, y-50));

def testaOndeMouseClicou(event, listaRect, mousePos):
    
    for posicao in listaRect:
        if event.type == MOUSEBUTTONDOWN and posicao.collidepoint(mousePos):
            print("entrou1")
            if posicao == rect1:
                print("entrou")
                testaJogada(0, (149,187),escolha);
            elif(posicao == rect2):
                print("entrou")
                testaJogada(0, (321,187),escolha);
            elif(posicao == rect3):
                print("entrou")
                testaJogada(0, (497,187),escolha);
            elif(posicao == rect4):
                print("entrou")
                testaJogada(0, (497,187),escolha);
            elif(posicao == rect5):
                print("entrou")
                testaJogada(0, [100,100],escolha);
            elif(posicao == rect6):
                print("entrou")
                testaJogada(0, [100,100],escolha);
            elif(posicao == rect7):
                print("entrou")
                testaJogada(0, [100,100],escolha);
            elif(posicao == rect8):
                print("entrou")
                testaJogada(0, [100,100],escolha);
            elif(posicao == rect9):
                print("entrou")
                testaJogada(0, [100,100],escolha);

def testaJogada(indice, pos, escolha):
    
    if(tabuleiro[indice] == "X"):
        print("X");
    elif(tabuleiro[indice] == "O"):
        print("O");
    else:
        print(tabuleiro)
        tabuleiro[indice] = escolha;



janelaAberta = True;
tabuleiro = [None,None,None,
            None,None,None,
            None,None,None];
pontuP1 = 0;
pontuP2 = 0;
mousePos = pg.mouse.get_pos();



while(janelaAberta):
    pg.time.delay(5);

    for event in pg.event.get():
        if event.type == pg.QUIT:
            janelaAberta = False;
        if event.type == MOUSEBUTTONDOWN:
            testaOndeMouseClicou(event,tabRect, mousePos);
            
    
    renderizaJanela(JANELA,pg,pontuP1,pontuP2);