import pygame
import sys

# Isometric Checkers
pygame.init()

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
DEBUG_MODE = False
GRID_SIZE = 10
TILE_WIDTH = 96
TILE_HEIGHT = 48
BACKGROUND_COLOR = (200, 200, 200)
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
HOVER_COLOR = (255, 255, 0)  # Yellow for hover effect

# Cube specifics
CUBE_COLOR_RED = (255, 0, 0)
CUBE_COLOR_GREEN = (0, 255, 0)
CUBE_COLOR_TOP_R = (200, 0, 0)
CUBE_COLOR_LEFT_R = (150, 0, 0)
CUBE_COLOR_RIGHT_R = (100, 0, 0)
CUBE_COLOR_TOP_G = (0, 200, 0)
CUBE_COLOR_LEFT_G = (0, 150, 0)
CUBE_COLOR_RIGHT_G = (0, 100, 0)

CUBE_WIDTH = TILE_WIDTH - 20
CUBE_HEIGHT = TILE_HEIGHT - 10
CUBE_HEIGHT_3D = 20

CUBE_LIST = [
    {"ID" : 1, "TEAMCOLOR" : "RED", "ALIVE" : True, "KINGED" : False, "INITIAL_COORD" : (0,0), "CURRENT_COORD" : [0,0]} ,
    {"ID" : 2, "TEAMCOLOR" : "RED", "ALIVE" : True, "KINGED" : False, "INITIAL_COORD" : (0,0), "CURRENT_COORD" : [0,0]},
    {"ID" : 3, "TEAMCOLOR" : "RED", "ALIVE" : True, "KINGED" : False, "INITIAL_COORD" : (0,0), "CURRENT_COORD" : [0,0]},
    {"ID" : 4, "TEAMCOLOR" : "GREEN", "ALIVE" : True, "KINGED" : False, "INITIAL_COORD" : (0,0), "CURRENT_COORD" : [0,0]},
    {"ID" : 5, "TEAMCOLOR" : "GREEN", "ALIVE" : True, "KINGED" : False, "INITIAL_COORD" : (0,0), "CURRENT_COORD" : [0,0]},
    {"ID" : 6, "TEAMCOLOR" : "GREEN", "ALIVE" : True, "KINGED" : False, "INITIAL_COORD" : (0,0), "CURRENT_COORD" : [0,0]}
]

CUBE_COLOR_LOGIC = [
    {"TEAMCOLOR" : "RED", "COLOR" : (CUBE_COLOR_TOP_R, CUBE_COLOR_LEFT_R, CUBE_COLOR_RIGHT_R)},
    {"TEAMCOLOR" : "GREEN", "COLOR" : (CUBE_COLOR_TOP_G, CUBE_COLOR_LEFT_G, CUBE_COLOR_RIGHT_G)}
]
# Load button image
BUTTON_IMAGE = pygame.image.load('C:/Users/091318/Downloads/gear.png')  # Replace with your button image path
BUTTON_RECT = BUTTON_IMAGE.get_rect()
BUTTON_RECT.topleft = (WINDOW_WIDTH - BUTTON_RECT.width - 10, 10)  # Position the button in the top-right corner

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Isometric Checkers")

