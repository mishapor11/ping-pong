from pygame import *

window = display.set_mode((700, 500))
display.set_caption('ping-pong')  

background = transform.scale(
    image.load('es.jpg'),
    (700, 500)
) 

class GameSprite(sprite.Sprite):
    def __init__(self, img, speed, x, y):
        self.img = transform.scale(image.load(img), (100,100))
        self.speed = speed
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.img, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, img, speed, x, y):
            super().__init__(img, speed, x, y)


    def control(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0 :
            self.rect.y -= self.speed    
        if keys_pressed[K_s] and self.rect.y < 405:
            self.rect.y += self.speed

clock = time.Clock()
FPS = 60
game = True

player = Player('palka.png', 30, 10, 400)
while game:
    window.blit(background,(0, 0))
    player.reset()
    player.control()
    for e in event.get():
        if e.type == QUIT:
            game = False

    

    clock.tick(FPS)

    display.update()