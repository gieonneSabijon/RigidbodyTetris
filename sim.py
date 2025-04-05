import pygame
import pymunk
import pymunk.pygame_util
import random

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.font.init()
font = pygame.font.SysFont("Arial", 24)
pygame.display.set_caption("Rigidbody Tetris")

space = pymunk.Space()
space.gravity = (0, 980)  # Gravity in pixels/sec^2

WHITE = (255, 255, 255)
COLORS = [(255, 0, 0, 255), (0, 255, 0, 255), (0, 0, 255, 255), (255, 255, 0, 255), (255, 165, 0, 255)]

draw_options = pymunk.pygame_util.DrawOptions(screen)

# Floor and Walls
floor = pymunk.Body(body_type=pymunk.Body.STATIC)
floor_shape = pymunk.Segment(floor, (0, HEIGHT), (WIDTH, HEIGHT), 5)
floor_shape.elasticity = 0.2  # Bounce
floor_shape.friction = 0.8  # Slows down rolling
space.add(floor, floor_shape)
wall_thickness = 5
left_wall = pymunk.Segment(floor, (0, 0), (0, HEIGHT), wall_thickness)
left_wall.elasticity = 0.2
left_wall.friction = 0.8
right_wall = pymunk.Segment(floor, (WIDTH, 0), (WIDTH, HEIGHT), wall_thickness)
right_wall.elasticity = 0.2
right_wall.friction = 0.8
space.add(left_wall, right_wall)

# Tetris piece shapes
def get_tetris_shapes(size):
    return {
        "I": [(0, 0), (size, 0), (2 * size, 0), (3 * size, 0)],
        "O": [(0, 0), (size, 0), (0, size), (size, size)],
        "T": [(0, 0), (-size, 0), (size, 0), (0, size)],
        "L": [(0, 0), (0, -size), (0, size), (size, size)],
        "J": [(0, 0), (0, -size), (0, size), (-size, size)],
        "S": [(0, 0), (size, 0), (0, size), (-size, size)],
        "Z": [(0, 0), (-size, 0), (0, size), (size, size)],
    }

def create_tetris_piece(x, y):
    size = 40
    shapes_dict = get_tetris_shapes(size)
    shape_type = random.choice(list(shapes_dict.keys()))
    offsets = shapes_dict[shape_type]

    mass = 1 * len(offsets)
    moment = pymunk.moment_for_box(mass, (size, size)) * len(offsets)
    body = pymunk.Body(mass, moment)
    body.position = x, y
    body.angle = random.uniform(-0.5, 0.5)

    space.add(body)
    piece_color = random.choice(COLORS)

    for ox, oy in offsets:
        
        half = size / 2
        verts = [
            (ox - half, oy - half),
            (ox + half, oy - half),
            (ox + half, oy + half),
            (ox - half, oy + half),
        ]

        shape = pymunk.Poly(body, verts)
        shape.color = piece_color
        shape.elasticity = 0.2
        shape.friction = 0.5
        space.add(shape)

    return body

def clear_pieces(pieceList):
    for body in pieceList:
        for shape in body.shapes:
            space.remove(shape)
        space.remove(body)
    pieceList.clear()


#Sim Loop
clock = pygame.time.Clock()
running = True
paused = False

piece_count = 0
pieceList = []

while running:
    screen.fill(WHITE)
    

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False
        elif event.type == pygame.KEYDOWN: #Spawn Piece
            if event.key == pygame.K_SPACE:
                x = random.randint(100, WIDTH - 100)
                pieceList.append(create_tetris_piece(x, 50))
            elif event.key == pygame.K_p: #Pause/Resume
                paused = not paused 
            elif event.key == pygame.K_c: #Clear Pieces
                clear_pieces(pieceList)


    # Update physics
    if not paused:
        space.step(1 / 60)

    piece_count = len(pieceList)

    # Draw Pieces
    space.debug_draw(draw_options)


    #Screen Text
    pieceCountText = font.render(f"Piece Count: {piece_count}", True, (0, 0, 0))
    screen.blit(pieceCountText, (10, 10))

    pauseText = font.render(f"Press 'p' to pause/resume", True, (0, 0, 0))
    screen.blit(pauseText, (10, 40))

    clearText = font.render(f"Press 'c' to clear pieces", True, (0, 0, 0))
    screen.blit(clearText, (10, 70))

    spawnText = font.render(f"Press 'SPACE' to spawn pieces", True, (0, 0, 0))
    screen.blit(spawnText, (10, 100))

    # Refresh Screen
    pygame.display.flip()
    clock.tick(60)

pygame.quit()