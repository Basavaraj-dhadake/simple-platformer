"""Collision bug demo. Copy into the project root (next to main.py) and run:
    python bug_demo.py
The player is dropped from far above the raised middle platform.
  BEFORE the fix: the player falls straight THROUGH the platform.
  AFTER the fix : the player LANDS on the platform.
Press R to drop again, Esc to quit."""
import pygame
from game.game_engine import GameEngine

pygame.init()
W, H = 800, 500
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Collision bug demo - press R to drop again")
clock = pygame.time.Clock()
engine = GameEngine(W, H)

def drop():
    if hasattr(engine, "start_game"):
        engine.start_game("Medium")
    else:
        engine.game_over = False
        engine._game_over_logged = False
    engine.player.x, engine.player.y, engine.player.vy = 450, -5000, 0

drop()
running = True
while running:
    screen.fill((100, 160, 220))
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT or (ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE):
            running = False
        elif ev.type == pygame.KEYDOWN and ev.key == pygame.K_r:
            drop()
    engine.update()
    engine.render(screen)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
