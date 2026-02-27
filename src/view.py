import pygame
import os

class GameView:
    def __init__(self, screen, w, h):
        self.screen = screen
        self.w, self.h = w, h
        self.font_title = pygame.font.SysFont("Consolas", 70, bold=True)
        self.font_ui = pygame.font.SysFont("Consolas", 25, bold=True)
        
        try:
            self.bg = pygame.transform.scale(pygame.image.load(os.path.join("assets", "images", "background.jpg")).convert(), (w, h))
            self.heart = pygame.transform.scale(pygame.image.load(os.path.join("assets", "images", "corazon.png")).convert_alpha(), (28, 28))
        except:
            self.bg = pygame.Surface((w, h)); self.bg.fill((20, 20, 30))
            self.heart = pygame.Surface((25, 25)); self.heart.fill((255, 0, 0))

    def draw_menu(self, hi_lvl, hi_time, diff_name, diff_idx):
        self.screen.blit(self.bg, (0, 0))
        colors = [(100, 255, 100), (255, 255, 100), (255, 100, 100)]
        
        title = self.font_title.render("GAMELOVE", True, (255, 100, 150))
        record = self.font_ui.render(f"RECORD: NIVEL {hi_lvl} ({hi_time}s)", True, (255, 255, 255))
        diff = self.font_ui.render(f"DIFICULTAD: < {diff_name} >", True, colors[diff_idx])
        hint = self.font_ui.render("ENTER para jugar | 'D' para dificultad", True, (180, 180, 180))
        
        self.screen.blit(title, (self.w//2 - 170, self.h//2 - 150))
        self.screen.blit(record, (self.w//2 - 200, self.h//2 - 30))
        self.screen.blit(diff, (self.w//2 - 150, self.h//2 + 50))
        self.screen.blit(hint, (self.w//2 - 240, self.h//2 + 150))

    def draw_hud(self, model, time_sec):
        self.screen.blit(self.font_ui.render(f"SCORE: {model.score}", True, (255, 215, 0)), (20, 20))
        self.screen.blit(self.font_ui.render(f"LVL: {model.level}", True, (255, 255, 255)), (self.w - 180, 20))
        self.screen.blit(self.font_ui.render(f"TIME: {time_sec}s", True, (200, 200, 200)), (self.w - 180, 55))
        for i in range(model.lives):
            self.screen.blit(self.heart, (20 + (i * 35), 60))