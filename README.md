# Rigidbody Tetris 

This is a physics simulation project using **Pygame** and **Pymunk**, where traditional Tetris pieces fall and interact under the influence of gravity and real rigid body physics.



Unlike standard Tetris, this version doesn't follow a grid. Instead, pieces behave like physical objects — falling, rotating, colliding, and stacking naturally due to physics.

Each piece is built from multiple rigid square blocks and responds to gravity, friction, and bounce using the Pymunk physics engine.

## Overleaf

https://www.overleaf.com/read/vnyjdhjzjkvq#a9e023

## Controls

| Key         | Action                    |
|-------------|---------------------------|
| `SPACE`     | Drop a new Tetris piece   |
| `P`         | Pause/Resume simulation   |
| `C`         | Clear all pieces          |



## How to Run

1. Install Python 3
2. Install required libraries:

```bash
pip install pygame pymunk
```
3. Run the Script

```bash
python sim.py
```

## Libraries Used
* Pygame – For rendering graphics and handling input
* Pymunk – A 2D rigid body physics engine wrapper 
