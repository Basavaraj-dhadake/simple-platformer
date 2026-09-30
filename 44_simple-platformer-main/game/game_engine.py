import pygame
from .player import Player, MAX_FALL_SPEED
from .platform import Platform
from .hazard import Hazard
from .sounds import SoundManager

# Game Engine

WHITE = (255, 255, 255)
BROWN = (150, 100, 60)
RED = (220, 60, 60)
GREEN = (0, 200, 0)
YELLOW = (255, 220, 80)

# name: (gravity, jump strength)
DIFFICULTIES = {
    "Easy":   (0.5, -13.0),
    "Medium": (0.6, -12.0),
    "Hard":   (0.7, -12.5),
}
DIFFICULTY_KEYS = {
    pygame.K_1: "Easy", pygame.K_KP1: "Easy",
    pygame.K_2: "Medium", pygame.K_KP2: "Medium",
    pygame.K_3: "Hard", pygame.K_KP3: "Hard",
}


class GameEngine:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.difficulty = "Medium"
        self.gravity = DIFFICULTIES[self.difficulty][0]

        self.start_x, self.start_y = 40, height - 120
        self.player = Player(self.start_x, self.start_y)
        self.player.jump_strength = DIFFICULTIES[self.difficulty][1]

        # A simple hand-built level: platforms with gaps between them
        # (falling into a gap means falling off the bottom of the
        # screen), one hazard, and a goal near the right edge.
        ground_y = height - 40
        self.platforms = [
            Platform(0, ground_y, 160),
            Platform(220, ground_y, 140),
            Platform(420, ground_y - 60, 120),
            Platform(600, ground_y, 180),
        ]
        self.hazards = [Hazard(240, ground_y - 14, 100)]
        self.goal_x = 740

        self.score = 0
        self.font = pygame.font.SysFont("Arial", 30)
        self.big_font = pygame.font.SysFont("Arial", 56, bold=True)
        self.small_font = pygame.font.SysFont("Arial", 24)
        self.game_over = False
        self.quit_requested = False
        self.sounds = SoundManager()

    # ---------- state management ----------
    def start_game(self, difficulty):
        """(Re)start a run with the chosen difficulty."""
        self.difficulty = difficulty
        self.gravity, jump = DIFFICULTIES[difficulty]
        self.player = Player(self.start_x, self.start_y)
        self.player.jump_strength = jump
        self.score = 0
        self.game_over = False

    def end_game(self):
        if not self.game_over:
            self.game_over = True
            self.player.vx = 0
            self.sounds.play("die")

    # ---------- input ----------
    def handle_event(self, event):
        if event.type != pygame.KEYDOWN:
            return

        if self.game_over:
            if event.key in DIFFICULTY_KEYS:
                self.start_game(DIFFICULTY_KEYS[event.key])
            elif event.key in (pygame.K_ESCAPE, pygame.K_q):
                self.quit_requested = True
            return

        if event.key in (pygame.K_SPACE, pygame.K_UP, pygame.K_w):
            if self.player.jump():
                self.sounds.play("jump")

    def handle_input(self):
        if self.game_over:
            return
        keys = pygame.key.get_pressed()
        self.player.vx = 0
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.player.vx = -self.player.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.player.vx = self.player.speed

    # ---------- simulation ----------
    def update(self):
        if self.game_over:
            return

        player = self.player
        player.vy = min(player.vy + self.gravity, MAX_FALL_SPEED)  # terminal velocity
        player.x = max(0, player.x + player.vx)

        # Swept collision: remember where the feet were BEFORE moving, then
        # check whether the feet crossed the platform's top surface this frame.
        # This works at any fall speed, unlike a simple overlap test.
        prev_bottom = player.y + player.height
        player.y += player.vy
        new_bottom = player.y + player.height
        player.on_ground = False

        if player.vy >= 0:
            player_rect = player.rect()
            for platform in self.platforms:
                overlaps_x = (player_rect.right > platform.x and
                              player_rect.left < platform.x + platform.width)
                crossed_top = prev_bottom <= platform.y <= new_bottom
                if overlaps_x and crossed_top:
                    player.y = platform.y - player.height
                    player.vy = 0
                    player.on_ground = True
                    break

        for hazard in self.hazards:
            if player.rect().colliderect(hazard.rect()):
                self.end_game()
                return

        if player.y > self.height:
            self.end_game()
            return

        if player.x >= self.goal_x:
            self.score += 1
            self.sounds.play("goal")
            player.x, player.y = self.start_x, self.start_y
            player.vy = 0

    # ---------- drawing ----------
    def render(self, screen):
        for platform in self.platforms:
            pygame.draw.rect(screen, BROWN, platform.rect())
        for hazard in self.hazards:
            pygame.draw.rect(screen, RED, hazard.rect())

        goal_rect = pygame.Rect(self.goal_x, 0, 6, self.height)
        pygame.draw.rect(screen, GREEN, goal_rect)

        pygame.draw.rect(screen, WHITE, self.player.rect())

        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        screen.blit(score_text, (10, 10))
        diff_text = self.small_font.render(self.difficulty, True, WHITE)
        screen.blit(diff_text, (self.width - diff_text.get_width() - 10, 10))

        if self.game_over:
            self.render_game_over(screen)

    def render_game_over(self, screen):
        overlay = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 170))
        screen.blit(overlay, (0, 0))

        cx = self.width // 2
        lines = [
            (self.big_font, "GAME OVER", RED, 110),
            (self.font, f"Final Score: {self.score}", WHITE, 190),
            (self.small_font, "Play again - choose difficulty:", YELLOW, 260),
            (self.small_font, "1 - Easy     2 - Medium     3 - Hard", WHITE, 300),
            (self.small_font, "Esc / Q - Exit", WHITE, 350),
        ]
        for font, text, color, y in lines:
            surf = font.render(text, True, color)
            screen.blit(surf, (cx - surf.get_width() // 2, y))
