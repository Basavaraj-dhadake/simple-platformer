# Real-Time Simple Platformer Game

This project is a terminal-based platformer using **Pygame**. It introduces students to interactive game design using object-oriented principles and real-time graphical rendering.

---

## What’s Provided

A partially working version of a platformer with:

- A player-controlled character with left/right movement, gravity, and jumping
- A small hand-built level of platforms with gaps and one hazard
- Score display

You are expected to **analyze**, **interact with an AI assistant**, and **complete/fix** the game to make it fully functional.

### **Use an LLM (e.g. ChatGPT or Claude) as your debugging and pair-programming partner for this lab.**

---

## Getting Started

### Setup

1. Clone the repo or download the project folder.
2. Make sure you have Python 3.10+ installed.
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the game:

```bash
python main.py
```

---


## Tasks to Complete

Each task must be completed using an iterative process involving LLM suggestions and your critical code review.

### Task 1: Refine Collision Detection

> The player sometimes falls straight through a platform instead of landing on it, especially after a long fall. Investigate and enhance collision accuracy so landings register reliably regardless of fall speed.


### Task 2: Implement Game Over Condition

> Add a screen that displays the final score once the player falls off the bottom of the screen or touches a hazard, then gracefully waits for input instead of just printing to the console.


### Task 3: Add Replay Option

> After Game Over, allow the user to play again by choosing a difficulty (Easy, Medium, or Hard gravity/jump strength), or exit.


### Task 4: Add Sound Feedback

> Add basic sound effects for jumping, reaching the goal, and dying.


---

## Expected Behavior

- Smooth left/right movement using `Left`/`Right` or `A`/`D`, and jumping with `Space`/`Up`/`W`
- Gravity pulls the player down and platforms stop the fall when landed on from above
- Touching the hazard or falling off the bottom of the screen ends the game
- Reaching the goal at the right edge increases the score and sends the player back to the start
- Score is visible on screen at all times

---

## Folder Structure

```
simple-platformer-main/
├── main.py
├── requirements.txt
├── game/
│   ├── game_engine.py
│   ├── player.py
│   ├── platform.py
│   └── hazard.py
└── README.md
```

---

## Submission Checklist

Submission is only the following three things:

- [] A 10-second video of gameplay **before** your changes, showing the bug/broken behavior
- [] A 10-second video of gameplay **after** your changes, showing the bug fixed and the new features working
- [] The Chat/LLM used page link, with the complete chat history
---

## Solutions Implemented

- **Task 1 – Collision:** added a terminal velocity cap (`MAX_FALL_SPEED`) and *swept* landing detection: the player's feet position before the move is compared to the platform top, so a platform can no longer be skipped in a single frame. Landing also requires horizontal overlap, and is only checked while falling.
- **Task 2 – Game Over:** a dimmed "GAME OVER" overlay with the final score is drawn in-game (no more console print); the game freezes and waits for input.
- **Task 3 – Replay:** on Game Over press `1` Easy, `2` Medium, `3` Hard to restart (gravity/jump strength change per difficulty), or `Esc`/`Q` to exit.
- **Task 4 – Sound:** `game/sounds.py` synthesizes jump, goal and death sounds in code (no asset files). If no audio device exists, the game runs silently.
