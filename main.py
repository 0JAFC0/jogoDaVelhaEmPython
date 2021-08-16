import pygame as pg;

pg.init();
pg.font.init();

LARGURA = 800
ALTURA = 800

BRANCO = (255,255,255)
AZUL = (55, 194, 203)

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
    pg.draw.rect(JANELA, (83,116,116), (55,124, 689,623));
    pg.draw.rect(JANELA, (88,124,124), (88,155, 624,564));

    #colunas
    pg.draw.line(JANELA, AZUL, (314,186), (314,690), 10);
    pg.draw.line(JANELA, AZUL, (490,186), (490,690), 10);

    #linhas
    pg.draw.line(JANELA, AZUL, (149,339.61), (651,339.61), 10);
    pg.draw.line(JANELA, AZUL, (149,520.61), (651,520.61), 10);

def renderizaJanela(JANELA,pg,pontP1,pontP2):

    desenhaTabuleiro(JANELA,pg,pontP1,pontP2);

    pg.display.update();


#game loop
def main():
    janelaAberta = True;
    
    pontuP1 = 0;
    pontuP2 = 0;

    

    while(janelaAberta):
        pg.time.delay(5);

        for event in pg.event.get():
            if event.type == pg.QUIT:
                janelaAberta = False;
        
        renderizaJanela(JANELA,pg,pontuP1,pontuP2);

#roda a função principal
main();