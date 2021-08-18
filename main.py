#importações
import pygame as pg
from pygame.constants import MOUSEBUTTONDOWN
from pygame.draw import rect;

#esta função desenha o tabuleiro na janela
def desenhaTabuleiro(JANELA,pg,pontP1,pontP2):
    #deixa o fundo roxo
    JANELA.fill((112,38,205));

    fonte = pg.font.SysFont("Robot", 30);
    lbPontP1 = fonte.render(f"Pontuação P1: {pontP1}", 1, BRANCO);
    lbPontP2 = fonte.render(f"Pontuação P2: {pontP2}", 1, BRANCO);

    JANELA.blit(lbPontP1, (56, 36));
    JANELA.blit(lbPontP2, (573, 36));

    #desenha retangulo
    pg.draw.rect(JANELA, (83,116,116), (55,124, 689,623));
    pg.draw.rect(JANELA, (88,124,124), (88,155, 624,564));
    

    #teste area
    """
    pg.draw.rect(JANELA, BRANCO, rect1);
    pg.draw.rect(JANELA, BRANCO, rect2);
    pg.draw.rect(JANELA, BRANCO, rect3);

    pg.draw.rect(JANELA, BRANCO, rect4);
    pg.draw.rect(JANELA, BRANCO, rect5);
    pg.draw.rect(JANELA, BRANCO, rect6);

    pg.draw.rect(JANELA, BRANCO, rect7);
    pg.draw.rect(JANELA, BRANCO, rect8);
    pg.draw.rect(JANELA, BRANCO, rect9);
    """

    #colunas
    pg.draw.line(JANELA, AZUL, (314,186), (314,694), 10);
    pg.draw.line(JANELA, AZUL, (490,186), (490,694), 10);

    #linhas
    pg.draw.line(JANELA, AZUL, (149,339.61), (660,339.61), 10);
    pg.draw.line(JANELA, AZUL, (149,520.61), (660,520.61), 10);

#esta função desenha as peças na posição passada
def desenhaPeca(x,y):
    if vez == 'p1':
        img = pg.image.load('./img/x.png')
        imgR = pg.transform.scale(img, (100, 100))
        JANELA.blit(imgR, (x - 50, y - 50))
    else:
        img = pg.image.load('./img/o.png')
        imgR = pg.transform.scale(img, (100, 100))
        JANELA.blit(imgR, (x - 50, y - 50))

#esta função ela confirma se a jogada que o jogador fez ja foi feita.
def confirmar(indice, pos, p1,p2):
    global escolha, vez, espaco, pontP1, pontP2
    if(tabuleiro[indice] == "x"):
        print("x")
    elif(tabuleiro[indice] == "o"):
        print("o")
    else:
        tabuleiro[indice] = escolha;
        desenhaPeca(pos[0],pos[1]);
        if(testaVitoria(escolha)):
            mostrarMensagemDoGanhador(vez);
            if(vez=="p1"):
                pontP1 += 1;
            else:
                pontP2 += 1;
            #reset();
        elif(not(testaVitoria(escolha)) and espaco == 9):
            mostrarMensagemDoGanhador("EMPATE");
            #reset();
        else:
            if(vez == "p1"):
                vez = "p2"
                escolha = "o"
            else:
                vez = "p1"
                escolha = "x"
            espaco += 1

# esta função ela testa onde o mouse clicou e depois ela verifica qual o rect que foi clicado e chama a função desenhar
def testaOndeMouseClicou():
    mousePos = pg.mouse.get_pos();
    for p in tabRect:
        if event.type == MOUSEBUTTONDOWN and p.collidepoint(mousePos):
            if p == rect1:
                confirmar(0,(230, 270), pontP1, pontP2)
            elif p == rect2:
                confirmar(1,(405, 270), pontP1, pontP2)
            elif p == rect3:
                confirmar(2,(575, 270), pontP1, pontP2)
            elif p == rect4:
                confirmar(3,(230, 430), pontP1, pontP2)
            elif p == rect5:
                confirmar(4,(405, 430), pontP1, pontP2)
            elif p == rect6:
                confirmar(5,(575, 430), pontP1, pontP2)
            elif p == rect7:
                confirmar(6,(230, 610), pontP1, pontP2)
            elif p == rect8:
                confirmar(7,(405, 610), pontP1, pontP2)
            elif p == rect9:
                confirmar(8,(575, 610), pontP1, pontP2)

