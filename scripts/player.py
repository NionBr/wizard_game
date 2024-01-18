import pygame
from utils.load_images import load_sprites

class Player(pygame.sprite.Sprite):
    
    '''Classe básica para a criação de um player
    
    Contém métodos para criar o objeto player, além de 
    adicionar animação, obter as entradas do teclado para
    fazer a movimentação do player.
    
    Herda da classe Sprite da biblioteca pygame, que serve
    para auxiliar na criação do player.
    
    '''
    
    # Método construtor
    def __init__(self, x, y, width, height):
        super().__init__()
        
        # Carrega todos os sprites do player
        self.sprite_list = load_sprites('images', 'lightning_mage', 128, 128, True)
        
        # Atributos de configuração do player
        self.direction = '_right'
        self.status = 'Idle'
        self.x_vel = 0
        self.move_speed = 4
        self.animation_count = 0
        
        # Atributos ligados a animação de ataque 
        self.attack_hit = 0
        self.is_attack = False
        
        # Defini um frame inicial para o player
        self.image = self.sprite_list[self.status + self.direction][0]
        # Define o retangulo para facilitar a movimentação do player
        self.rect = pygame.Rect(x, y, width, height)
        
        
    '''------------------------------------------------------
    Métodos responsáveis pela movimentaçãoe atualização 
    dos status do player.
    
    Se o player estiver virado para a esquerda o método
    move_right vai modificar o seu estatos para a direita
    além de fazer com que ele se mova para a direita, e vice
    e versa com o método move_left.
    
    '''    
    # Move o player poara a direita
    def move_right(self, speed):
        self.x_vel = speed
        if self.direction != '_right':
            self.direction = '_right'
            self.animation_count = 0
    
    # Move o player poara a esquerda
    def move_left(self, speed):
        self.x_vel = -speed
        if self.direction != '_left':
            self.direction = '_left'
            self.animation_count = 0
    
    # O método move é responsável por fazer o movimento vertical
    # e horizontal do player
    def move(self, dx):
        self.rect.x += dx
            
    '''------------------------------------------------------'''
    
    # Método que faz o player realizar o ataque
    def attack(self):
        # Altera o estado do player para o estado de ataque
        self.is_attack = True
        # Alterna do primeiro ataque para o segundo caso
        # a tecla z seja pressionada mais de uma vez
        if self.attack_hit == 0:
            self.animation_count = 0
            self.attack_hit = 1
        elif self.is_attack == True and self.animation_count >= 9:
            self.attack_animation_correction()
            self.animation_count = 0
            self.attack_hit = 2
    
    def attack_animation_correction(self):
        
        '''Método feito para corrigir um erro na transição das
        demais animações para para a animação de ataque.
        
        O método é necessário, pois a biblioteca pygame não possui
        ferramentas para uma melhor detecção de pixel.
        
        '''
        # Verifica a direção do player
        if self.is_attack == True:
            if self.direction == '_right':
                self.rect.x += 18
            elif self.direction == '_left':
                self.rect.x -= 18
           
    # Método responsável por fazer a animação do player 
    def animate(self):
        
        '''--------------------------------------------------
        Esta sequencia de operadores condicionais verifica 
        e atualizao status da animação do player.
        
        '''
        if self.x_vel == 0 and self.is_attack == False:
            self.status = 'Idle'
        elif self.attack_hit == 1:
            self.status = 'Attack_1'
        elif self.attack_hit >= 1:
            self.status = 'Attack_2'
        elif self.x_vel != 0:
            self.status = 'Run'
        '''--------------------------------------------------'''
        
        # Incrementa valor ao animation_count
        if self.status != 'Attack_1':
            # Velocidade padrão para demais animações
            self.animation_count += 0.15
        else:
            # Defini uma atualização de frames mais rápida
            # para a animação de ataque
            self.animation_count += 0.25
            
        '''----------------------------------------------------------------------------
        Este laço condicional faz com que a animação execute em loop.
        
        Além disso também reseta os atributos attack_hit e is_attack para
        o seu estado inicial.
        
        '''
        if self.animation_count >= len(self.sprite_list[self.status + self.direction]):
            self.animation_count = 0
            self.attack_hit = 0
            self.is_attack = False
        '''----------------------------------------------------------------------------'''
        
        # Adiciona o novo frame da animação
        self.image = self.sprite_list[self.status + self.direction][int(self.animation_count)]
    
    # Método que capta as entrdas do teclado
    def get_input(self):
        
        # Obtem a tecla no momento em que é pressionada
        keys = pygame.key.get_pressed()
        
        # Adiciona a velocidade do eixo de x para 0
        self.x_vel = 0 
        # Verifica se o player está atacando
        if self.is_attack == False:
            # Caso o player não esteja atacando ele pode correr
            # ou para a direita ou para a esquerda
            if keys[pygame.K_RIGHT]:
                self.move_right(self.move_speed)
            elif keys[pygame.K_LEFT]:
                self.move_left(self.move_speed)
        
        # Faz o player atacar
        if keys[pygame.K_z]:
            self.attack()
    
    # Método que atualiza o player a cada frame
    def update(self):
        self.get_input()
        self.animate()
        self.move(self.x_vel)
    
    # Método que desenha o player na tela
    def draw(self, screen: pygame.Surface):
        screen.blit(self.image, self.rect)