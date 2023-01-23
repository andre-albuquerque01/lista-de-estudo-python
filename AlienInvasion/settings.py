class Settings:
    """Uma classe  para armazenar todas as configurações"""
    
    def __init__(self):
        """Incializa as configurações do jogo"""
        # Configurão da tela
        # Configura largura
        self.screen_width = 900
        # Configura altura
        self.screen_height = 600
        self.bg_color = (230,230,230)
        
        # Configuraçoes da espaçonave
        self.ship_limit = 2
        
        # Configurações do projetius
        self.bullet_width = 3
        self.bullet_height = 5
        self.bullet_color = (0,0,0)
        self.bullets_allowed = 5
        
        # Configurações dos aliens
        self.fleet_drop_speed = 10
        
        
        # A taxa com que a velocidade do jogo aumenta
        self.speedup_scale = 1.1
        
        self.initialize_dynamic_settings()
        
        
    def initialize_dynamic_settings(self):
        """Inicializa a configuração que mudam no decorrer do jogo"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 2
        self.alien_speed_factor = 1
        
        # Pontuação
        self.alien_points = 50
        
        # fleet_direction igual a 1 representa  a direta; -1 representa a esquerda
        self.fleet_direction = 1
        
        # A taxa com que os pontos para cada alien aumentam
        self.score_scale = 1.5
        
    def increase_speed(self):
        """Aumenta as configurações de velocidade"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        
        self.alien_points = int(self.alien_points * self.score_scale)