import pygame
import random
import os

class Player(pygame.sprite.Sprite):
    def __init__(self, w, h):
        super().__init__()
        img = pygame.image.load(os.path.join("assets", "images", "player.png")).convert_alpha()
        self.image = pygame.transform.scale(img, (60, 60))
        self.rect = self.image.get_rect(midbottom=(w // 2, h - 20))
        self.speed = 15
        self.screen_w = w

    def update(self):
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and self.rect.left > 0: self.rect.x -= self.speed
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and self.rect.right < self.screen_w: self.rect.x += self.speed

class Enemy(pygame.sprite.Sprite):
    def __init__(self, w, level):
        super().__init__()
        img = pygame.image.load(os.path.join("assets", "images", "enemy.png")).convert_alpha()
        self.image = pygame.transform.scale(img, (60, 60))
        self.rect = self.image.get_rect(x=random.randint(0, w-60), y=random.randint(-100, -40))
        self.speed = random.randint(3, 6) + (level // 2)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > 800: self.kill()

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        img = pygame.image.load(os.path.join("assets", "images", "corazon.png")).convert_alpha()
        self.image = pygame.transform.scale(img, (35, 35))
        self.rect = self.image.get_rect(centerx=x, bottom=y)
        self.speed = 12

    def update(self):
        self.rect.y -= self.speed
        if self.rect.bottom < 0: self.kill()