def testaVitoria(vez):
    return ((tabuleiro[0] == vez and tabuleiro[1] == vez and tabuleiro[2] == vez) or
        (tabuleiro[3] == vez and tabuleiro[4] == vez and tabuleiro[5] == vez) or
        (tabuleiro[6] == vez and tabuleiro[7] == vez and tabuleiro[8] == vez) or
        (tabuleiro[0] == vez and tabuleiro[3] == vez and tabuleiro[6] == vez) or
        (tabuleiro[1] == vez and tabuleiro[4] == vez and tabuleiro[7] == vez) or
        (tabuleiro[2] == vez and tabuleiro[5] == vez and tabuleiro[8] == vez) or
        (tabuleiro[0] == vez and tabuleiro[4] == vez and tabuleiro[8] == vez) or
        (tabuleiro[2] == vez and tabuleiro[4] == vez and tabuleiro[6] == vez));

def mostrarMensagemDoGanhador(vez):
    arial = pg.font.SysFont('arial', 70)
    mensagem = 'JOGADOR {} VENCEU'.format(vez)

    if vez == 'EMPATE':
        JANELA.blit(arial.render('DEU VELHA', True, (125, 0, 130), 0), (180, 355))
    else:
        JANELA.blit(arial.render(mensagem, True, (125, 0, 130), 0), (17, 355))

def reset():
        global escolha, estado, vez, tabuleiro, espaco
        estado = 'JOGANDO'
        vez = 'p1'
        escolha = 'x'
        espaco = 0
        tabuleiro = [
            1, 2, 3,
            4, 5, 6,
            7, 8, 9]
        desenhaTabuleiro(JANELA,pg,pontP1,pontP2);
        pg.display.update()

# inicializa o pygame e as fontes
pg.init();
pg.font.init();

LARGURA = 800
ALTURA = 800

BRANCO = (255,255,255)
AZUL = (55, 194, 203)

#variaveis de controle na partida
espaco = 1
escolha = "x";
vez = "p1";

#variaveis globais
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


#configurações da janela
JANELA = pg.display.set_mode((LARGURA,ALTURA));#seto o tamanho da tela
pg.display.set_caption("jogo da velha");# nome da janela

#retangulos para fazer as colisões
#linha 1
rect1 = pg.Rect(149,187, 160,146);
rect2 = pg.Rect(321,187, 164,146);
rect3 = pg.Rect(497,187, 164,146);
#linha 2
rect4 = pg.Rect(149,347, 160,166);
rect5 = pg.Rect(321,347, 164,166);
rect6 = pg.Rect(497,347, 164,166);
#linha 3
rect7 = pg.Rect(149,530, 160,166);
rect8 = pg.Rect(321,528, 164,166);
rect9 = pg.Rect(497,528, 164,166);

tabRect = [rect1,rect2,rect3,
            rect4,rect5,rect6,
            rect7,rect8,rect9];

tabuleiro = [1,2,3,
            4,5,6,
            7,8,9];

 #variaveis de pontuação           
pontP1 = 0;
pontP2 = 0;

janelaAberta = True;

#tem que chamar a função aqui pq senão não funciona, a função 
desenhaTabuleiro(JANELA,pg,pontP1,pontP2);

while(janelaAberta):
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            janelaAberta = False;
        if event.type == MOUSEBUTTONDOWN:
                testaOndeMouseClicou();
            
    
    pg.display.flip()

pg.display.quit()