import pygame as pg;

pg.init();
pg.font.init();

LARGURA = 800
ALTURA = 800

BRANCO = (255,255,255)

JANELA = pg.display.set_mode((LARGURA,ALTURA));#seto o tamanho da tela
pg.display.set_caption("jogo da velha");# nome da janela

def renderizaJanela(JANELA):

    #deixa o fundo roxo
    JANELA.fill((112,38,205));

    #colunas
    pg.draw.line(JANELA, BRANCO, (266,60), (266,800), 10);
    pg.draw.line(JANELA, BRANCO, (532,60), (532,800), 10);

    #linhas
    pg.draw.line(JANELA, BRANCO, (0,60), (800,60), 10);
    pg.draw.line(JANELA, BRANCO, (0,266), (800,266), 10);
    pg.draw.line(JANELA, BRANCO, (0,572), (800,572), 10);

    pg.display.update();

#game loop
def main():
    janelaAberta = True;

    while(janelaAberta):
        pg.time.delay(5);

        for event in pg.event.get():
            if event.type == pg.QUIT:
                janelaAberta = False;
        
        renderizaJanela(JANELA);


main();