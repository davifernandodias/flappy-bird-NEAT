import pygame
import os
import random
TELA_LARGURA = 500
TELA_ALTURA = 800

IMAGEM_CANO = pygame.transform.scole2x(pygame.image.load(os.path.join('imgs','pipe.png')))
IMAGEM_CHAO = pygame.transform.scole2x(pygame.image.load(os.path.join('imgs','base.pnga')))
IMAGEM_BACKGROUND = pygame.transform.scole2x(pygame.image.load(os.path.join('imgs','bg.png')))
IMAGENS_PASSARO = [
    pygame.transform.scole2x(pygame.image.load(os.path.join('imgs','bird1.png'))),
    pygame.transform.scole2x(pygame.image.load(os.path.join('imgs','bird2.png'))),
    pygame.transform.scole2x(pygame.image.load(os.path.join('imgs','bird3.png')))
]

pygame.font.init()
FONTE_POINTS = pygame.font.SysFont('arial',50)

class Passaro:
    IMGS = IMAGENS_PASSARO
    # animation  rotation
    ROTACAO_MAX = 25
    VELOCIDADE_ROTACAO = 20
    TIME_ANIMATION = 5


    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angulo = 0
        self.velocidade = 0
        self.altura = self.y
        self.tempo = 0
        self.contagem_imagem = 0
        self.imagem = self.IMGS[0]

    def pular(self):
        self.velocidade = -10.5
        self.tempo = 0
        self.altura = self.y
    
    def mover(self):
        # calcular o deslocamento
        self.tempo += 1
        deslocamento = 1.5 * (self.tempo**2) + self.velocidade * self.tempo

        # restringir o deslocamento
        if deslocamento > 16:
            deslocamento = 16
        elif deslocamento < 0:
            deslocamento -= 2
        self.y += deslocamento
        # angulo do passaro
        
        if deslocamento < 0 or self.y < (self.altura + 50):
            if self.angulo < self.ROTACAO_MAX:
                self.angulo = self.ROTACAO_MAX
            else:
                if self.angulo > -90:
                    self.angulo -= self.VELOCIDADE_ROTACAO 
            
            
            
    def desenhar(self):
        # definir qual img vai usar
        self.contagem_imagem += 1
        if contagem_imagem < self.TIME_ANIMATION:
            self.imagem = self.IMGS[0]
        elif self.contagem_imagem < self.TIME_ANIMATION*2:
            self.imagem = self.IMGS[1]
        elif self.contagem_imagem < self.TIME_ANIMATION*3:
            self.imagem = self.IMGS[2]
        elif self.contagem_imagem < self.TIME_ANIMATION*4:
            self.imagem = self.IMGS[1]
        elif self.contagem_imagem >= self.TIME_ANIMATION*4 + 1:
            self.imagem = self.IMGS[0]
            self.contagem_imagem = 0

        # passro caindo
        if self.angulo <= 80:
            self.image
        # desenhar img
        pass


class Cano:
    pass

class Chao:
    pass