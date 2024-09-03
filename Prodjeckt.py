import pygame

bullet11="bullet/1.png"
bullet2=["bullet/1.png","bullet/2.png","bullet/3.png","bullet/4.png"]
clock = pygame.time.Clock()
pygame.init()

imen="enemy/a1.png"
mony="Mony/coin_01.png"
ALLMany=["Mony/coin_01.png","Mony/coin_02.png","Mony/coin_03.png","Mony/coin_04.png","Mony/coin_05.png","Mony/coin_05.png","Mony/coin_06.png","Mony/coin_07.png","Mony/coin_08.png"]
LEFT = -8
RIGHT = 8
UP = 8
Finish=0
Playand= 0
DOWN = -8
ANIMATION_DELAY = 10
width = 1380
height = 630
BLACK = (0, 0, 0)
window = pygame.display.set_mode((width, height))
background = pygame.transform.scale(pygame.image.load("fon.png"), (width, height))
xbk1=0
move_80 = 0
keystate = pygame.key.get_pressed()
move_8 = 0
move_7 = 0
enemydd=["enemy/a1.png","enemy/a2.png","enemy/a3.png"]
moving = [1, 400]  # x i y player
size = [196, 140]
move_drawe = ["move/k1.png", "move/k2.png", "move/k3.png", "move/k4.png", "move/k5.png", "move/k6.png", "move/k7.png", "move/k8.png"]
left_move = ["Left_move/L1.png", "Left_move/L2.png", "Left_move/L3.png", "Left_move/L4.png", "Left_move/L5.png", "Left_move/L6.png", "Left_move/L7.png", "Left_move/L8.png"]
idle = "idle/i1.png"
bloks = ["Bloks/bk1.png", "Bloks/bk2.png", "Bloks/bk3.png"]

