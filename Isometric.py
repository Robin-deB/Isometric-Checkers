import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
GRID_SIZE = 10
TILE_WIDTH = 96
TILE_HEIGHT = 48
BACKGROUND_COLOR = (200, 200, 200)
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
CUBE_COLOR_RED = (255, 0, 0)
CUBE_COLOR_GREEN = (0, 255, 0)
CUBE_COLOR_TOP_R = (200, 0, 0)
CUBE_COLOR_LEFT_R = (150, 0, 0)
CUBE_COLOR_RIGHT_R = (100, 0, 0)
CUBE_COLOR_TOP_G = (0, 200, 0)
CUBE_COLOR_LEFT_G = (0, 150, 0)
CUBE_COLOR_RIGHT_G = (0, 100, 0)

# Cube size
CUBE_WIDTH = TILE_WIDTH - 20
CUBE_HEIGHT = TILE_HEIGHT - 10
CUBE_HEIGHT_3D = 20

# Set up the screen
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Isometric Grid with Red and Green Cubes")

# Player cubes
Red_player_cubes = [
    (1, 688, 189, CUBE_COLOR_TOP_R, CUBE_COLOR_LEFT_R, CUBE_COLOR_RIGHT_R),
    (2, 784, 237, CUBE_COLOR_TOP_R, CUBE_COLOR_LEFT_R, CUBE_COLOR_RIGHT_R),
    (3, 880, 285, CUBE_COLOR_TOP_R, CUBE_COLOR_LEFT_R, CUBE_COLOR_RIGHT_R),
    (4, 976, 333, CUBE_COLOR_TOP_R, CUBE_COLOR_LEFT_R, CUBE_COLOR_RIGHT_R),
    (5, 1072, 381, CUBE_COLOR_TOP_R, CUBE_COLOR_LEFT_R, CUBE_COLOR_RIGHT_R)
]

Green_player_cubes = [
    (1, 208, 381, CUBE_COLOR_TOP_G, CUBE_COLOR_LEFT_G, CUBE_COLOR_RIGHT_G),
    (2, 304, 429, CUBE_COLOR_TOP_G, CUBE_COLOR_LEFT_G, CUBE_COLOR_RIGHT_G),
    (3, 400, 477, CUBE_COLOR_TOP_G, CUBE_COLOR_LEFT_G, CUBE_COLOR_RIGHT_G),
    (4, 496, 525, CUBE_COLOR_TOP_G, CUBE_COLOR_LEFT_G, CUBE_COLOR_RIGHT_G),
    (5, 592, 573, CUBE_COLOR_TOP_G, CUBE_COLOR_LEFT_G, CUBE_COLOR_RIGHT_G)
]

all_cubes = Red_player_cubes + Green_player_cubes  # Combine both players' cubes

