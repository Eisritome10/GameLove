import pygame
import sys
import random
from src.model import GameModel
from src.view import GameView
from src.sprites import Player, Enemy, Bullet

class GameLoveController:
    def __init__(self):
        pygame.init()
        self.W, self.H = 1200, 790
        self.screen = pygame.display.set_mode((self.W, self.H))
        pygame.display.set_caption("GameLove v2.0 - MVC")
        
        self.model = GameModel()
        self.view = GameView(self.screen, self.W, self.H)
        self.clock = pygame.time.Clock()

    def start_game(self):
        self.all_sprites = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.player = Player(self.W, self.H)
        self.all_sprites.add(self.player)
        self.model.reset_state()
        self.model.state = "PLAYING"

    def run(self):
        while True:
            if self.model.state == "MENU":
                self.handle_menu()
            elif self.model.state == "PLAYING":
                self.handle_playing()
            pygame.display.flip()
            self.clock.tick(60)

    def handle_menu(self):
        name = self.model.difficulty_names[self.model.difficulty_mode]
        self.view.draw_menu(self.model.high_score_lvl, self.model.high_score_time, name, self.model.difficulty_mode)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN: self.start_game()
                if event.key == pygame.K_d: self.model.cycle_difficulty()

    def handle_playing(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                b = Bullet(self.player.rect.centerx, self.player.rect.top)
                self.all_sprites.add(b); self.bullets.add(b)

        time_sec = self.model.update_difficulty()
        self.all_sprites.update()
        
        if random.randint(0, 100) < (2 + self.model.level):
            e = Enemy(self.W, self.model.level)
            self.all_sprites.add(e); self.enemies.add(e)

        pygame.sprite.groupcollide(self.bullets, self.enemies, True, True)
        if pygame.sprite.spritecollide(self.player, self.enemies, True):
            self.model.lives -= 1
            if self.model.lives <= 0:
                self.model.save_record()
                self.model.state = "MENU"

        self.screen.blit(self.view.bg, (0, 0))
        self.all_sprites.draw(self.screen)
        self.view.draw_hud(self.model, time_sec)

if __name__ == "__main__":
    GameLoveController().run()