import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self, screen, ai_settings):
        """Inicializa a espaçonave e define sua posição inical"""
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        
        # Carrega imagem da espaçonave e obtem seu rect
        self.image = pygame.image.load('AlienInvasion/image/ship.bmp')
        # Cria um retangulo em volta da imagem
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        
        # Inicia cada nova espaçonave em sua posição atual
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        # Armazena um valor decimal para o centro da espaçonave
        self.center = float(self.rect.centerx)
        
        self.moving_right = False
        self.moving_left = False
        
    def update(self):
        """Atualiza a posição da espaçonave de acordo  com a flag de movimento"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        
        # Atualiza o objeto rect de acordo com o self.center
        self.rect.centerx = self.center 
        
    def blitme(self):
        """Desenha a espaçonave em sua posição atual"""
        self.screen.blit(self.image, self.rect)
    
    def center_ship(self):
        """Centraliza a espaçonave na tela"""
        self.center = self.screen_rect.centerx
        