def draw_iso_tile(surface, color, x, y):
    points = [
        (x, y),
        (x + TILE_WIDTH // 2, y + TILE_HEIGHT // 2),
        (x, y + TILE_HEIGHT),
        (x - TILE_WIDTH // 2, y + TILE_HEIGHT // 2)
    ]
    pygame.draw.polygon(surface, color, points)

def draw_iso_grid(surface, grid_size):
    tiles = []
    for row in range(grid_size):
        for col in range(grid_size):
            x = (col - row) * (TILE_WIDTH // 2) + WINDOW_WIDTH // 2
            y = (col + row) * (TILE_HEIGHT // 2) + WINDOW_HEIGHT // 4
            tiles.append((x, y))
            tile_color = COLOR_WHITE if (row + col) % 2 == 0 else COLOR_BLACK
            draw_iso_tile(surface, tile_color, x, y)
    return tiles

def draw_iso_cube(surface, x, y, color_top, color_left, color_right, lift=False):
    offset_y = -10 if lift else 0
    top_points = [
        (x, y + offset_y),
        (x + CUBE_WIDTH // 2, y + CUBE_HEIGHT // 2 + offset_y),
        (x, y + CUBE_HEIGHT + offset_y),
        (x - CUBE_WIDTH // 2, y + CUBE_HEIGHT // 2 + offset_y)
    ]
    pygame.draw.polygon(surface, color_top, top_points)
    
    left_points = [
        (x - CUBE_WIDTH // 2, y + CUBE_HEIGHT // 2 + offset_y),
        (x, y + CUBE_HEIGHT + offset_y),
        (x, y + CUBE_HEIGHT + offset_y + CUBE_HEIGHT_3D),
        (x - CUBE_WIDTH // 2, y + CUBE_HEIGHT // 2 + offset_y + CUBE_HEIGHT_3D)
    ]
    pygame.draw.polygon(surface, color_left, left_points)
    
    right_points = [
        (x + CUBE_WIDTH // 2, y + CUBE_HEIGHT // 2 + offset_y),
        (x, y + CUBE_HEIGHT + offset_y),
        (x, y + CUBE_HEIGHT + offset_y + CUBE_HEIGHT_3D),
        (x + CUBE_WIDTH // 2, y + CUBE_HEIGHT // 2 + offset_y + CUBE_HEIGHT_3D)
    ]
    pygame.draw.polygon(surface, color_right, right_points)

def draw_cubes(surface, cubes, cube_selected=None):
    for i, (_, x, y, color_top, color_left, color_right) in enumerate(cubes):
        if i != cube_selected:  # Only draw the cube if it's not the selected one
            draw_iso_cube(surface, x, y, color_top, color_left, color_right)

def snap_to_grid(mouse_x, mouse_y, tiles, occupied_tiles):
    closest_tile = min(tiles, key=lambda t: (t[0] - mouse_x) ** 2 + (t[1] - mouse_y) ** 2)
    
    if closest_tile not in occupied_tiles:  # Ensure the tile isn't occupied
        cube_x = closest_tile[0]
        cube_y = closest_tile[1] + (TILE_HEIGHT - CUBE_HEIGHT - 25)
        return cube_x, cube_y, closest_tile
    return None, None, None

# Main loop
running = True
fullscreen = False
cube_selected = None  # No cube is selected initially
cube_x, cube_y = 0, 0
original_cube_position = None  # Track the original position of the selected cube
tiles = []
occupied_tiles = [(x, y + (TILE_HEIGHT - CUBE_HEIGHT - 25)) for _, x, y, _, _, _ in all_cubes]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_f:
                fullscreen = not fullscreen
                if fullscreen:
                    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                else:
                    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            for i, (_, x, y, _, _, _) in enumerate(all_cubes):
                if abs(mouse_x - x) < CUBE_WIDTH // 2 and abs(mouse_y - y) < CUBE_HEIGHT:
                    cube_selected = i  # Select the cube by index
                    original_cube_position = (x, y)  # Store original position
                    break
        elif event.type == pygame.MOUSEBUTTONUP:
            if cube_selected is not None:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                new_x, new_y, tile_position = snap_to_grid(mouse_x, mouse_y, tiles, occupied_tiles)
                
                if new_x is not None:  # If valid placement
                    _, _, _, color_top, color_left, color_right = all_cubes[cube_selected]
                    all_cubes[cube_selected] = (cube_selected, new_x, new_y, color_top, color_left, color_right)
                    
                    # Update occupied tiles
                    occupied_tiles.append(tile_position)
                else:  # Invalid placement, reset to original position
                    all_cubes[cube_selected] = (cube_selected, *original_cube_position, *all_cubes[cube_selected][3:])
                
                cube_selected = None  # Deselect the cube

    if cube_selected is not None:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        cube_x, cube_y = mouse_x, mouse_y
    
    screen.fill(BACKGROUND_COLOR)
    tiles = draw_iso_grid(screen, GRID_SIZE)
    
    # Draw all cubes except the one being dragged
    draw_cubes(screen, all_cubes, cube_selected=cube_selected)
    
    # If a cube is selected, show it following the mouse
    if cube_selected is not None:
        _, _, _, color_top, color_left, color_right = all_cubes[cube_selected]
        draw_iso_cube(screen, cube_x, cube_y, color_top, color_left, color_right, lift=True)

    pygame.display.flip()

pygame.quit()
sys.exit()
