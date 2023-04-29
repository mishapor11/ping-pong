from pygame import *

window = display.set_mode((700, 500))
display.set_caption('Догонялки')  

background = transform.scale(
    image.load('galaxy.jpg'),
    (700, 500)
) 


mixer.init()

x1 = 10
y1 = 400

mixer.music.load('space.ogg')
mixer.music.play()

num_fire = 0
rel_time = False

rocket = 'rocket.png'

class GameSprite(sprite.Sprite):
    def __init__(self, img, speed, x, y):
        self.image = transform.scale(image.load(img), (100,100))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blid(self.iage, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, img, speed, x, y):
            super().__init__(img, speed, x, y)

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

    def control(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_RIGHT] and x < 600:
            self.x += self.speed    
        if keys_pressed[K_LEFT] and x > 0:
            self.y -= self.speed
        
#class Enemy(GameSprite):
#    def __init__(self, name, image, speed, x, y):
#        self.name = 
 
#class Bullet(GameSprite):
#    def __init__(self, image, speed, x, y):

clock = time.Clock()
FPS = 60
player = Player(rocket, 10, 10, 400)
game = True
while game:
    window.blit(background,(0, 0))
    player.reset()
    for e in event.get():
        if e.type == QUIT:
            game = False

    keys_pressed = key.get_pressed()



    clock.tick(FPS)

    display.update()