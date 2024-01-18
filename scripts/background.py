import pygame
from utils.load_images import load_background

class Backgroud:
    
    '''Classe básica para a criação de um background.
    
    Possui métodos para desenhar o background, além de 
    criar uma interação direta com o player para fazer
    efeitos como o parallax.
    
    '''
    
    # Método construtor
    def __init__(self, screen: pygame.Surface):
        
        # Atributos necessários para a configuração do background
        self.screen = screen
        
        # Instancia da classe Sky
        self.sky = Sky(0,0)
        self.sky_list = [] # -> Lista de objetos Sky

        # Instancia da classe Clouds
        self.clouds = Clouds(0,0)
        self.clouds_list = [] # -> Lista de objetos Clouds
        
        # Instancia da classe Sea
        self.sea = Sea(0,0)
        self.sea_list = [] # -> Lista de objetos Sea
        
        # Executa o método create
        self.create()

    # Configura o background
    def create(self):
        
        '''Este método cria e configura cada image que forma o background.
        
        Cada loop for é responsável por preencher uma lista que contém as
        posições iniciais de cada imagem.
        
        Através desta mesma lista futuramente posso acessar o atributo rect
        para movimentar o background e criar um efeito conhecido como efeito 
        parallax.
        
        '''
        
        # Loop for para criar o Sky
        for i in range(self.screen.get_width() // self.sky.width + 1):
            self.sky_list.append(Sky(i * self.sky.width, 0))
            
        # Loop for para criar o Clouds
        for i in range(self.screen.get_width() // self.clouds.width + 1):
            self.clouds_list.append(Clouds(i * self.clouds.width, self.screen.get_height() - self.sky.height))
        
        # Loop for para criar o Sea
        for i in range(self.screen.get_width() // self.sea.width + 1):
            self.sea_list.append(Sea(i * self.sea.width, self.screen.get_height() - self.sea.height))
    
    def update(self):
        pass
        
    # Método que desenha o background
    def draw(self):
        
        '''Para limitar o número de vezes que cada elemento que compõe o
        background é desenhada, utilizo o método get_width para saber o 
        tamanho da tela e logo após chamo o atributo sizes onde tenho 
        armazenado todos os tamanhos de cada imagem do background, então
        faço a divisão inteira e acrescento mais um para garantir que não
        fique nenhuma parte da tela sem ter o background.
        
        '''
        # Loop for que desenha o Sky
        for i in range(len(self.sky_list)):
            self.screen.blit(self.sky_list[i].image, self.sky_list[i].rect)
        
        # Loop for que desenha o Clouds
        for i in range(len(self.clouds_list)):
            self.screen.blit(self.clouds_list[i].image, self.clouds_list[i].rect)
        
        # Loop for que desenha o Sea
        for i in range(len(self.sea_list)):
            self.screen.blit(self.sea_list[i].image, self.sea_list[i].rect)
            
# Classe base para a criação do Sky background
class Sky:
    def __init__(self, x, y):
        self.image = load_background('Sky.png')
        self.rect = self.image.get_rect(topleft = (x, y))
        self.width = self.image.get_width()
        self.height = self.image.get_height()

# Classe base para a criação do Sea background
class Sea:
    def __init__(self, x, y):
        self.image = load_background('Sea.png')
        self.rect = self.image.get_rect(topleft = (x, y))
        self.width = self.image.get_width()
        self.height = self.image.get_height()

# Classe base para a criação do clouds background
class Clouds:
    def __init__(self, x, y):
        self.image = load_background('Clouds.png')
        self.rect = self.image.get_rect(topleft = (x, y))
        self.width = self.image.get_width()
        self.height = self.image.get_height()