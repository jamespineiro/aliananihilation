import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, width, ground_rect):
        super().__init__()
        self.keys = pygame.key.get_pressed()
        self.speed = 4
        self.width = width
        self.ground_rect = ground_rect
        self.gravity = 0
        self.speed = 10
        self.image = pygame.transform.smoothscale_by(pygame.image.load('assets/player/player.png'),(.12,.12)).convert_alpha()
        self.rect = self.image.get_rect(midbottom = (self.width/2, 400))
        self.hitbox = pygame.Rect(self.rect[0] + 70, self.rect[1], self.rect.width//4, self.rect.height - 30)
        self.pressing_space = False
        self.rocket_power = 1.1
        self.celebrating = pygame.transform.smoothscale_by(pygame.image.load('assets/player/player.png'),(.12,.12)).convert_alpha()
        self.dead = False
        self.dead_image = pygame.transform.smoothscale_by(pygame.image.load('assets/player/deadplayer.png'),(.12,.12)).convert_alpha()
        
        # Throwing egg animation
        self.throwing_egg0 = pygame.transform.smoothscale_by(pygame.image.load('assets/player/throwingegg/throwingegg0.png'),(.12,.12)).convert_alpha()
        self.throwing_egg1 = pygame.transform.smoothscale_by(pygame.image.load('assets/player/throwingegg/throwingegg1.png'),(.12,.12)).convert_alpha()
        self.throwing_egg2 = pygame.transform.smoothscale_by(pygame.image.load('assets/player/throwingegg/throwingegg2.png'),(.12,.12)).convert_alpha()
        self.throwing_egg3 = pygame.transform.smoothscale_by(pygame.image.load('assets/player/throwingegg/throwingegg3.png'),(.12,.12)).convert_alpha()
        self.throwing_egg4 = pygame.transform.smoothscale_by(pygame.image.load('assets/player/throwingegg/throwingegg4.png'),(.12,.12)).convert_alpha()
        self.throwing_egg5 = pygame.transform.smoothscale_by(pygame.image.load('assets/player/throwingegg/throwingegg5.png'),(.12,.12)).convert_alpha()
        self.throwing_egg6 = pygame.transform.smoothscale_by(pygame.image.load('assets/player/throwingegg/throwingegg6.png'),(.12,.12)).convert_alpha()
        self.throwing_egg7 = pygame.transform.smoothscale_by(pygame.image.load('assets/player/throwingegg/throwingegg7.png'),(.12,.12)).convert_alpha()
        self.throwing_egg8 = pygame.transform.smoothscale_by(pygame.image.load('assets/player/throwingegg/throwingegg8.png'),(.12,.12)).convert_alpha()
        self.throwing_egg9 = pygame.transform.smoothscale_by(pygame.image.load('assets/player/throwingegg/throwingegg0.png'),(.12,.12)).convert_alpha()
        
        self.throwing_egg_index = 0
        self.throwing_egg_animation_speed = .3
        self.throwing_eggs = [self.throwing_egg0, self.throwing_egg1, self.throwing_egg2,
                              self.throwing_egg3, self.throwing_egg4, self.throwing_egg5,
                              self.throwing_egg6, self.throwing_egg7, self.throwing_egg8,
                              self.throwing_egg9]
        
    def check_for_input(self):
        self.keys = pygame.key.get_pressed()
        if not self.dead:
            if self.hitbox.top < 0:
                self.rect.top = 0
                self.hitbox.top = 0
                self.gravity = 0
                self.pressing_space = False
            else:
                if self.keys[pygame.K_SPACE] and self.hitbox.top > 0:
                    self.gravity -= self.rocket_power
                    self.rect.y -= 1
                    self.hitbox.y -= 1
                    self.pressing_space = True
                else:
                    self.pressing_space = False
            if self.keys[pygame.K_d]:
                self.rect.x += self.speed
                self.hitbox.x += self.speed
            if self.keys[pygame.K_a]:
                self.rect.x -= self.speed
                self.hitbox.x -= self.speed
            if self.rect.right > self.width + 90:
                self.rect.right = self.width + 90
                self.hitbox.right = self.width - 20
            if self.rect.left < -70:
                self.rect.left = -70
                self.hitbox.left = 0
            if self.pressing_space:
                if self.rocket_power < 8:
                    self.rocket_power += .001
            else:
                self.rocket_power = 1.1
            
    def apply_gravity(self):
        if self.rect.bottom < self.ground_rect.top + 20:
            self.gravity += .5
        else:
            self.gravity += .1
            self.rect.bottom = self.ground_rect.top + 20
            self.hitbox.bottom = self.ground_rect.top
        if self.gravity > 1 and self.hitbox.bottom >= self.ground_rect.top:
            self.y_velocity = 0
        self.rect.y += self.gravity
        self.hitbox.y += self.gravity
    
    def animation_state(self):
        if not self.dead:
            self.image = self.throwing_eggs[int(self.throwing_egg_index)]
            self.throwing_egg_index += self.throwing_egg_animation_speed
            if self.throwing_egg_index >= len(self.throwing_eggs):
                self.throwing_egg_index = 0
                self.image = self.throwing_eggs[0]
        else:
            self.image = self.dead_image
    
    def update(self):
        self.check_for_input()
        self.apply_gravity()
        self.animation_state()