import pygame, sys

pygame.init()

Clock = pygame.time.Clock()

screen = pygame.display.set_mode((700,700))

class MAIN:
    def __init__(self):
        self.x_coord = 20
        self.y_coord = 525
        self.gravity = 1
        self.velocity = 20
        self.jumping = False
        self.current_sprite = 0 
        self.idle = True
        self.run = False
        self.jumpanim = False
        self.attack = False
        self.back1 = 0
        self.back2 = 700
        self.attack2 = False
        self.health = 5
        self.hurt = False
        self.alive = True

        self.idle_sprites = []
        self.idle_sprites.append(pygame.image.load('img/idle/Warrior_Idle_1.png'))
        self.idle_sprites.append(pygame.image.load('img/idle/Warrior_Idle_2.png'))
        self.idle_sprites.append(pygame.image.load('img/idle/Warrior_Idle_3.png'))
        self.idle_sprites.append(pygame.image.load('img/idle/Warrior_Idle_4.png'))
        self.idle_sprites.append(pygame.image.load('img/idle/Warrior_Idle_5.png'))
        self.idle_sprites.append(pygame.image.load('img/idle/Warrior_Idle_6.png'))

        self.background1 = pygame.image.load('img/Background.png')
        self.background1 = pygame.transform.scale(self.background1, (700,950))

        self.background2 = pygame.image.load('img/Background.png')
        self.background2 = pygame.transform.scale(self.background2, (700,950))

        self.run_sprites = []
        self.run_sprites.append(pygame.image.load('img/Run/Warrior_Run_1.png'))
        self.run_sprites.append(pygame.image.load('img/Run/Warrior_Run_2.png'))
        self.run_sprites.append(pygame.image.load('img/Run/Warrior_Run_3.png'))
        self.run_sprites.append(pygame.image.load('img/Run/Warrior_Run_4.png'))
        self.run_sprites.append(pygame.image.load('img/Run/Warrior_Run_5.png'))
        self.run_sprites.append(pygame.image.load('img/Run/Warrior_Run_6.png'))
        self.run_sprites.append(pygame.image.load('img/Run/Warrior_Run_7.png'))
        self.run_sprites.append(pygame.image.load('img/Run/Warrior_Run_8.png'))

        self.jump_sprites = []
        self.jump_sprites.append(pygame.image.load('img/Jump/Warrior_Jump_1.png'))
        self.jump_sprites.append(pygame.image.load('img/Jump/Warrior_Jump_2.png'))
        self.jump_sprites.append(pygame.image.load('img/Jump/Warrior_Jump_3.png'))

        self.hurt_sprites = []
        self.hurt_sprites.append(pygame.image.load('img/Hurt-Effect/Warrior_hurt_1.png'))
        self.hurt_sprites.append(pygame.image.load('img/Hurt-Effect/Warrior_hurt_2.png'))
        self.hurt_sprites.append(pygame.image.load('img/Hurt-Effect/Warrior_hurt_3.png'))
        self.hurt_sprites.append(pygame.image.load('img/Hurt-Effect/Warrior_hurt_4.png'))

        self.death_sprites = []
        self.death_sprites.append(pygame.image.load('img/Death/Warrior_Death_1.png'))
        self.death_sprites.append(pygame.image.load('img/Death/Warrior_Death_2.png'))
        self.death_sprites.append(pygame.image.load('img/Death/Warrior_Death_3.png'))
        self.death_sprites.append(pygame.image.load('img/Death/Warrior_Death_4.png'))
        self.death_sprites.append(pygame.image.load('img/Death/Warrior_Death_5.png'))
        self.death_sprites.append(pygame.image.load('img/Death/Warrior_Death_6.png'))
        self.death_sprites.append(pygame.image.load('img/Death/Warrior_Death_7.png'))
        self.death_sprites.append(pygame.image.load('img/Death/Warrior_Death_8.png'))
        self.death_sprites.append(pygame.image.load('img/Death/Warrior_Death_9.png'))
        self.death_sprites.append(pygame.image.load('img/Death/Warrior_Death_10.png'))
        self.death_sprites.append(pygame.image.load('img/Death/Warrior_Death_11.png'))

        self.attack_sprites = []
        self.attack_sprites.append(pygame.image.load('img/Attack/Warrior_Attack_1.png'))
        self.attack_sprites.append(pygame.image.load('img/Attack/Warrior_Attack_2.png'))
        self.attack_sprites.append(pygame.image.load('img/Attack/Warrior_Attack_3.png'))
        self.attack_sprites.append(pygame.image.load('img/Attack/Warrior_Attack_4.png'))
        self.attack_sprites.append(pygame.image.load('img/Attack/Warrior_Attack_5.png'))
        self.attack_sprites.append(pygame.image.load('img/Attack/Warrior_Attack_6.png'))
        self.attack_sprites.append(pygame.image.load('img/Attack/Warrior_Attack_7.png'))
        self.attack_sprites.append(pygame.image.load('img/Attack/Warrior_Attack_8.png'))
        self.attack_sprites.append(pygame.image.load('img/Attack/Warrior_Attack_9.png'))
        self.attack_sprites.append(pygame.image.load('img/Attack/Warrior_Attack_10.png'))
        self.attack_sprites.append(pygame.image.load('img/Attack/Warrior_Attack_11.png'))
        self.attack_sprites.append(pygame.image.load('img/Attack/Warrior_Attack_12.png'))

        self.attack2_sprites = []
        self.attack2_sprites.append(pygame.image.load('img/Attack2/Warrior_Dash-Attack_1.png'))
        self.attack2_sprites.append(pygame.image.load('img/Attack2/Warrior_Dash-Attack_2.png'))
        self.attack2_sprites.append(pygame.image.load('img/Attack2/Warrior_Dash-Attack_3.png'))
        self.attack2_sprites.append(pygame.image.load('img/Attack2/Warrior_Dash-Attack_4.png'))
        self.attack2_sprites.append(pygame.image.load('img/Attack2/Warrior_Dash-Attack_5.png'))
        self.attack2_sprites.append(pygame.image.load('img/Attack2/Warrior_Dash-Attack_6.png'))
        self.attack2_sprites.append(pygame.image.load('img/Attack2/Warrior_Dash-Attack_7.png'))
        self.attack2_sprites.append(pygame.image.load('img/Attack2/Warrior_Dash-Attack_8.png'))
        self.attack2_sprites.append(pygame.image.load('img/Attack2/Warrior_Dash-Attack_9.png'))
        self.attack2_sprites.append(pygame.image.load('img/Attack2/Warrior_Dash-Attack_10.png'))


    def background(self):

        if self.back1 == -700:
            self.back1 = 0

        if self.back2 == 0:
            self.back2 = 700

 
    def idle_anim(self):

        if self.idle == True and self.alive == True:
            if self.current_sprite >= len(self.idle_sprites):
                self.current_sprite = 0

            self.image = self.idle_sprites[int(self.current_sprite)]
            self.current_sprite += 0.15
            self.image = pygame.transform.scale(self.image, (150,150))

    def run_anim(self):
        if self.run == True:
            main.attack2 = False


            if self.current_sprite >= len(self.run_sprites):
                self.current_sprite = 0

            self.image = self.run_sprites[int(self.current_sprite)]
            self.current_sprite += 0.7
            self.image = pygame.transform.scale(self.image, (150,150))

    def jump_anim(self):
        if self.jumpanim == True:
            if self.current_sprite >= len(self.jump_sprites):
                self.current_sprite = 0

            self.image = self.jump_sprites[int(self.current_sprite)]
            self.current_sprite += 0.5
            self.image = pygame.transform.scale(self.image, (150,150))

    def hurt_anim(self):

        if self.hurt == True:
            if self.current_sprite >= len(self.hurt_sprites):
                self.current_sprite = 0
                self.hurt = False

            self.image = self.hurt_sprites[int(self.current_sprite)]
            self.current_sprite += 0.1
            self.image = pygame.transform.scale(self.image, (150,150))

    def death_anim(self):

        if self.alive == False:

            if self.current_sprite >= len(self.death_sprites):
                self.alive = True
                self.current_sprite = 0
                self.x_coord = 20
                self.idle = True
                main.health = 5


            self.image = self.death_sprites[int(self.current_sprite)]
            self.current_sprite += 0.4
            self.image = pygame.transform.scale(self.image, (150,150))



    def attk_anim(self):

        if self.attack == True:
            self.image = self.attack_sprites[int(self.current_sprite)]
            self.current_sprite += 0.5
            self.image = pygame.transform.scale(self.image, (150,150))
            
            if self.current_sprite >= len(self.attack_sprites):
                self.current_sprite = 0
                self.attack = False
                self.idle = True

    def attk_anim2(self):

        if self.attack2 == True:
            if self.current_sprite >= len(self.attack2_sprites):
                self.current_sprite = 0
                self.attack2 = False
                self.idle = True

            if int(self.current_sprite) == 4:
                ui.color -= 30

            self.image = self.attack2_sprites[int(self.current_sprite)]
            self.current_sprite += 0.5
            self.image = pygame.transform.scale(self.image, (150,150))

    def playerloop(self):
        screen.blit(self.image, (self.x_coord,self.y_coord))

    def jump(self):

        if self.jumping == True:
            self.y_coord -= self.velocity
            self.velocity -= self.gravity
            

        if self.y_coord == 525:
            self.gravity = 1
            self.velocity = 15
            self.jumping = False

