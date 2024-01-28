import pygame
from scripts.player import Player
from scripts.background import Backgroud
from scripts.level import Level

class Game:
    def __init__(self):

        # Inicia o pygame 
        pygame.init()

        # Configurações iniciais
        self.screen = pygame.display.set_mode((1200, 700))
        self.clock = pygame.time.Clock()

        # Instância do player
        self.player = Player(200, 475, 128, 128)
        # Instância do background
        self.background = Backgroud(self.screen)
        
        self.level = Level(self.screen)
    
    # Desenha todos os elementos da tela
    def draw_screnn(self):
        # Denha o background
        self.background.draw()
        self.background.parallax(self.player.x_vel)
        
        self.level.draw()
                
        # Desenha e atualiza o player a cada quadro
        self.player.draw(self.screen)
        self.player.update()
        
    # Método que executa o game
    def run(self):
        # Loop principal do jogo
        while True:
            
            # Desenha todos os detalhes na tela
            self.draw_screnn()
            
            # Loop de eventos 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit
                    exit()
        
            pygame.display.update()
            self.clock.tick(60)
            
if __name__ == '__main__':
    game = Game()
    game.run()