import pygame
from random import randint

class Alien(pygame.sprite.Sprite):
    def __init__(self, screen, width, height, player):
        super().__init__()
        self.width = width
        self.height = height
        self.screen = screen
        self.player = player
        self.image = pygame.transform.smoothscale_by(pygame.image.load('assets/alien/ufo.png'), (.2, .2)).convert_alpha()
        self.rect = self.image.get_rect(bottomleft = (self.width-450, self.height/2 + 150))
        self.hitbox1 = pygame.Rect(self.rect.x + 30, self.rect.y + 230, self.rect.width - 50, self.rect.height//4)
        self.hitbox2 = pygame.Rect(self.rect.x + 180, self.rect.y + 10, self.rect.width//7, self.rect.height//7)
        self.hitbox3 = pygame.Rect(self.rect.x + 190, self.rect.y + 10, self.rect.width//12, self.rect.height//4)
        self.hitbox4 = pygame.Rect(self.rect.x + 130, self.rect.y + 130, self.rect.width//3 + 40, self.rect.height//4)
        self.hitboxes = [self.hitbox1, self.hitbox2, self.hitbox3, self.hitbox4]
        self.health = 50
        
        self.just_attacked = True
        
        self.stage1 = True
        self.image_crack1 = pygame.transform.smoothscale_by(pygame.image.load('assets/alien/ufocrack1.png'), (.2, .2)).convert_alpha()
        self.image_crack2 = pygame.transform.smoothscale_by(pygame.image.load('assets/alien/ufocrack2.png'), (.2, .2)).convert_alpha()
        self.image_crack3 = pygame.transform.smoothscale_by(pygame.image.load('assets/alien/ufocrack3.png'), (.2, .2)).convert_alpha()
        self.image_crack4 = pygame.transform.smoothscale_by(pygame.image.load('assets/alien/ufocrack4.png'), (.2, .2)).convert_alpha()
        
        self.image2_crack1 = pygame.transform.smoothscale_by(pygame.image.load('assets/alien/ufo2crack1.png'), (.2, .2)).convert_alpha()
        self.image2_crack2 = pygame.transform.smoothscale_by(pygame.image.load('assets/alien/ufo2crack2.png'), (.2, .2)).convert_alpha()
        self.image2_crack3 = pygame.transform.smoothscale_by(pygame.image.load('assets/alien/ufo2crack3.png'), (.2, .2)).convert_alpha()
        self.image2_crack4 = pygame.transform.smoothscale_by(pygame.image.load('assets/alien/ufo2crack4.png'), (.2, .2)).convert_alpha()
        
        self.image3_crack1 = pygame.transform.smoothscale_by(pygame.image.load('assets/alien/ufo3crack1.png'), (.2, .2)).convert_alpha()
        self.image3_crack2 = pygame.transform.smoothscale_by(pygame.image.load('assets/alien/ufo3crack2.png'), (.2, .2)).convert_alpha()
        self.image3_crack3 = pygame.transform.smoothscale_by(pygame.image.load('assets/alien/ufo3crack3.png'), (.2, .2)).convert_alpha()
        self.image3_crack4 = pygame.transform.smoothscale_by(pygame.image.load('assets/alien/ufo3crack4.png'), (.2, .2)).convert_alpha()
        
        self.stage2 = False
        self.stage3 = False
        self.hover_speed = 0
        self.hover_addition = .3
        
        self.attack_counter = 0
        self.attack_counter_max = 150
        self.attacking = False
        self.active_red_attack = False
        
        self.active_attacks = [self.active_red_attack]
        self.attack_cycles = 0
        
        self.neutral = pygame.transform.smoothscale_by(pygame.image.load('assets/alien/antenna/stage1antennas/stage1antenna.png'), (.2, .2)).convert_alpha()
        self.antenna = pygame.transform.smoothscale_by(pygame.image.load('assets/alien/antenna/stage1antennas/stage1antenna.png'), (.2, .2)).convert_alpha()
        
        self.antenna_speed = .1
        self.attacks = ['red', 'green', 'yellow']
        self.random = randint(0,2)
        self.attack = self.attacks[self.random]
        
        self.red1 = pygame.transform.smoothscale_by(pygame.image.load('assets/alien/antenna/stage1antennas/red/red1.png'), (.2, .2)).convert_alpha()
        self.red2 = pygame.transform.smoothscale_by(pygame.image.load('assets/alien/antenna/stage1antennas/red/red2.png'), (.2, .2)).convert_alpha()
        self.red3 = pygame.transform.smoothscale_by(pygame.image.load('assets/alien/antenna/stage1antennas/red/red3.png'), (.2, .2)).convert_alpha()
        self.red4 = pygame.transform.smoothscale_by(pygame.image.load('assets/alien/antenna/stage1antennas/red/red4.png'), (.2, .2)).convert_alpha()
        self.red5 = pygame.transform.smoothscale_by(pygame.image.load('assets/alien/antenna/stage1antennas/red/red5.png'), (.2, .2)).convert_alpha()
        
        self.reds = [self.neutral, self.red1, self.red2, self.red3, self.red4, self.red5, self.red5, self.red5]
        self.red_index = 0
        
        self.green1 = pygame.transform.smoothscale_by(pygame.image.load('assets/alien/antenna/stage1antennas/green/green1.png'), (.2, .2)).convert_alpha()
        self.green2 = pygame.transform.smoothscale_by(pygame.image.load('assets/alien/antenna/stage1antennas/green/green2.png'), (.2, .2)).convert_alpha()
        self.green3 = pygame.transform.smoothscale_by(pygame.image.load('assets/alien/antenna/stage1antennas/green/green3.png'), (.2, .2)).convert_alpha()
        self.green4 = pygame.transform.smoothscale_by(pygame.image.load('assets/alien/antenna/stage1antennas/green/green4.png'), (.2, .2)).convert_alpha()
        self.green5 = pygame.transform.smoothscale_by(pygame.image.load('assets/alien/antenna/stage1antennas/green/green5.png'), (.2, .2)).convert_alpha()
        
        self.greens = [self.neutral, self.green1, self.green2, self.green3, self.green4, self.green5, self.green5, self.green5]
        self.green_index = 0
        
        self.prebeam = pygame.transform.smoothscale_by(pygame.image.load('assets/alien/greenbeam/soontobeam.png'), (.4, .4)).convert_alpha()
        self.beam = pygame.transform.smoothscale_by(pygame.image.load('assets/alien/greenbeam/beam.png'), (.4, .4)).convert_alpha()
        self.beam_rect = self.prebeam.get_rect(midtop = (randint(400, 700), 0))
        
        self.yellow1 = pygame.transform.smoothscale_by(pygame.image.load('assets/alien/antenna/stage1antennas/yellow/yellow1.png'), (.2, .2)).convert_alpha()
        self.yellow2 = pygame.transform.smoothscale_by(pygame.image.load('assets/alien/antenna/stage1antennas/yellow/yellow2.png'), (.2, .2)).convert_alpha()
        self.yellow3 = pygame.transform.smoothscale_by(pygame.image.load('assets/alien/antenna/stage1antennas/yellow/yellow3.png'), (.2, .2)).convert_alpha()
        self.yellow4 = pygame.transform.smoothscale_by(pygame.image.load('assets/alien/antenna/stage1antennas/yellow/yellow4.png'), (.2, .2)).convert_alpha()
        self.yellow5 = pygame.transform.smoothscale_by(pygame.image.load('assets/alien/antenna/stage1antennas/yellow/yellow5.png'), (.2, .2)).convert_alpha()
        
        self.yellows = [self.neutral, self.yellow1, self.yellow2, self.yellow3, self.yellow4, self.yellow5, self.yellow5, self.yellow5]
        self.yellow_index = 0
        
        self.yellow_prebeam = pygame.transform.smoothscale_by(pygame.image.load('assets/alien/beam/prebeam.png'), (1, 1)).convert_alpha()
        self.yellow_beam = pygame.transform.smoothscale_by(pygame.image.load('assets/alien/beam/beam.png'), (1, 1)).convert_alpha()
        self.yellow_beam_rect = self.yellow_beam.get_rect(midleft = (0, height/2))
        
        self.pellet = pygame.transform.smoothscale_by(pygame.image.load('assets/alien/pellet.png'), (.2, .2)).convert_alpha()
        self.pellet_rect = self.pellet.get_rect(center = (-100,-100))
        self.pellet_hitbox = pygame.Rect(self.pellet_rect[0], self.pellet_rect[1], 20, 20)
        self.pellet_speed = -2
        self.pellet2 = pygame.transform.smoothscale_by(pygame.image.load('assets/alien/pellet.png'), (.2, .2)).convert_alpha()
        self.pellet2_rect = self.pellet2.get_rect(center = (-100,-100))
        self.pellet2_hitbox = pygame.Rect(self.pellet2_rect[0], self.pellet2_rect[1], 20, 20)
        self.pellet2_speed = -2
        self.pellet3 = pygame.transform.smoothscale_by(pygame.image.load('assets/alien/pellet.png'), (.2, .2)).convert_alpha()
        self.pellet3_rect = self.pellet3.get_rect(center = (-100,-100))
        self.pellet3_hitbox = pygame.Rect(self.pellet3_rect[0], self.pellet3_rect[1], 20, 20)
        self.pellet3_speed = -2
        self.just_shot = False
        
        pygame.mixer.init()
    
        self.pew = pygame.mixer.Sound('UI_Sound/pew.wav')
        self.pew.set_volume(1.2)
        self.glass_crack = pygame.mixer.Sound('UI_Sound/glasscrack.wav')
        self.glass_crack.set_volume(1.3)
        self.crack1 = False
        self.crack2 = False
        self.crack3 = False
        self.crack4 = False
        self.glass_break = pygame.mixer.Sound('UI_Sound/glassbreak.wav')
        self.glass_breaking = False
        self.boing_sound = pygame.mixer.Sound('UI_Sound/boing.wav')
        self.boing_sound.set_volume(.5)
        self.boing1 = False
        self.boing2 = False
        self.boing3 = False
        self.boing4 = False
        self.cracking = pygame.mixer.Sound('UI_Sound/cracking.wav')
        self.cracking1 = False
        self.cracking2 = False
        self.cracking3 = False
        self.cracking4 = False
        self.fire_loop = pygame.mixer.Sound('UI_Sound/fireloop.wav')
        self.fire_looping = False
        self.explosion = pygame.mixer.Sound("UI_Sound/explosion.wav")
        self.exploded = False
        
    def hover(self):
        if not self.active_red_attack:
            if not self.attacking:
                if not self.just_attacked and not self.active_red_attack:
                    self.rect.y += self.hover_speed
                    self.hover_speed += self.hover_addition
                else:
                    if self.rect.bottom >= self.height/2 + 300:
                        self.rect.bottom -= 8
                    elif self.rect.top <= 50:
                        self.rect.top += 8
                self.hitbox1.y = self.rect.y + 230
                self.hitbox2.y = self.rect.y + 10
                self.hitbox3.y = self.rect.y + 10
                self.hitbox4.y = self.rect.y + 130
                if self.rect.bottom >= self.height/2 + 300 or self.rect.top <= 50:
                    if not self.just_attacked:
                        self.hover_addition *= -1
                        self.hover_speed *= -1
                        if self.rect.bottom >= self.height/2 + 300:
                            self.rect.bottom = self.height/2 + 299
                            self.hover_speed /= 8
                        else:
                            self.rect.top = 51
                            self.hover_speed /= 8
                else:
                    if self.just_attacked:
                        self.just_attacked = False
            elif self.attacking and not self.active_red_attack and self.attack == 'red':
                if self.player.rect.bottom > self.height/2:
                    if self.hitbox2.top > self.player.hitbox.bottom:
                        self.rect.y -= 6
                        self.hitbox1.y = self.rect.y + 230
                        self.hitbox2.y = self.rect.y + 10
                        self.hitbox3.y = self.rect.y + 10
                        self.hitbox4.y = self.rect.y + 130
                    else:
                        self.rect.y += 6
                        self.hitbox1.y = self.rect.y + 230
                        self.hitbox2.y = self.rect.y + 10
                        self.hitbox3.y = self.rect.y + 10
                        self.hitbox4.y = self.rect.y + 130
                
    def update_image_in_stage(self):
        if self.stage1:
            if self.health == 40:
                if not self.crack1:
                    self.glass_crack.play()
                    self.crack1 = True
                self.image = self.image_crack1
            elif self.health == 30:
                if not self.crack2:
                    self.glass_crack.play()
                    self.crack2 = True
                self.image = self.image_crack2
            elif self.health == 20:
                if not self.crack3:
                    self.glass_crack.play()
                    self.crack3 = True
                self.image = self.image_crack3
            elif self.health == 10:
                if not self.crack4:
                    self.glass_crack.play()
                    self.crack4 = True
                self.image = self.image_crack4
        elif self.stage2:
            if self.health == 40:
                if not self.boing1:
                    self.boing_sound.play()
                    self.boing1 = True
                self.image = self.image2_crack1
            elif self.health == 30:
                if not self.boing2:
                    self.boing_sound.play()
                    self.boing2 = True
                self.image = self.image2_crack2
            elif self.health == 20:
                if not self.boing3:
                    self.boing_sound.play()
                    self.boing3 = True
                self.image = self.image2_crack3
            elif self.health == 10:
                if not self.boing4:
                    self.boing_sound.play()
                    self.boing4 = True
                self.image = self.image2_crack4
        elif self.stage3:
            if self.health == 40:
                if not self.cracking1:
                    self.cracking.play()
                    self.cracking1 = True
                self.image = self.image3_crack1
            elif self.health == 30:
                if not self.cracking2:
                    self.cracking.play()
                    self.cracking2 = True
                self.image = self.image3_crack2
            elif self.health == 20:
                if not self.cracking3:
                    self.cracking.play()
                    self.cracking3 = True
                self.image = self.image3_crack3
            elif self.health == 10:
                if not self.cracking4:
                    self.cracking.play()
                    self.cracking4 = True
                self.image = self.image3_crack4
            elif self.health <= 0:
                self.image = pygame.transform.smoothscale_by(pygame.image.load('assets/alien/ufolose.png'), (.2, .2)).convert_alpha()
        self.screen.blit(self.antenna, self.rect)
        
    def prepare_for_attack(self):
        if self.attack == 'red':
            if self.attack_cycles < 3:
                self.attack_counter += 1
                if self.attack_counter >= self.attack_counter_max:
                    self.attacking = True
                    self.red_index += self.antenna_speed
                    if self.red_index >= len(self.reds):
                        self.red_index = 0
                        self.attack_counter = 0
                        self.attack_cycles += 1
                        self.attacking = False
                        self.active_red_attack = False
                    elif int(self.red_index) > 4:
                        self.active_red_attack = True
                        self.just_attacked = True
                self.antenna = self.reds[int(self.red_index)]
            else:
                #self.attacks.remove('red')
                self.random = randint(1,2)
                self.attack = self.attacks[self.random]
                self.attack_cycles = 0
        elif self.attack == 'green':
            if self.attack_cycles < 3:
                self.attack_counter += 1
                if self.attack_counter >= self.attack_counter_max:
                    self.attacking = True
                    self.green_index += self.antenna_speed
                    if self.green_index >= len(self.greens):
                        self.green_index = 0
                        self.attack_counter = 0
                        self.attack_cycles += 1
                        self.beam_rect = self.prebeam.get_rect(midtop = (randint(400, 700), 0))
                        self.attacking = False
                        self.active_green_attack = False
                    elif int(self.green_index) > 4:
                        self.active_green_attack = True
                        self.just_attacked = True
                self.antenna = self.greens[int(self.green_index)]
            else:
                #self.attacks.remove('red')
                self.random = randint(0,1)
                if self.random == 0:
                    self.attack = 'red'
                else:
                    self.attack = 'yellow'
                self.attack_cycles = 0
        elif self.attack == 'yellow':
            if self.attack_cycles < 3:
                self.attack_counter += 1
                if self.attack_counter >= self.attack_counter_max:
                    self.attacking = True
                    self.yellow_index += self.antenna_speed
                    if self.yellow_index >= len(self.yellows):
                        self.yellow_index = 0
                        self.attack_counter = 0
                        self.attack_cycles += 1
                        self.attacking = False
                        self.active_yellow_attack = False
                    elif int(self.yellow_index) > 4:
                        self.active_yellow_attack = True
                        self.just_attacked = True
                self.antenna = self.yellows[int(self.yellow_index)]
            else:
                #self.attacks.remove('red')
                self.random = randint(0,1)
                self.attack = self.attacks[self.random]
                self.attack_cycles = 0
        if self.health == 0 and self.stage1:
            if not self.glass_breaking:
                self.glass_break.play()
                self.glass_breaking = True
            self.image = pygame.transform.smoothscale_by(pygame.image.load('assets/alien/ufostage2.png'), (.2, .2)).convert_alpha()
            self.health = 50
            self.stage1 = False
            self.stage2 = True
        if self.health == 0 and self.stage2:
            self.image = pygame.transform.smoothscale_by(pygame.image.load('assets/alien/ufostage3.png'), (.2, .2)).convert_alpha()
            if not self.fire_looping:
                self.fire_loop.play(loops = -1)
                self.fire_looping = True
            if not self.exploded:
                self.explosion.play()
            self.health = 50
            self.attack_counter_max = 75
            self.stage2 = False
            self.stage3 = True
        if (self.stage2 or self.stage3) and self.attack_counter == 0 and not self.just_shot:
            if self.pellet_rect.right < 0:
                if self.stage3:
                    self.pellet = pygame.transform.smoothscale_by(pygame.image.load('assets/alien/pellet2.png'), (.2, .2)).convert_alpha()
                    self.pellet_speed = -4
                self.pellet_rect.x = self.rect[0]
                self.pellet_rect.y = self.rect[1]
                self.pellet_hitbox.x = self.rect[0] + 53
                self.pellet_hitbox.y = self.rect[1] + 145
                self.pew.play()
            elif self.pellet2_rect.right < 0:
                if self.stage3:
                    self.pellet2 = pygame.transform.smoothscale_by(pygame.image.load('assets/alien/pellet2.png'), (.2, .2)).convert_alpha()
                    self.pellet2_speed = -4
                self.pellet2_rect.x = self.rect[0]
                self.pellet2_rect.y = self.rect[1]
                self.pellet2_hitbox.x = self.rect[0] + 53
                self.pellet2_hitbox.y = self.rect[1] + 145
                self.pew.play()
            elif self.pellet3_rect.right < 0:
                if self.stage3:
                    self.pellet3 = pygame.transform.smoothscale_by(pygame.image.load('assets/alien/pellet2.png'), (.2, .2)).convert_alpha()
                    self.pellet3_speed = -4
                self.pellet3_rect.x = self.rect[0]
                self.pellet3_rect.y = self.rect[1]
                self.pellet3_hitbox.x = self.rect[0] + 53
                self.pellet3_hitbox.y = self.rect[1] + 145
                self.pew.play()
            self.just_shot = True
        else: 
            self.just_shot = False
        
    def update(self):
        self.prepare_for_attack()
        self.update_image_in_stage()
        if not (self.stage3 and self.health <= 0):
            self.hover()
        else:
            self.rect.y += 3
            self.hitbox1.y = self.rect.y + 230
            self.hitbox2.y = self.rect.y + 10
            self.hitbox3.y = self.rect.y + 10
            self.hitbox4.y = self.rect.y + 130
            