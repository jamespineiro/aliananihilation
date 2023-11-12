import pygame
from player import Player
from alien import Alien
from egg import Egg
from sys import exit
from random import randint

if __name__ == "__main__":
    
    # Initializing video settings
    pygame.init()
    pygame.display.init()
    pygame.display.set_caption('HackUMass 2023')
    
    screen = pygame.display.set_mode((1280,720), vsync = 1)
    width, height = screen.get_size()
    clock = pygame.time.Clock()
    keys = pygame.key.get_pressed()
    
    # Creating an easier, more controlled way of creating images
    def load_image(directory, scale_width = 1, scale_height = 1, x_pos = 0, y_pos = 0, has_hitbox = False):
        image = pygame.transform.smoothscale_by(pygame.image.load(f'assets/{directory}'), (scale_width, scale_height)).convert_alpha()
        rect = image.get_rect(bottomleft = (x_pos, y_pos))
        if has_hitbox:
            hitbox = pygame.Rect(rect.x, rect.y, rect.width, rect.height)
        else:
            hitbox = None
        return image, rect, hitbox
    
    # Game states
    running = True
    title = True
    story = False
    ingame = False
    postgame = False
    endstory = False
    lost = False
    
    temp_ground = pygame.Rect(0,height,width,height)
    
    # Creating the player
    
    player_group = pygame.sprite.GroupSingle()
    player = Player(width, temp_ground)
    player_group.add(player)
    
    alien_group = pygame.sprite.GroupSingle()
    alien = Alien(screen, width, height, player)
    
    tree1, tree1_rect, tree1_hitbox = load_image('environment/tree.png', .25, .25, width/2 - 400, temp_ground.top, False)
    tree2, tree2_rect, tree2_hitbox = load_image('environment/tree.png', .25, .25, width/2 - 800, temp_ground.top, False)
    tree3, tree3_rect, tree3_hitbox = load_image('environment/tree.png', .25, .25, width/2, temp_ground.top, False)
    tree4, tree4_rect, tree4_hitbox = load_image('environment/tree.png', .25, .25, width/2 + 400, temp_ground.top, False)
    
    trees = [tree1, tree2, tree3, tree4]
    tree_rects = [tree1_rect, tree2_rect, tree3_rect, tree4_rect]
    
    egg_group = pygame.sprite.Group()
    
    eggs = []
    egg_thrown = False
    
    leaf_blower_wind, leaf_blower_wind_rect, leaf_blower_wind_hitbox = load_image('player/leafblowerwind.png', .05, .05, player.hitbox.left, height, False)
    
    title_screen1, title_screen1_rect, title_screen1_hitbox = load_image('title/titlescreen1.png',1,1,0,height,False)
    title_screen2, title_screen2_rect, title_screen2_hitbox = load_image('title/titlescreen2.png',1,1,0,height,False)
    play_selected = False
    play_rect = pygame.Rect(width/2-190, height/2 - 100, 250, 130)
    
    story1, story1_rect, story1_hitbox = load_image('story/story1.png',1,1,0,height,False)
    story2, story2_rect, story2_hitbox = load_image('story/story2.png',1,1,width,height,False)
    story3, story3_rect, story3_hitbox = load_image('story/story3.png',1,1,width,height,False)
    story4, story4_rect, story4_hitbox = load_image('story/story4.png',1,1,width,height,False)
    story5, story5_rect, story5_hitbox = load_image('story/story5.png',1,1,width,height,False)
    story6, story6_rect, story6_hitbox = load_image('story/story6.png',1,1,width,height,False)
    
    story_number = 0
    story_pressed = False
    story_moving = False
    stories = [story1, story2, story3, story4, story5, story6]
    story_rects = [story1_rect, story2_rect, story3_rect, story4_rect, story5_rect, story6_rect]
    
    story7, story7_rect, story7_hitbox = load_image('story/story7.png',1,1,0,height,False)
    story8, story8_rect, story8_hitbox = load_image('story/story8.png',1,1,width,height,False)
    story9, story9_rect, story9_hitbox = load_image('story/story9.png',1,1,width,height,False)
    story10, story10_rect, story10_hitbox = load_image('story/story10.png',1,1,width,height,False)
    story_end_number = 0
    
    end_stories = [story7, story8, story9, story10]
    end_story_rects = [story7_rect, story8_rect, story9_rect, story10_rect]
    end_counter = 0
    
    warning, warning_rect, warning_hitbox = load_image('warning.png', .5, .5, width/2 - 400, 250, False)
    sink_counter = 0
    tree_speed = -6
    
    yellow_hitbox1 = pygame.Rect(0, 0, width, 120)
    yellow_hitbox2 = pygame.Rect(0, height-130, width, 130)
    
    lose_screen1, lose_screen1_rect, lose_screen1_hitbox = load_image('losescreen1.png', 1, 1 ,0, height, False)
    lose_screen2, lose_screen2_rect, lose_screen2_hitbox = load_image('losescreen2.png', 1, 1 ,0, height, False)
    replay_rect = pygame.Rect(width/2 - 80, height/2 + 200, 650, 100)
    
    # Sound effects and music
    
    pygame.mixer.init()
    
    story_proceed_sound = pygame.mixer.Sound('UI_Sound/storysound.wav')
    story_proceed_sound.set_volume(1)
    egg_crack = pygame.mixer.Sound('UI_Sound/eggcrack.wav')
    egg_crack.set_volume(.2)
    beam_sound = pygame.mixer.Sound('UI_Sound/beamsound.wav')
    beam_sound.set_volume(.5)
    yellow_beam_sound = pygame.mixer.Sound('UI_Sound/yellowbeamsound.wav')
    yellow_beam_sound.set_volume(.5)
    red_beam_sound = pygame.mixer.Sound('UI_Sound/redbeam.wav')
    red_beam_sound.set_volume(.5)
    music = pygame.mixer.Sound('UI_Sound/music.wav')
    music.set_volume(.7)
    music_playing = False
    end_music = pygame.mixer.Sound('UI_Sound/theend.wav')
    end_played = False
    cheers = pygame.mixer.Sound("UI_Sound/cheers.wav")
    cheers_played = False
    
