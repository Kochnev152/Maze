#gerar,gerar,gerar:создай игру "Лабиринт"!
from pygame import *
clock = time.Clock()
FPS = 30

class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))
    def collidepoint(self):
        return self.rect.collidepoint()      
    def colliderect(self, rect):
        return self.rect.colliderect(rect)

class Wall(sprite.Sprite):
    def __init__(self, color_1,color_2,color_3,wall_x,wall_y,wall_width,wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1,color_2,color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    

    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Enemy(GameSprite):
    def __init__(self,player_image,player_x,player_y,player_speed,direction = "left"):
        self.direction = direction
        self.image = transform.scale(image.load(player_image),(65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def update(self):
        if self.rect.x <= 500:
            self.direction = "right"
        if self.rect.x >= 700 - 65:
            self.direction = "left"
        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Player(GameSprite):
    def __init__(self,player_image,player_x,player_y,player_speed):
        self.image = transform.scale(image.load(player_image),(65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y >= 10:
            self.rect.y -= 10
        if keys_pressed[K_DOWN] and self.rect.y <= 420:
            self.rect.y += 10
        if keys_pressed[K_LEFT] and self.rect.x >= 10:
            self.rect.x -= 10
        if keys_pressed[K_RIGHT] and self.rect.x <= 620:
            self.rect.x += 10

window = display.set_mode((700,500))
name = display.set_caption('Maze')
background = transform.scale(image.load('background.jpg'),(700,500))
wall_1 = Wall(119,119,0,80,30,600,15)
wall_2 = Wall(119,119,0,80,30,15,380)
wall_3 = Wall(119,119,0,190,480,305,15)
wall_4 = Wall(119,119,0,480,180,15,300)
wall_5 = Wall(119,119,0,190,130,15,350)
wall_6 = Wall(119,119,0,200,130,100,15)
wall_7 = Wall(119,119,0,380,40,15,350)
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()
kick = mixer.Sound('kick.ogg')
moneymoney = mixer.Sound('money.ogg')

x1 = 520
y1 = 70
sprite1 = Player('hero.png',10,70,4)
sprite2 = Enemy('cyborg.png',600,280,4,"left")
money = GameSprite('treasure.png',600,400,0)

font.init()
font = font.Font(None, 70)
win = font.render('YOU WIN!', True, (255,215,0))
lose = font.render('YOU LOSE!', True, (180,0,0))

game = True
finish = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True: 
        window.blit(background,(0,0))
        sprite1.reset()
        sprite1.update()
        sprite2.update()
        sprite2.reset()
        money.update()
        money.reset()

        wall_1.draw_wall()
        wall_2.draw_wall()
        wall_3.draw_wall()
        wall_4.draw_wall()
        wall_5.draw_wall()
        wall_6.draw_wall()
        wall_7.draw_wall()


        if sprite1.colliderect(money.rect):
            finish = True
            window.blit(win,(200,200))
            moneymoney.play() 
        if sprite1.colliderect(sprite2.rect) or sprite1.colliderect(wall_1.rect) or sprite1.colliderect(wall_2.rect) or sprite1.colliderect(wall_3.rect) or sprite1.colliderect(wall_4.rect) or sprite1.colliderect(wall_5.rect) or sprite1.colliderect(wall_6.rect) or sprite1.colliderect(wall_7.rect):
            finish = True
            window.blit(lose,(200,200))
            kick.play()
    

    clock.tick(FPS)
    display.update()