class ENEMY:
    def __init__(self):
        self.eney = 595
        self.enex = 690
        self.enemy_current = 0
        self.alive = True

        self.slime_sprites = []
        self.slime_sprites.append(pygame.image.load('img/Slimer/slimer1.png'))
        self.slime_sprites.append(pygame.image.load('img/Slimer/slimer1.png'))
        self.slime_sprites.append(pygame.image.load('img/Slimer/slimer1.png'))
        self.slime_sprites.append(pygame.image.load('img/Slimer/slimer2.png'))
        self.slime_sprites.append(pygame.image.load('img/Slimer/slimer3.png'))
        self.slime_sprites.append(pygame.image.load('img/Slimer/slimer4.png'))
        self.slime_sprites.append(pygame.image.load('img/Slimer/slimer5.png'))
        self.slime_sprites.append(pygame.image.load('img/Slimer/slimer6.png'))
        self.slime_sprites.append(pygame.image.load('img/Slimer/slimer7.png'))
        self.slime_sprites.append(pygame.image.load('img/Slimer/slimer1.png'))

        self.slime_death = []
        self.slime_death.append(pygame.image.load('img/Slimer/slimer4.png'))
        self.slime_death.append(pygame.image.load('img/Slimer/slimer3.png'))
        self.slime_death.append(pygame.image.load('img/Slimer/slimer5.png'))
        self.slime_death.append(pygame.image.load('img/Slimer/slimer6.png'))
        self.slime_death.append(pygame.image.load('img/Slimer/slimer6.png'))
        self.slime_death.append(pygame.image.load('img/Slimer/slimer6.png'))


    def spawn(self):
        
        if self.alive == True:
            self.enemy_image = self.slime_sprites[int(self.enemy_current)]
            self.enemy_current += 0.33
            self.enemy_image = pygame.transform.scale(self.enemy_image, (80,80))

            if int(self.enemy_current) == 5:
                self.enex -= 5

            if self.enemy_current >= len(self.slime_sprites):
                self.enemy_current = 0

            if self.enex <= -45:
                self.enex = 690

    def death(self):
       
        if self.alive == False:
            self.enemy_image = self.slime_death[int(self.enemy_current)]
            self.enemy_current += 0.33
            self.enemy_image = pygame.transform.scale(self.enemy_image, (80,80))

            if self.enemy_current >= len(self.slime_death):
                self.enemy_current = 0
                self.alive = True
                self.enex = 690

    def enemyspawn(self):
        screen.blit(self.enemy_image, (self.enex,self.eney))

