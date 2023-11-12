import pygame

class Egg(pygame.sprite.Sprite):
    def __init__(self, width, height, player):
        super().__init__()
        self.width = width
        self.height = height
        self.image = pygame.transform.smoothscale_by(pygame.image.load('assets/egg/egg.png'),(.12,.12)).convert_alpha()
        self.splat = pygame.transform.smoothscale_by(pygame.image.load('assets/egg/eggsplat.png'),(.12,.12)).convert_alpha()
        self.rect = self.image.get_rect(midbottom = (player.rect.midbottom))
        self.hitbox = pygame.Rect(self.rect[0] + 137,self.rect[1] + 128, 10, 10)
        self.speed = 10
        self.gravity = -9
        self.gravity_change = .5
        self.despawning_timer = 0
        self.despawning = False
        self.despawned = False
        self.dealt_damage = False
        
    def apply_gravity(self):
        if self.hitbox.bottom < self.height and not self.despawning:
            self.rect.y += self.gravity
            self.hitbox.y += self.gravity
            self.gravity += self.gravity_change
            self.rect.x += self.speed
            self.hitbox.x += self.speed
        else:
            self.gravity = 0
            self.image = self.splat
            self.despawning = True
        if self.despawning:
            self.despawning_timer += 1
        if self.hitbox.right < 0 or self.despawning_timer > 50:
            self.kill()
            self.despawned = True
        
    def update(self):
        self.apply_gravity()