from pygame import *

window = display.set_mode((700, 500))
display.set_caption('ping-pong')  

background = transform.scale(
    image.load('es.jpg'),
    (700, 500)
) 

class GameSprite(sprite.Sprite):
    def __init__(self, img, speed, x, y, img_width, img_height, pon):
        self.img = transform.scale(image.load(img), (img_width, img_height))
        self.speed = speed
        self.pon = pon
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.img, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, img, speed, x, y, img_width, img_height, pon):
            super().__init__(img, speed, x, y, img_width, img_height, pon)


    def control(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0 :
            self.rect.y -= self.speed    
        if keys_pressed[K_s] and self.rect.y < 405:
            self.rect.y += self.speed

    def control2(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0 :
            self.rect.y -= self.speed    
        if keys_pressed[K_DOWN] and self.rect.y < 405:
            self.rect.y += self.speed


class Ball(GameSprite):
    def __init__(self, img, speed, x, y, speed_x, speed_y, img_width, img_height, pon):
        super().__init__(img, speed, x, y, img_width, img_height, pon)
        self.speed_x = speed_x
        self.speed_y = speed_y

    def kuda(self):
        
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if sprite.collide_rect(ball, player2):
            self.speed_x *= -1
            self.speed_y *= -1

        if self.rect.y <= 0:
            

ball = 'ball.png'

clock = time.Clock()
FPS = 60
game = True

player = Player('palka.png', 30, 50, 400, 20, 100, 0)
player2 = Player('palka.png', 30, 600, 400, 20, 100, 0)
ball = Ball(ball, 70, 400, 300, 3, 3, 50, 50, 0)
while game:
    window.blit(background,(0, 0))
    player.reset()
    player.control()
    player2.reset()
    player2.control2()
    ball.reset()
    ball.kuda()
    for e in event.get():
        if e.type == QUIT:
            game = False

    

    clock.tick(FPS)

    display.update()
