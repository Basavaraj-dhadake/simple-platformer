 # Real-Time Simple Platformer Game 

This repository contains my completed and improved version of the **Real-Time Simple Platformer Game** assigned through the SETAPESU26 repository.

The original project was a partially working Pygame platformer. I ran the original version, recorded the gameplay before making changes, investigated the issues using an LLM as a debugging and pair-programming partner, fixed the broken behavior, added all required features, tested the updated game, and pushed the completed project to my own GitHub repository.

---

## Project Overview

This project is a real-time 2D platformer game built using **Python and Pygame**.

The game includes:

- Player movement
- Gravity and jumping
- Platforms
- Hazards
- Goal/score system
- Collision detection
- Game Over screen
- Final score display
- Replay functionality
- Difficulty selection
- Sound effects




## Development Process

I followed the required workflow:

1. Opened the assigned repository.
2. Read the original README and understood the required tasks.
3. Downloaded/cloned the project.
4. Installed the required Python dependencies.
5. Ran the original game.
6. Recorded gameplay before making changes.
7. Used an LLM as a debugging and pair-programming assistant.
8. Fixed the broken collision behavior.
9. Added the required Game Over system.
10. Added replay and difficulty selection.
11. Added sound feedback.
12. Tested the completed game.
13. Recorded gameplay after making the changes.
14. Pushed the completed project to my own GitHub repository.
15. Did not create a Pull Request to the main `SETAPESU26` repository.

---

## AI / LLM Development Conversation

The AI conversation used during the development, debugging, and feature implementation is available here:

https://claude.ai/share/bc88ec3d-faf5-4955-b4cb-9e584ec25975

The conversation contains the prompts and development discussion used during the project.

---

# Tasks Completed

## Task 1: Refine Collision Detection

### Original Issue

The original game could allow the player to fall through a platform, particularly after falling at a higher speed.

### Changes Made

The collision detection was improved so that platform landings are detected more reliably.

The updated collision behavior checks the player's movement and platform positions so that the player can correctly land on platforms from above.

### Result

- Player can land correctly on platforms.
- Falling through platforms is reduced/fixed.
- Platform collision works more reliably during jumping and falling.

---

## Task 2: Implement Game Over Condition

### Original Issue

The original game did not provide a proper graphical Game Over experience when the player died.

### Changes Made

A Game Over system was added.

The game now detects when the player:

- Touches a hazard.
- Falls below the bottom of the screen.

After the player dies, a Game Over screen is displayed instead of simply ending the gameplay.

The final score is also displayed.

### Result

The player receives clear visual feedback when the game ends and can see the final score.

---

## Task 3: Add Replay Option

### Original Issue

The original game did not provide a complete replay flow after Game Over.

### Changes Made

A replay system was added.

After Game Over, the player can choose a difficulty or exit the game.

### Difficulty Options

| Key | Difficulty |
|---|---|
| `1` | Easy |
| `2` | Medium |
| `3` | Hard |

The difficulty changes the gameplay parameters such as gravity/jump strength.

### Result

The player can start another game without closing and reopening the program.

---

## Task 4: Add Sound Feedback

### Original Issue

The original game did not provide sound feedback for important gameplay events.

### Changes Made

Basic sound effects were added for:

- Jumping
- Reaching the goal
- Dying

The sound functionality is implemented in:

```text
game/sounds.py
