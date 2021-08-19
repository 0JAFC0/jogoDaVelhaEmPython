#importações
import pygame as pg
from pygame.constants import MOUSEBUTTONDOWN 
from pygame.draw import rect;
import time

#esta função desenha a tela do menu
def desenhaTelaMenu(JANELA,pg):
    #deixa o fundo roxo
    JANELA.fill((112,38,205))

    #adiciona texto na tela
    fonte = pg.font.SysFont("Robot", 72);
    lbTextoMenu = fonte.render("Jogo da Velha", 1, VERDE);
    JANELA.blit(lbTextoMenu, (220, 162));

    #area dos botões
    pg.draw.rect(JANELA, (181,0,31), rect1Menu);

    fonte = pg.font.SysFont("Robot", 60);
    lbTextoMenu = fonte.render("P1VSP2", 1, VERDE);
    JANELA.blit(lbTextoMenu, (313, 379));

    pg.draw.rect(JANELA, VERDE, rect2Menu);
    
    lbTextoMenu = fonte.render("EXIT", 1, (181,0,31));
    JANELA.blit(lbTextoMenu, (342, 480));

    #imagens da tela
    JANELA.blit(pg.transform.scale(pg.image.load("./img/jogodavelha.png"),(162,138)),(53,616))

    JANELA.blit(pg.transform.scale(pg.image.load("./img/pessoas-velhas.png"),(128,122)),(623,40))

def testaOndeMouseClicouNaTelaMenu():
    mousePos = pg.mouse.get_pos();
    for p in tabRect:
        if event.type == MOUSEBUTTONDOWN and p.collidepoint(mousePos):
            if p == rect1Menu:
                return "JOGANDO"
            elif p == rect2Menu:
                exit()

 
#esta função desenha o tabuleiro na JANELA
def desenhaTelaJogo(JANELA,pg,pontP1,pontP2):
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
def confirmarPosicaoTelaJogo(indice, pos):
    global escolha, vez, espaco
    if(tabuleiro[indice] == "x"):
        print("x")
    elif(tabuleiro[indice] == "o"):
        print("o")
    else:
        tabuleiro[indice] = escolha;
        desenhaPeca(pos[0],pos[1]);
        if(vez == "p1"):
            vez = "p2"
            escolha = "o"
        else:
            vez = "p1"
            escolha = "x"
        espaco += 1

# esta função ela testa onde o mouse clicou e depois ela verifica qual o rect que foi clicado e chama a função desenhar
def testaOndeMouseClicouNaTelaJogo():
    mousePos = pg.mouse.get_pos();
    for p in tabRect:
        if event.type == MOUSEBUTTONDOWN and p.collidepoint(mousePos):
            if p == rect1:
                confirmarPosicaoTelaJogo(0,(230, 270))
            elif p == rect2:
                confirmarPosicaoTelaJogo(1,(405, 270))
            elif p == rect3:
                confirmarPosicaoTelaJogo(2,(575, 270))
            elif p == rect4:
                confirmarPosicaoTelaJogo(3,(230, 430))
            elif p == rect5:
                confirmarPosicaoTelaJogo(4,(405, 430))
            elif p == rect6:
                confirmarPosicaoTelaJogo(5,(575, 430))
            elif p == rect7:
                confirmarPosicaoTelaJogo(6,(230, 610))
            elif p == rect8:
                confirmarPosicaoTelaJogo(7,(405, 610))
            elif p == rect9:
                confirmarPosicaoTelaJogo(8,(575, 610))

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

    if vez == 'EMPATOU':
        JANELA.blit(arial.render('DEU VELHA', True, (125, 0, 130), 0), (180, 355))
    else:
        JANELA.blit(arial.render(mensagem, True, (125, 0, 130), 0), (17, 355))

def reset():
        global escolha, estadoDoJogo, vez, tabuleiro, espaco
        estadoDoJogo = 'JOGANDO'
        vez = 'p1'
        escolha = 'x'
        espaco = 1
        tabuleiro = [
            1, 2, 3,
            4, 5, 6,
            7, 8, 9]
        desenhaTelaJogo(JANELA,pg,pontP1,pontP2);
        pg.display.update()

if __name__ == "__main__":
    # inicializa o pygame e as fontes
    pg.init();
    pg.font.init();

    LARGURA = 800;
    ALTURA = 800;

    BRANCO = (255,255,255);
    AZUL = (55, 194, 203);
    VERDE = (88, 124, 124);

    #variaveis globais
    global tabuleiro;
    #global pontP1, pontP2;
    global rect1,rect2,rect3,rect4,rect5,rect6,rect7,rect8,rect9;
    global rect1Menu,rect2Menu;

    #retangulos para fazer as colisões
    #retangulos do menu
    rect1Menu = pg.Rect(307,371, 164,57);
    rect2Menu = pg.Rect(307,471, 164,57);

    tabRect = [rect1Menu,rect2Menu];

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

    #configurações da JANELA
    pg.display.set_icon(pg.image.load("./img/pessoas-velhas.png"));#seta icone das Janelas
    JANELA = pg.display.set_mode((LARGURA,ALTURA));#seta o tamanho da tela

    pg.display.set_caption("Jogo da velha");# nome da JANELA

    estadoDoJogo = "MENU";
    desenhaUmaVez = True;
    janelaAberta = True;

    #variaveis de controle na partida
    espaco = 1;
    escolha = "x";
    vez = "p1";

    #variaveis de pontuação           
    pontP1 = 0;
    pontP2 = 0;

    while(janelaAberta):
        if(estadoDoJogo == "JOGANDO"):
            #condição para ele sempre desenhar uma unica vez, pq se não ele sempre fica desenhando
            if(desenhaUmaVez):
                desenhaTelaJogo(JANELA,pg,pontP1,pontP2);
                desenhaUmaVez = False;
            elif(estadoDoJogo == "JOGANDO"):
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        janelaAberta = False;
                        exit();
                    if event.type == MOUSEBUTTONDOWN:
                        testaOndeMouseClicouNaTelaJogo();
                        
                if(testaVitoria("x")):
                    print("entrou x")
                    pontP1 += 1;
                    estadoDoJogo = "RESETAR";
                elif(testaVitoria("o")):
                    print("entrou o")
                    pontP2 += 1;
                    estadoDoJogo = "RESETAR";
                elif(espaco >= 9):
                    print("entrou empate")
                    estadoDoJogo = "RESETAR";
            if(pontP1 == 2 or pontP2 == 2):
                print("reseta")
                pontP1 = 0;
                pontP2 = 0;
                estadoDoJogo = "MENU";
                desenhaUmaVez = True;
                if(pontP1 == 2):
                    mostrarMensagemDoGanhador("PLAYER1");
                    pg.display.flip();
                    time.sleep(5)
                else:
                    mostrarMensagemDoGanhador("PLAYER2");
                    pg.display.flip();
                    time.sleep(5)
            pg.display.flip();
        elif(estadoDoJogo == "MENU"):
            desenhaTelaMenu(JANELA,pg);
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.display.quit();
                    janelaAberta = False;
                    exit();
                if event.type == MOUSEBUTTONDOWN:
                    estadoDoJogo = testaOndeMouseClicouNaTelaMenu();
            pg.display.flip();
        else:#reseta a tela
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.display.quit();
                    exit();
                if(event.type == MOUSEBUTTONDOWN):
                    reset();
                    desenhaTelaJogo(JANELA,pg,pontP1,pontP2);
            pg.display.flip();