class UI:
    def __init__(self):
        self.heart = pygame.image.load('img/heart.png')
        self.heartgone = pygame.image.load('img/heart2.png')

        self.heart = pygame.transform.scale(self.heart, (50,50))
        self.heartgone = pygame.transform.scale(self.heartgone, (50,50))

        self.heart1 = self.heart
        self.heart2 = self.heart
        self.heart3 = self.heart
        self.heart4 = self.heart
        self.heart5 = self.heart


        self.counter = 0
        self.color = 185

        self.bar = pygame.image.load('img/bg.png')

        self.bar = pygame.transform.scale(self.bar, (250,50))


    def healthbar(self):

        screen.blit(self.heart1, (10,5))
        screen.blit(self.heart2, (50,5))
        screen.blit(self.heart3, (90,5))
        screen.blit(self.heart4, (130,5))
        screen.blit(self.heart5, (170,5))

        if main.health == 4:
            self.heart5 = self.heartgone
        elif main.health == 3:
            self.heart4 = self.heartgone
        elif main.health == 2:
            self.heart3 = self.heartgone
        elif main.health == 1:
            self.heart2 = self.heartgone
        elif main.health == 0:
            self.heart1 = self.heartgone
        elif main.health == 5:
            self.heart1 = self.heart
            self.heart2 = self.heart
            self.heart3 = self.heart
            self.heart4 = self.heart
            self.heart5 = self.heart

    def stam(self):
        screen.blit(self.bar, (478,5))
        pygame.draw.rect(screen, (0,0,250), (511,19,self.color,23))
        

