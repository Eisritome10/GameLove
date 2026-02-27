import pygame
import os

class GameModel:
    def __init__(self):
        self.data_path = os.path.join("data", "record.txt")
        # Cargamos nivel y tiempo récord: [Nivel, Tiempo]
        self.high_score_lvl, self.high_score_time = self.load_record()
        self.state = "MENU"
        self.difficulty_mode = 1 # 0: Facil, 1: Normal, 2: Dificil
        self.difficulty_names = ["FACIL", "NORMAL", "DIFICIL"]
        self.reset_state()

    def reset_state(self):
        self.score = 0
        self.lives = 3
        # El nivel inicial escala con la dificultad
        self.level = 1 + (self.difficulty_mode * 2) 
        self.start_ticks = pygame.time.get_ticks()
        self.current_session_time = 0

    def load_record(self):
        if not os.path.exists("data"): os.makedirs("data")
        if not os.path.exists(self.data_path): return 1, 0
        try:
            with open(self.data_path, "r") as f:
                data = f.read().split(",")
                return int(data[0]), int(data[1])
        except: return 1, 0

    def save_record(self):
        # Guarda si el nivel es mayor, o si es igual nivel pero duró más tiempo
        if (self.level > self.high_score_lvl) or \
           (self.level == self.high_score_lvl and self.current_session_time > self.high_score_time):
            self.high_score_lvl = self.level
            self.high_score_time = self.current_session_time
            with open(self.data_path, "w") as f:
                f.write(f"{self.level},{self.current_session_time}")

    def update_difficulty(self):
        self.current_session_time = (pygame.time.get_ticks() - self.start_ticks) // 1000
        # Multiplicador de progresión según dificultad
        multiplier = 15 if self.difficulty_mode == 2 else 20
        self.level = (1 + (self.difficulty_mode * 2)) + (self.current_session_time // multiplier)
        return self.current_session_time

    def cycle_difficulty(self):
        self.difficulty_mode = (self.difficulty_mode + 1) % 3