import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep

def check_down_events(event, ai_settings, screen, ship, bullets):
    """Responde a pressionamento de teclas"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
            # Direção esquerda
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True 
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()
        
        
        
def check_keyup_events(event, ship):
    # Responde a soltura de teclas
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False 
        
def checkEvent(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button):
    """Responder o evento pressionamento de teclas e de mouse"""
     # Eventos de teclado e de mouse
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # Move para a direita
        elif event.type == pygame.KEYDOWN:
            check_down_events(event, ai_settings, screen, ship, bullets)
        # Solta a tecla e para a nave
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button, mouse_x, mouse_y)
            
def check_play_button(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button, mouse_x, mouse_y):
    """Inicia um novo jogo quando o jogador clicar no play"""
   
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
   
    if button_clicked and not stats.game_active:
        # Ocuta o curso
        pygame.mouse.set_visible(False)
        
        # Reinicia os dados estatiscos do jogo 
        stats.reset_stats()
        stats.game_active = True
        ai_settings.initialize_dynamic_settings()
        
        # Reinicia as imagens do painel da pontuação
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()
        
        # Esvazia a lista de alien e de projeteis
        aliens.empty()
        bullets.empty()
        
        # Cria uma nova frota e centraliza a espaçonave
        creat_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
            
def  update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button):
    # Redesenhar a tela a cada passagem do loop
    screen.fill(ai_settings.bg_color)        
        
    # Redesenha todos os projeteis atrás da espaçonave e dos alings
    for bullet in bullets.sprites():
        bullet.draw_bullet()
        
    ship.blitme()
    aliens.draw(screen)
    
    # Desenha a informação sobre a pontuação 
    sb.show_score()
    
    # Desenha o botão play se o jogo estiver inativo
    if not stats.game_active:
        play_button.draw_button()
        
    # Deixa a tela mais recente visivel, sempre atualizando
    pygame.display.flip()
    
            
def check_bullet_alien_collision(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Responde a colisões entre projeteis e alien"""
    # Remove qualque projetil e aling que tenha colidido
    collision = pygame.sprite.groupcollide(bullets, aliens, True, True)
    
    if len(aliens) == 0:
        # Se a frota toda for destruida, inicia um novo nível
        bullets.empty()
        ai_settings.increase_speed()
        
        # Aumenta o nível
        stats.level += 1
        sb.prep_level()
        
        creat_fleet(ai_settings, screen, ship, aliens)
    
    if collision:
        for aliens in collision.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
        
        check_high_score(stats, sb)
            
def update_bullets(ai_settings, screen, stats, sb, ship, bullets, aliens):
    bullets.update()
    # Remove os projeteis que desparecem
    for bullet in bullets.copy():
        if bullet.rect.bottom <=0:
            bullets.remove(bullet)
    check_bullet_alien_collision(ai_settings, screen, stats, sb, ship, aliens, bullets)
    
            
def fire_bullet(ai_settings, screen, ship, bullets):
    # Cria um novo projetil e adiciona ao topo de projeteis e limitar 
    if len(bullets) < ai_settings.bullets_allowed: 
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
 
def get_number_rows(ai_settings, ship_height, alien_height):
    """Determina o número de aliens que cabe na tela"""       
    available_space_y = (ai_settings.screen_height - (3 * alien_height - ship_height))
    number_row = int(available_space_y / (2 * alien_height))
    return number_row

def get_number_aliens_x(ai_settings, alien_width):
    """Determina o número que cabem na linha"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_alien_x = int(available_space_x / (2 * alien_width))
    return number_alien_x

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    # Cria um alieng e posiciona na linha
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    alien.rect.x = alien.x
    aliens.add(alien)
    
def creat_fleet(ai_settings, screen, ship, aliens):
    """Crie uma frota de aliengs"""
    # Crie um alieng e calcula o número de aliegns em uma linha
    # O espaçamento entre os aliengs é igual à largura de um alieng
    alien = Alien(ai_settings, screen)
    number_alien_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_row = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    
    # Cria a primeira linha de aliengs
    for row_number in range(number_row):
        for alien_number in range(number_alien_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)
            
def  check_fleet_edges(ai_settings, aliens):
    """Responde se algum alien alcançou alguma borda"""
    for alien  in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break
def change_fleet_direction(ai_settings, aliens):
    """Faz toda a frota descer e muda a sua direção"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1   
            
def ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Responde ao fato de espaçonave ter sido atingido por um alien"""
    if stats.ships_left > 0:
        # Decrementa ship_left
        stats.ships_left -= 1
        
        # Atualiza o painel de pontuações
        sb.prep_ships()
        
        # Esvazia a lista de aliengs e de projeteis
        aliens.empty()
        bullets.empty()
        
        # Cria uma nova frota e centraliza a espaçonave
        creat_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
        
        # Faz uma pausa
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)
    
def check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Verifica se algum aling  alcançou a parte inferior da tela"""
    screen_rect = screen.get_rect()
    
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # Trata esse caso do mesmo modo que é feito quando a espaçonave é atingida
            ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)
            break
        
def update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Verifica se a frota está em uma das bordas e então atualiza as posições de todos os aliens da frota"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    
    # Verifica se houve colisões entre aliens e a espaçonave
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets) 
    
    # Verifica se há algum alien que atingiu a parte inferior da tela
    check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets)

def check_high_score(stats, sb):
    """Verifica se há uma nova pontuação"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()