import sys
from random import random
import argparse
import pygame as pg

# Configurações do Jogo
FPS = 50
TITULO = "Lógica - Tarefa 2 - Game of Life"
SUBTITULO = "Alunas: Carla Moreno Barbosa e Luana Gonçalves Ribeiro"
TAMANHO_PIXEL = 16
GERACOES_POR_SEGUNDO = 15
PROBABILIDADE_PIXEL_ATIVO = 0.5
ESQUERDO = 0

# Cores
PRETO = (0, 0, 0)
CINZA = (60, 60, 60)
AMARELO = (255, 255, 0)
BRANCO = (255, 255, 255)

# Tipografia
TAMANHO_FONTE = 20
FONTE = 'arial'

class Pixel(pg.sprite.Sprite):
    def __init__(self, jogo, x, y):
        self.groups = jogo.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.image = pg.Surface((TAMANHO_PIXEL, TAMANHO_PIXEL))
        self.rect = self.image.get_rect()
        self.rect.x = x * TAMANHO_PIXEL
        self.rect.y = y * TAMANHO_PIXEL
        self.desativado()

    def desativado(self, cor=PRETO):
        self.alive = False
        self.image.fill(cor)

    def ativado(self, cor=BRANCO):
        self.alive = True
        self.image.fill(cor)
        self.cor = cor

    def sobrevive(self):
        self.cor = (r, g, b)
        self.image.fill(self.cor)


class Jogo:
    def __init__(self):
        pg.init()
        pg.font.init()
        self.screen = pg.display.set_mode((LARGURA, ALTURA))
        pg.display.set_caption(TITULO)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100)
        self.nova_geracao_event = pg.USEREVENT+1
        pg.time.set_timer(self.nova_geracao_event, int(1000/GERACOES_POR_SEGUNDO))

        self.menu_font = pg.font.SysFont(FONTE, TAMANHO_FONTE)

    def novo(self):
        self.gridlargura = int(LARGURA / TAMANHO_PIXEL)
        self.gridaltura = int(ALTURA / TAMANHO_PIXEL)
        self.pause = True
        self.show_menu = True
        self.show_grid = True
        self.cor = BRANCO
        self.all_sprites = pg.sprite.Group()
        self.cells = []
        for x in range(self.gridlargura):
            self.cells.append([])
            for y in range(self.gridaltura):
                self.cells[x].append(Pixel(self, x, y))
        self.previous_click, self.previous_x, self.previous_y = None, None, None

    def rodar(self):
        while True:
            self.clock.tick(FPS)
            self.eventos()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()

    def draw_grid(self):
        for x in range(0, LARGURA, TAMANHO_PIXEL):
            pg.draw.line(self.screen, CINZA, (x, 0), (x, ALTURA))
        for y in range(0, ALTURA, TAMANHO_PIXEL):
            pg.draw.line(self.screen, CINZA, (0, y), (LARGURA, y))

    def blit(self, posicao, texto, cor=AMARELO):
        self.screen.blit(self.menu_font.render(texto, False, cor), (TAMANHO_FONTE, TAMANHO_FONTE*posicao))

    def draw(self):
        self.all_sprites.draw(self.screen)
        if self.show_grid:
            self.draw_grid()
        if self.show_menu:
            self.blit(0, f"{TITULO}")
            self.blit(1, f"{SUBTITULO}")
            self.blit(3, f"Instruções:")
            self.blit(4, f"Para iniciar o jogo, o usuário deve marcar")
            self.blit(5, f"com o mouse os pixels que inicialmente estarão")
            self.blit(6, f"ativados, sendo que os demais pixels permanecerão desativados")
            self.blit(8, f"i    :  Inicializar o jogo aleatoriamente")
            self.blit(9, f"space:  Rodar jogo / Pausar jogo {' (pausado)' if self.pause else ' (rodando)'}")
            self.blit(10,f"esc:  Sair")
        pg.display.flip()

    def inicio_aleatorio(self, probabilidade_para_pixel_ativado=PROBABILIDADE_PIXEL_ATIVO):
        for x in range(self.gridlargura):
            for y in range(self.gridaltura):
                if random() < probabilidade_para_pixel_ativado:
                    self.cells[x][y].ativado(self.cor)
                else:
                    self.cells[x][y].desativado()

    def nova_geracao(self):
        temp = []
        for x in range(self.gridlargura):
            temp.append([])
            for y in range(self.gridaltura):
                x_anterior = x-1
                y_anterior = y-1
                proximo_x = (x+1) % self.gridlargura
                proximo_y = (y+1) % self.gridaltura
                value = \
                    self.cells[x_anterior][y_anterior].alive + \
                    self.cells[x_anterior][y].alive + \
                    self.cells[x_anterior][proximo_y].alive + \
                    self.cells[x][y_anterior].alive + \
                    self.cells[x][proximo_y].alive + \
                    self.cells[proximo_x][y_anterior].alive + \
                    self.cells[proximo_x][y].alive + \
                    self.cells[proximo_x][proximo_y].alive
                if self.cells[x][y].alive:
                    if value < 2 or value > 3:
                        temp[x].append(False)
                    else:
                        temp[x].append(True)
                else:
                    if value == 3:
                        temp[x].append(True)
                    else:
                        temp[x].append(False)
        for x in range(self.gridlargura):
            for y in range(self.gridaltura):
                if temp[x][y]:
                    if self.cells[x][y].alive:
                        self.cells[x][y].sobrevive()
                    else:
                        self.cells[x][y].ativado(self.cor)
                else:
                    if self.cells[x][y].alive:
                        self.cells[x][y].desativado(PRETO)

    def eventos(self):
        for evento in pg.event.get():
            if evento.type == pg.QUIT:
                self.quit()
            if evento.type == pg.KEYDOWN:
                if evento.key == pg.K_i:
                    self.inicio_aleatorio()
                if evento.key == pg.K_ESCAPE:
                    self.quit()
                if evento.key == pg.K_SPACE:
                    self.pause = not(self.pause)

            clique = pg.mouse.get_pressed()
            x, y = pg.mouse.get_pos()
            x = int(x / TAMANHO_PIXEL)
            y = int(y / TAMANHO_PIXEL)

            if (clique, x, y) != (self.previous_click, self.previous_x, self.previous_y):
                self.previous_click, self.previous_x, self.previous_y = clique, x, y
                if clique[ESQUERDO] and not self.cells[x][y].alive:
                    self.cells[x][y].ativado(self.cor)
            if evento.type == self.nova_geracao_event and not self.pause:
                self.nova_geracao()

parser = argparse.ArgumentParser()
parser.add_argument("ALTURA", type=int, help="Altura da grid")
parser.add_argument("LARGURA", type=int, help="Largura da grid")
args = parser.parse_args()
ALTURA = args.ALTURA
LARGURA = args.LARGURA
jogo = Jogo()
while True:
    jogo.novo()
    jogo.rodar()