class Board_setup:
    def draw_iso_tile(self, surface, color, x, y, border_color=None):
        """Draws an isometric tile with optional border color."""
        vertexes = [
            (x, y),
            (x + TILE_WIDTH // 2, y + TILE_HEIGHT // 2),
            (x, y + TILE_HEIGHT),
            (x - TILE_WIDTH // 2, y + TILE_HEIGHT // 2)
        ]
        pygame.draw.polygon(surface, color, vertexes)
        if border_color:
            pygame.draw.polygon(surface, border_color, vertexes, 3)  # Draw border with width of 3

    def index_to_letter(self, index):
        return chr(ord('A') + index)
    
    def setup_iso_grid(self, GRID_SIZE):
        TILESET = []
        grid_surface = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        grid_surface.fill(BACKGROUND_COLOR)
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                x = (col - row) * (TILE_WIDTH // 2) + WINDOW_WIDTH // 2
                y = (col + row) * (TILE_HEIGHT // 2) + WINDOW_HEIGHT // 4
                
                if (row + col) % 2 == 0:
                    TILE_COLOR = COLOR_WHITE
                    TILE_VALIDITY = False
                else:
                    TILE_COLOR = COLOR_BLACK
                    TILE_VALIDITY = True

                row_letter = self.index_to_letter(row)
                ADD_TILESET = {"TILEID" : row_letter + str(col+1), "POSITION" : (x, y), "COLOR" : TILE_COLOR, "TILE_VALIDITY" : TILE_VALIDITY, "TILE_IN_USE" : None}
                TILESET.append(ADD_TILESET)

                # Draw tile without borders for the initial board
                self.draw_iso_tile(grid_surface, TILE_COLOR, x, y)
               
        return TILESET, grid_surface


class DebugSetting:
    def __init__(self):
        self.debug_font = pygame.font.Font(None, 24)  # Initialize font once

    def draw_debug_panel(self, surface, tile_info):
        """Draws the debug panel showing only the hovered tile's information."""
        panel_width = 300
        panel_height = 150
        panel_surface = pygame.Surface((panel_width, panel_height))
        panel_surface.fill(COLOR_BLACK)
        
        if tile_info:
            # Format and render the hovered tile's dictionary in the panel
            headers = ["TILEID", "POSITION", "COLOR", "VALID", "IN_USE"]
            values = [str(tile_info[key]) for key in ["TILEID", "POSITION", "COLOR", "TILE_VALIDITY", "TILE_IN_USE"]]

            for i, header in enumerate(headers):
                text_surface = self.debug_font.render(f"{header}: {values[i]}", True, COLOR_WHITE)
                panel_surface.blit(text_surface, (5, 5 + i * 25))

        # Blit the panel onto the main surface
        surface.blit(panel_surface, (10, 10))  # Top-left corner position

    def draw_tileID(self, surface, TILESET):
        font = pygame.font.Font(None, 32)
        for tiles in TILESET:
            tile_color = tiles["COLOR"]
            tile_ID = tiles["TILEID"]
            tilex, tiley = tiles["POSITION"]
            text_color = COLOR_BLACK if tile_color == COLOR_WHITE else COLOR_WHITE
            text = font.render(tile_ID, True, text_color)
            text_rect = text.get_rect(center=(tilex, tiley+25))
            surface.blit(text, text_rect)

DEBUG_SETTING = DebugSetting()
SETUP_BOARD = Board_setup()
TILESET, grid_surface = SETUP_BOARD.setup_iso_grid(GRID_SIZE)

def point_in_polygon(point, polygon):
    """Check if a point is inside a polygon."""
    x, y = point
    inside = False
    n = len(polygon)
    p1x, p1y = polygon[0]
    for i in range(n + 1):
        p2x, p2y = polygon[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xints = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or x <= xints:
                        inside = not inside
        p1x, p1y = p2x, p2y
    return inside

def get_hovered_tile(tileset, mouse_pos):
    """Returns the tile dictionary if the mouse is hovering over a tile."""
    for tile in tileset:
        x, y = tile['POSITION']
        # Define the polygon points of the tile
        polygon = [
            (x, y),
            (x + TILE_WIDTH // 2, y + TILE_HEIGHT // 2),
            (x, y + TILE_HEIGHT),
            (x - TILE_WIDTH // 2, y + TILE_HEIGHT // 2)
        ]
        if point_in_polygon(mouse_pos, polygon):
            return tile
    return None

running = True
hovered_tile = None

while running:
    mouse_pos = pygame.mouse.get_pos()
    hovered_tile = get_hovered_tile(TILESET, mouse_pos)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if BUTTON_RECT.collidepoint(event.pos):
                DEBUG_MODE = not DEBUG_MODE
                print(f"DEBUG_MODE is now {'ON' if DEBUG_MODE else 'OFF'}")
                TILESET, grid_surface = SETUP_BOARD.setup_iso_grid(GRID_SIZE)  # Re-create the grid surface

    screen.fill(BACKGROUND_COLOR)
    screen.blit(grid_surface, (0, 0))
    screen.blit(BUTTON_IMAGE, BUTTON_RECT.topleft)

    # Redraw tiles with hover effect
    for tile in TILESET:
        x, y = tile['POSITION']
        tile_color = tile['COLOR']
        border_color = HOVER_COLOR if tile == hovered_tile else None
        SETUP_BOARD.draw_iso_tile(screen, tile_color, x, y, border_color)

    # Display the debug panel for the hovered tile
    if DEBUG_MODE:
        DEBUG_SETTING.draw_debug_panel(screen, hovered_tile)
        DEBUG_SETTING.draw_tileID(screen, TILESET)
    pygame.display.flip()


pygame.quit()
sys.exit()