while running:
    while title:
        if not music_playing:
            music.play(loops = -1)
            music_playing = True
        cursor_pos = pygame.mouse.get_pos()
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                pygame.display.quit()
                pygame.quit()
                exit()
            if play_rect.collidepoint(cursor_pos):
                play_selected = True
            else:
                play_selected = False
            if play_selected and event.type == pygame.MOUSEBUTTONDOWN:
                title = False
                story = True
        screen.fill('white')
        if not play_selected:
            screen.blit(title_screen1, title_screen1_rect)
        else:
            screen.blit(title_screen2, title_screen2_rect)
            
        # pygame.draw.rect(screen, 'red', play_rect)    
        pygame.display.update()
        clock.tick(60)
        
    while story:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                pygame.display.quit()
                pygame.quit()
                exit()
        screen.fill('white')
        
        for story, rect in zip(stories, story_rects):
            screen.blit(story, rect)
            
        if keys[pygame.K_SPACE] and not story_pressed:
            if story_rects[story_number].x <= 0:
                if story_number < 5:
                    story_proceed_sound.play()
                    story_number += 1
                    story_moving = False
                else:
                    story = False
                    ingame = True
                    music.stop()
                    music.play(loops = -1)
                    
            else:
                story_moving = True
            story_pressed = True
        else:
            story_pressed = False
            
        if story_moving:
            if story_number < 6:
                if story_rects[story_number].x > 0:
                    story_rects[story_number].x -= 20
                    
        pygame.display.update()
        clock.tick(60)
        
    while ingame:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                pygame.display.quit()
                pygame.quit()
                exit()
                
        screen.fill('white')
        if player.hitbox.bottom >= temp_ground.top:
            sink_counter += 1
            if sink_counter > 20:
                if not player.dead:
                    screen.blit(warning, warning_rect)
            elif sink_counter >= 40:
                sink_counter = 0
        else:
            sink_counter = 0
        # pygame.draw.rect(screen, 'black', temp_ground)
        
        for tree, tree_rect in zip(trees, tree_rects):
            if tree_rect.right <= 0:
                tree_rect.left = width
            if alien.stage1:
                if alien.health == 30:
                    tree_speed = -9
                elif alien.health == 20:
                    tree_speed = -12
                elif alien.health == 10:
                    tree_speed = -15
            elif alien.stage2:
                if tree_speed > -30:
                    tree_speed -= 1
            elif alien.stage3:
                if alien.health <= 0:
                    ingame = False
                    postgame = True
                elif alien.health <= 10:
                    if tree_speed < -10:
                        tree_speed += 1
                elif alien.health <= 20:
                    if tree_speed < -20:
                        tree_speed += 1
                elif alien.health <= 30:
                    if tree_speed < -30:
                        tree_speed += 1
                elif alien.health <= 40:
                    if tree_speed < -40:
                        tree_speed += 1
                elif alien.health > 40:
                    if tree_speed > -50:
                        tree_speed -=1
            
            tree_rect.x += tree_speed
            screen.blit(tree, tree_rect)
        
        # pygame.draw.rect(screen, 'blue', player.hitbox)
        if leaf_blower_wind_rect.y >= height:
            leaf_blower_wind_rect.centery = player.hitbox.centery + 60
            leaf_blower_wind_rect.centerx = player.hitbox.left - 5
        else:
            leaf_blower_wind_rect.y += 10
            leaf_blower_wind_rect.centerx = player.hitbox.left - 5
        
        if not player.dead:    
            screen.blit(leaf_blower_wind, leaf_blower_wind_rect)
        
        screen.blit(player.image, player.rect)
        player.update()
        
        # pygame.draw.rect(screen, 'red', alien.hitbox1)
        # pygame.draw.rect(screen, 'orange', alien.hitbox2)
        # pygame.draw.rect(screen, 'yellow', alien.hitbox3)
        # pygame.draw.rect(screen, 'green', alien.hitbox4)
        alien.update()
        screen.blit(alien.image, alien.rect)
        
        if int(player.throwing_egg_index) == 0:
            egg_thrown = False
        elif int(player.throwing_egg_index) == 4 and not egg_thrown:
            egg_thrown = True
            eggs.append(Egg(width, height, player))
        
        if len(eggs) > 0:
            for egg in eggs:
                screen.blit(egg.image, egg.rect)
                # pygame.draw.rect(screen, 'green', egg.hitbox)
                egg.update()
                if egg.despawned == True or (egg.despawning and not (egg.hitbox.colliderect(alien.hitbox1) or egg.hitbox.colliderect(alien.hitbox2) or egg.hitbox.colliderect(alien.hitbox3) or egg.hitbox.colliderect(alien.hitbox4))):
                    eggs.remove(egg)
                if egg.hitbox.colliderect(alien.hitbox1) or egg.hitbox.colliderect(alien.hitbox2) or egg.hitbox.colliderect(alien.hitbox3) or egg.hitbox.colliderect(alien.hitbox4):
                    egg.speed = 0
                    egg.despawning = True
                    if not egg.dealt_damage:
                        egg_crack.play()
                        alien.health -= 1
                        egg.dealt_damage = True
                    egg.hitbox.y += alien.hover_speed
                    egg.rect.y += alien.hover_speed
        
        if alien.active_red_attack:
            red_beam_sound.play()
            pygame.draw.line(screen, 'red', (alien.rect.centerx, alien.rect.top + 40), (0, alien.rect.top + 40), 40)
            if player.hitbox.colliderect(pygame.draw.line(screen, 'red', (alien.rect.centerx, alien.rect.top + 40), (0, alien.rect.top + 40), 40)):
                player.dead = True
        elif alien.green_index > 0 and alien.green_index < 5:
            screen.blit(alien.prebeam, alien.beam_rect)
            beam_sound.play(0, 500)
        elif alien.green_index > 4:
            screen.blit(alien.beam, alien.beam_rect)
            beam_hitbox = pygame.Rect(alien.beam_rect.centerx - 160, 0, 320, height)
            beam_hitbox2 = pygame.Rect(alien.beam_rect.centerx - 200, 400, 400, height - 400)
            beam_hitbox3 = pygame.Rect(alien.beam_rect.centerx - 230, 600, 440, height - 600)
            if player.hitbox.colliderect(beam_hitbox) or player.hitbox.colliderect(beam_hitbox2) or player.hitbox.colliderect(beam_hitbox3):
                player.dead = True
            # pygame.draw.rect(screen, 'yellow', beam_hitbox)
            # pygame.draw.rect(screen, 'orange', beam_hitbox2)
            # pygame.draw.rect(screen, 'red', beam_hitbox3)
        elif alien.yellow_index > 0 and alien.yellow_index < 5:
            screen.blit(alien.yellow_prebeam, alien. yellow_beam_rect)
            yellow_beam_sound.play(0, 500)
        elif alien.yellow_index > 4:
            screen.blit(alien.yellow_beam, alien.yellow_beam_rect)
            if player.hitbox.colliderect(yellow_hitbox1) or player.hitbox.colliderect(yellow_hitbox2):
                player.dead = True
            # pygame.draw.rect(screen, 'purple', yellow_hitbox1)
            # pygame.draw.rect(screen, 'purple', yellow_hitbox2)

        if alien.stage2 or alien.stage3:
            screen.blit(alien.pellet, alien.pellet_rect)
            screen.blit(alien.pellet2, alien.pellet2_rect)
            screen.blit(alien.pellet3, alien.pellet3_rect)
            alien.pellet_rect.x += alien.pellet_speed
            alien.pellet_hitbox.x += alien.pellet_speed
            alien.pellet2_rect.x += alien.pellet2_speed
            alien.pellet2_hitbox.x += alien.pellet2_speed
            alien.pellet3_rect.x += alien.pellet3_speed
            alien.pellet3_hitbox.x += alien.pellet3_speed
            if player.hitbox.colliderect(alien.pellet_hitbox) or player.hitbox.colliderect(alien.pellet2_hitbox) or player.hitbox.colliderect(alien.pellet3_hitbox):
                player.dead = True
            
        # pygame.draw.rect(screen, 'orange', alien.pellet_hitbox)
        # pygame.draw.rect(screen, 'orange', alien.pellet2_hitbox)
        # pygame.draw.rect(screen, 'orange', alien.pellet3_hitbox)
        
        for hitbox in alien.hitboxes:
            if player.hitbox.colliderect(hitbox):
                player.dead = True
                
        if (player.dead and player.hitbox.bottom > height) or player.hitbox.bottom > height + 50:
            ingame = False
            lost = True
            music.stop()
            music_playing = False
        
        pygame.display.update()
        clock.tick(60)
        
    while postgame:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                pygame.display.quit()
                pygame.quit()
                exit()
        
        screen.fill('white')
        
        for tree, tree_rect in zip(trees, tree_rects):
            if tree_rect.right <= 0:
                tree_rect.left = width
            tree_rect.x += -3
            screen.blit(tree, tree_rect)    
            
        if leaf_blower_wind_rect.y >= height:
            leaf_blower_wind_rect.centery = player.hitbox.centery + 60
            leaf_blower_wind_rect.centerx = player.hitbox.left - 5
        else:
            leaf_blower_wind_rect.y += 10
            leaf_blower_wind_rect.centerx = player.hitbox.left - 5
            
        screen.blit(leaf_blower_wind, leaf_blower_wind_rect)
        
        screen.blit(player.celebrating, player.rect)
        player.update()
        
        screen.blit(alien.image, alien.rect)
        alien.rect.y += 3
        
        if alien.rect.top >= height:
            story_pressed = False
            story_moving = False
            postgame = False
            endstory = True
            music.stop()
            music_playing = False
        
        pygame.display.update()
        clock.tick(60)   
        
    while endstory:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                pygame.display.quit()
                pygame.quit()
                exit()
        screen.fill('white')
        end_counter += 1
        
        alien.fire_loop.stop()
        for story, rect in zip(end_stories, end_story_rects):
            screen.blit(story, rect)
            
        if story_end_number == 0 and not cheers_played:
                cheers.play()
                cheers_played = True
            
        if end_counter > 50 and not story_pressed and keys[pygame.K_SPACE] and end_story_rects[story_end_number].left <= 0:
            story_moving = False
            if story_end_number == len(end_stories) - 2 and music_playing == False:
                end_music.play()
                end_played = True
            if story_end_number < len(end_stories)-1:
                story_proceed_sound.play()
                story_end_number += 1
                story_moving = True
                story_pressed = True
            else:
                endstory = False
                title = True
                player_group = pygame.sprite.GroupSingle()
                player = Player(width, temp_ground)
                alien = Alien(screen, width, height, player)
                player_group.add(player)
                alien_group.add(alien)
                story_number = 0
                story_end_number = 0
                story1, story1_rect, story1_hitbox = load_image('story/story1.png',1,1,0,height,False)
                story2, story2_rect, story2_hitbox = load_image('story/story2.png',1,1,width,height,False)
                story3, story3_rect, story3_hitbox = load_image('story/story3.png',1,1,width,height,False)
                story4, story4_rect, story4_hitbox = load_image('story/story4.png',1,1,width,height,False)
                story5, story5_rect, story5_hitbox = load_image('story/story5.png',1,1,width,height,False)
                story6, story6_rect, story6_hitbox = load_image('story/story6.png',1,1,width,height,False)
                story7, story7_rect, story7_hitbox = load_image('story/story7.png',1,1,0,height,False)
                story8, story8_rect, story8_hitbox = load_image('story/story8.png',1,1,width,height,False)
                story9, story9_rect, story9_hitbox = load_image('story/story9.png',1,1,width,height,False)
                story10, story10_rect, story10_hitbox = load_image('story/story10.png',1,1,width,height,False)
                story_number = 0
                story_pressed = False
                story_moving = False
                stories = [story1, story2, story3, story4, story5, story6]
                story_rects = [story1_rect, story2_rect, story3_rect, story4_rect, story5_rect, story6_rect]
                end_stories = [story7, story8, story9, story10]
                end_story_rects = [story7_rect, story8_rect, story9_rect, story10_rect]
                end_counter = 0
        
        if not keys[pygame.K_SPACE]:
            story_pressed = False
            
        if story_moving:
            if story_end_number < 4:
                if end_story_rects[story_end_number].left > 0:
                    end_story_rects[story_end_number].left -= 20
                    
        pygame.display.update()
        clock.tick(60)  
        
    while lost:
        keys = pygame.key.get_pressed()
        cursor_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                pygame.display.quit()
                pygame.quit()
                exit()
            if replay_rect.collidepoint(cursor_pos):
                play_selected = True
            else:
                play_selected = False
            if play_selected and event.type == pygame.MOUSEBUTTONDOWN:
                lost = False
                ingame = True
                if not music_playing:
                    music.play(loops = -1)
                    music_playing = True
                player = Player(width, temp_ground)
                player_group.add(player)
                alien = Alien(screen, width, height,player)
                alien_group.add(alien)
                alien.stage1 = True
                alien.stage2 = False
                alien.stage3 = False
                alien.glass_breaking = False
                alien.health = 50
                tree_speed = -6
        
        if alien.stage3:
            alien.fire_loop.stop()
        screen.fill('white')
        if not play_selected:
            screen.blit(lose_screen1, lose_screen1_rect)
        else:
            screen.blit(lose_screen2, lose_screen2_rect)
        # pygame.draw.rect(screen, 'purple', replay_rect)
        
        pygame.display.update()
        clock.tick(60)

pygame.display.quit()
pygame.quit()
exit()   
    
            
    
