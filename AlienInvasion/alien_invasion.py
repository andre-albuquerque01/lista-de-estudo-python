import pygame
from settings import Settings
from ship import Ship
import game_funtions as gf
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreBoard import ScoreBoard

def run_game():
    # Inciliza o jogo e cria o objeto na tela
    pygame.init()
    # Instaciar a classe settings
    ai_settings = Settings()
    
    # Criar a janela e chamar os atributos da classe
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    # Titulo da janela
    pygame.display.set_caption("Alien")
    
    # Instaciar a classe ship e cria uma espaçonave
    ship = Ship(screen, ai_settings)
    # Crie um grupo no qual serão armazenados os projetius
    bullets = Group()
    # Criar um grupo de aliengs
    aliens = Group()
    # Cria uma instacia para armazenar dados estatisticos do jogo
    stats = GameStats(ai_settings)
    # Cria o botão play
    play_button = Button(ai_settings, screen, "Play")
    # Cria um painel de pontuação
    sb = ScoreBoard(ai_settings, screen, stats)
    
    gf.creat_fleet(ai_settings, screen, ship, aliens)
    
    # Inicia o principal laço do jogo
    while True:
       
        gf.checkEvent(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, bullets, aliens)        
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
        
        
                
       
    
    
run_game()