end_font = pygame.font.Font(None, 36)  
end_text = end_font.render("Игра окончена – Спасибо за игру!", True, (255, 255, 255))
end_rect = end_text.get_rect(center=(width // 2, height // 2))

play_again_font = pygame.font.Font(None, 24)  
play_again_text = play_again_font.render("Play Again", True, (255, 255, 255))
play_again_rect = play_again_text.get_rect(center=(width // 2, height // 2 + 50))
class GameSprite(pygame.sprite.Sprite):
    def __init__(self, img_path, x, y, width, height):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(img_path), (width,height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speedx = 0
        self.move_8 = move_8
        self.ui = 0
        self.move_7 = move_7
        self.xbk = 300
        self.ohoh = 1
        
        
    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))



class Player(GameSprite):
    def __init__(self, img_path, x, y, width, height, move_8, move_7, RIGHT, UP, DOWN,rotate):
        super().__init__(img_path, x, y, width, height)
        self.xccc = self.rect.x
        self.yccc =self.rect.y
        self.rotate= 0
        self.move_8 = move_8
        self.ui = 0
        self.move_7 = move_7
        self.RIGHT = RIGHT
        self.UP = UP
        self.DOWN = DOWN
        self.gravity = 0.4
        self.vertical_speed = 0
        self.blok_img = "Bloks/bk2.png"
       
    
    
        

    def update(self, all_platforms):
        xccc = self.rect.x
        self.rect.y += self.vertical_speed
        self.vertical_speed += self.gravity
        if self.speedx <0:
            self.rotate = 1

        block_hit_list = pygame.sprite.spritecollide(self, all_platforms, False)
        for block in block_hit_list:
            if self.vertical_speed > 0:
                if self.rect.top != block.rect.bottom:
                    self.rect.bottom = block.rect.top
                    self.vertical_speed = 0

        enemy_hit_list = pygame.sprite.spritecollide(self, all_enemy, False)
        yyy = len(enemy_hit_list)
        
        if yyy > 0 :
            player.rect.x = moving[0]
            player.rect.y = moving[1]
        
   
        Money12_hit_list = pygame.sprite.spritecollide(self, End_1, False)
        yym = len(Money12_hit_list)
        
        if yym > 0 :
            Finish=True
            
            
            
       
            
                

        





        self.speedx = 0
        self.rect.x = max(0, min(self.rect.x, width - self.rect.width))
        keystate = pygame.key.get_pressed()

        if keystate[pygame.K_LEFT]:
            self.speedx = LEFT
        elif keystate[pygame.K_RIGHT]:
            self.speedx = RIGHT

        if self.speedx ==-8:
            self.rotate = 2
        elif self.speedx == 8:
            self.rotate = 1


        self.rect.x += self.speedx
        if self.speedx == 0:
            self.image = pygame.transform.scale(pygame.image.load(idle), (196, 140))

        elif self.speedx > 0:


            if self.ui == 5:
                self.move_8 += 1
                if self.move_8 > 7:
                    self.move_8 = 0
                self.image = pygame.transform.scale(pygame.image.load(move_drawe[self.move_8]), (196, 140))
                self.ui = 0
            self.ui += 1
        else:

            if self.ui == 5:
                self.move_7 += 1
                if self.move_7 > 7:
                    self.move_7 = 0
                self.image = pygame.transform.scale(pygame.image.load(left_move[self.move_7]), (87, 122))
                
                self.ui = 0
            self.ui += 1
    
    


    def ENDD(self):
        Money12_hit_list = pygame.sprite.spritecollide(self, End_1, False)
        yym = len(Money12_hit_list)
        
        if yym > 0 :
            Finish=True
            return Finish  
    def jump(self):
        self.speedy = -20

    def get_rotate_value(self):
        return self.rotate

    def get_rect_x(self):
        return self.rect.x


    def up_update(self):
        self.rect.y = max(0, min(self.rect.y, width - self.rect.height))

        keystate = pygame.key.get_pressed()

        if keystate[pygame.K_UP]:
            self.speedy = LEFT
        elif keystate[pygame.K_DOWN]:
            self.speedy = LEFT * -1
        else:
            self.speedy = 0
        self.rect.y += self.speedy


class Platform(pygame.sprite.Sprite):
    def __init__(self, img_path, x, y, width, height):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(img_path), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.ohoh = 1

    def drawbloks(self):
        # нижние платформи
        #window.blit(self.image, (self.rect.x, self.rect.y))
        window.blit(self.image, (70, self.rect.y))
        window.blit(self.image, (140, self.rect.y))

        #window.blit(self.image, (210, self.rect.y))
        #window.blit(self.image, (280, self.rect.y))
        #window.blit(self.image, (350, self.rect.y))
        window.blit(self.image, (420, self.rect.y))
        window.blit(self.image, (490, self.rect.y))
        window.blit(self.image, (560, self.rect.y))

       # Верхние плат
        window.blit(self.image, (1310,500 ))
        window.blit(self.image, (1240,500 ))
        window.blit(self.image, (1170, 500))
        window.blit(self.image, (1100, 500))
        window.blit(self.image, (1030, 500))
        window.blit(self.image, (1310, 220))
        window.blit(self.image, (1240, 220))

        window.blit(self.image, (890, 220))
        window.blit(self.image, (820, 220))
        window.blit(self.image, (750, 220))

        window.blit(self.image, (400, 220))
        window.blit(self.image, (330, 220))
        window.blit(self.image, (260, 220))

        window.blit(self.image, (190, 122))
        window.blit(self.image, (120, 122))
        window.blit(self.image, (50, 122))
        window.blit(self.image, (-20, 122))














        self.rect.x = 0
class Enemy(pygame.sprite.Sprite):
    def __init__(self, img_path, x, y, width, height,spedy,spedx,move_7):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(img_path), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.spedy=spedy
        self.spedx=spedx
        self.move_7 = 0
        self.move_8=0
        self.ui = 0
    def update(self):
        while self.ui == 6:
            self.move_8 += 1
            if self.move_8 > 2:
                self.move_8 = 0
            self.image = pygame.transform.scale(pygame.image.load(enemydd[self.move_8]), (98, 70))
            self.ui = 0
        self.ui += 1
        self.rect.y += self.spedy
        window.blit(self.image, (self.rect.x, self.rect.y))

        if self.rect.y == 400:
            self.spedy = -(self.spedy)
        elif self.rect.y ==50:
            self.spedy = -(self.spedy)
    def updateM(self):
        while self.ui == 7:
            self.move_8 += 1
            if self.move_8 > 2:
                self.move_8 = 0
            self.image = pygame.transform.scale(pygame.image.load(ALLMany[self.move_8]), (48, 45))
            self.ui = 0
        self.ui += 1
        self.rect.y += self.spedy
        window.blit(self.image, (self.rect.x, self.rect.y))

        if self.rect.y == 70:
            self.spedy = -(self.spedy)
        elif self.rect.y ==20:
            self.spedy = -(self.spedy)

player = Player(idle, moving[0], moving[1], size[0], size[1], move_8, move_7, RIGHT, UP, DOWN,0)


class Bullet(GameSprite):
    def __init__(self, img_path, x, y, width, height,spedy):
        super().__init__(img_path, x, y, width, height)
        self.spedy =spedy
        self.image = pygame.transform.scale(pygame.image.load(img_path), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rotate_value = player.get_rotate_value()
        self.rect.x = player.get_rotate_value()
        self.move_7 = 0
        self.move_8 = 0
        self.ui = 0
        self.x_rect_value = player.get_rect_x()

    def drawe(self):
        
     
        window.blit(self.image, (self.x_rect_value, self.rect.y))
       
        

        
       
    def update(self):
       self.rect.x += 1
       self.rect.x -= 1
       self.x_rect_value = player.get_rect_x()

       print()
            
       enemy_hit_list = pygame.sprite.spritecollide(self, all_enemy, True)
       
       
       yyy = len(enemy_hit_list)
       if yyy > 0 :
            print("fwefef")
       if self.ui == 6:
            self.kill
                 
       self.ui += 1

    def update180(self):



        self.rect.x += self.spedy
        if self.rect.x < 1380 and self.rect.x > 10 :

            window.blit(self.image, (self.rect.x, self.rect.y))
            while self.ui == 6:
                self.move_8 += 1
                if self.move_8 > 3:
                    self.move_8 = 0


                self.image = pygame.transform.rotate(pygame.image.load(bullet2[self.move_8]),180)
                self.ui = 0
            self.ui += 1
        else :
            self.kill()
class Blade(GameSprite):
    def __init__(self, img_path, x, y, width, height, spedy):
        super().__init__(img_path, x, y, width, height)
        self.spedy = spedy
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.start_time = pygame.time.get_ticks()  

    def update(self):
        self.rect.x += self.spedy

      
        enemy_hit_list = pygame.sprite.spritecollide(self, all_enemy, True)
        for enemy in enemy_hit_list:
            enemy.kill()

        # Blade exists for 3 seconds
        if pygame.time.get_ticks() - self.start_time > 3000:
            self.kill()  


knite = Bullet(bullet11,116,50,50,50,0)
Moneyy = Enemy(mony,20, 40,45,48,1,1,move_7)
enemy1 =Enemy(imen,550, 220,98,70,2,2,move_7)
End_1 = pygame.sprite.Group()
End_1.add(Moneyy)
blook = Platform("Bloks/bk2.png", 70, 600, 70, 98)
blook1 = Platform("Bloks/bk2.png", 70, 600, 70, 98)
blook2 = Platform("Bloks/bk2.png", 140, 600, 70, 98)
blook3 = Platform("Bloks/bk2.png", 210, 600, 70, 98)
blook4 = Platform("Bloks/bk2.png", 280, 600, 70, 98)
blook5 = Platform("Bloks/bk2.png", 350, 600, 70, 98)
blook6 = Platform("Bloks/bk2.png", 420, 600, 70, 98)
blook7 = Platform("Bloks/bk2.png", 490, 600, 70, 98)
blook8 = Platform("Bloks/bk2.png", 350, 600, 70, 98)
blook9 = Platform("Bloks/bk2.png", 350, 600, 70, 98)

# верх плит
blook10 = Platform("Bloks/bk2.png", 1100, 500, 70, 98)
blook11 = Platform("Bloks/bk2.png", 1240,500 , 70, 98)
blook12 = Platform("Bloks/bk2.png", 1310,220, 70, 98)

blook13 = Platform("Bloks/bk2.png", 820,220, 70, 98)
blook14 = Platform("Bloks/bk2.png", 330, 220, 70, 98)
blook15 = Platform("Bloks/bk2.png", 100, 122, 70, 98)


all_platforms = pygame.sprite.Group()
all_platforms.add(blook1,blook7,blook10,blook11,blook12,blook13,blook14,blook15)
all_enemy =pygame.sprite.Group()
all_enemy.add(enemy1)

ENDGAME = 0


while True:
    x_rect_value = player.get_rect_x()
        
    
    
    
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    if ENDGAME != True :
        
        knite.update()
        
        
        rotate_value = player.get_rotate_value()
        
        
        if player.rect.y > height:
            player.rect.x = moving[0]
            player.rect.y = moving[1]
        player.update(all_platforms)
    
        window.blit(background, (0, 0))
        keystate55 = pygame.key.get_pressed()
        
        
        if keystate55[pygame.K_DOWN]:
        
            knite.drawe()
            knite.update()
        

        player.draw()


        blook.drawbloks()
        Moneyy.updateM()
        enemy1.update()
        rotate_value = player.get_rotate_value()
        

        player.up_update()
    else :
        
        window.fill(BLACK)
        window.blit(end_text, end_rect)
        window.blit(play_again_text, play_again_rect)
       
        mouse_pos = pygame.mouse.get_pos()
        mouse_clicked = pygame.mouse.get_pressed()
        if play_again_rect.collidepoint(mouse_pos):

            if mouse_clicked[0]: 
                
                player.rect.x = moving[0]
                player.rect.y = moving[1]
                ENDGAME = False
                
                
                
    ENDGAME = player.ENDD()
    pygame.display.update()
    clock.tick(40)
  