main = MAIN()
enemy = ENEMY()
ui = UI()

while True:

    screen.fill((255,255,255))
    main.background()
    screen.blit(main.background1, (main.back1,-200))
    screen.blit(main.background2, (main.back2,-200))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:

            if main.x_coord < 400:
                main.x_coord += 10

            if main.x_coord >= 400:
                main.back1 -= 10
                main.back2 -= 10
                enemy.enex -= 10

            main.idle = False
            main.jumpanim = False
            main.run = True

        if event.key == pygame.K_LEFT:
            if main.x_coord > -10:
                main.x_coord -= 10
            main.idle = False
            main.jumpanim = False
            main.run = True

        if event.key == pygame.K_UP:
            main.jumping = True
            main.idle = False
            main.jumpanim = True
            main.run = False
            main.attack = False
            
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
            main.idle = True
            main.run = False
        if event.key == pygame.K_LEFT:
            main.idle = True
            main.run = False
        if event.key == pygame.K_UP:
            main.idle = True
            main.jumpanim = False
    if event.type == pygame.TEXTINPUT:
        if event.text == "z":
            main.jumpanim = False
            main.run = False
            main.idle = False
            main.attack = True
            main.attack2 = False


        if event.text == "x" and 30 < ui.color:
            main.current_sprite = 0
            main.jumpanim = False
            main.run = False
            main.idle = False
            main.attack = False
            main.attack2 = True

            if main.x_coord <= enemy.enex <= main.x_coord + 110 and enemy.eney == main.y_coord + 70:     
                enemy.enemy_current = 0
                enemy.alive = False




    if enemy.enex == main.x_coord + 70 and enemy.eney == main.y_coord + 70:
        main.hurt = True
        main.health -= 1
        main.x_coord -= 15

    if enemy.enex == main.x_coord and enemy.eney == main.y_coord + 70:
        main.hurt = True
        main.health -= 1
        main.x_coord += 30

    if main.health <= 0 and  main.alive == True:
        main.idle = False
        main.alive = False

    if ui.color < 185:
        ui.counter += .5

        if ui.counter % 10 == 0:
            ui.color += 20

    if ui.color < 0:
        ui.color = 0
    elif ui.color > 185:
        ui.color = 185

    enemy.spawn()
    main.idle_anim()
    main.jump()
    main.attk_anim()
    main.attk_anim2()
    main.hurt_anim()
    main.death_anim()
    ui.healthbar()
    ui.stam()

    Clock.tick(25)

    enemy.death()
    enemy.enemyspawn()
    main.jump_anim()
    main.run_anim()
    main.playerloop()
    pygame.display.update()