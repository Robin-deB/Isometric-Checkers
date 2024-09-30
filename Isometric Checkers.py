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
    {"ID" : 1, "TEAMCOLOR" : "RED", "ALIVE" : True, "KINGED" : False, "INIT_TILE_ID": "A2", "NEW COORDINATES" : [0,0], "OLD COORDINATES" : [0,0]},
    {"ID" : 2, "TEAMCOLOR" : "RED", "ALIVE" : True, "KINGED" : False, "INIT_TILE_ID": "A4", "NEW COORDINATES" : [0,0], "OLD COORDINATES" : [0,0]},
    {"ID" : 3, "TEAMCOLOR" : "RED", "ALIVE" : True, "KINGED" : False, "INIT_TILE_ID": "A6", "NEW COORDINATES" : [0,0], "OLD COORDINATES" : [0,0]},
    {"ID" : 4, "TEAMCOLOR" : "RED", "ALIVE" : True, "KINGED" : False, "INIT_TILE_ID": "A8", "NEW COORDINATES" : [0,0], "OLD COORDINATES" : [0,0]},
    {"ID" : 5, "TEAMCOLOR" : "RED", "ALIVE" : True, "KINGED" : False, "INIT_TILE_ID": "A10", "NEW COORDINATES" : [0,0], "OLD COORDINATES" : [0,0]},
    {"ID" : 6, "TEAMCOLOR" : "RED", "ALIVE" : True, "KINGED" : False, "INIT_TILE_ID": "B1", "NEW COORDINATES" : [0,0], "OLD COORDINATES" : [0,0]},
    {"ID" : 7, "TEAMCOLOR" : "RED", "ALIVE" : True, "KINGED" : False, "INIT_TILE_ID": "B3", "NEW COORDINATES" : [0,0], "OLD COORDINATES" : [0,0]},
    {"ID" : 8, "TEAMCOLOR" : "RED", "ALIVE" : True, "KINGED" : False, "INIT_TILE_ID": "B5", "NEW COORDINATES" : [0,0], "OLD COORDINATES" : [0,0]},
    {"ID" : 9, "TEAMCOLOR" : "RED", "ALIVE" : True, "KINGED" : False, "INIT_TILE_ID": "B7", "NEW COORDINATES" : [0,0], "OLD COORDINATES" : [0,0]},
    {"ID" : 10, "TEAMCOLOR" : "RED", "ALIVE" : True, "KINGED" : False, "INIT_TILE_ID": "B9", "NEW COORDINATES" : [0,0], "OLD COORDINATES" : [0,0]},
    {"ID" : 11, "TEAMCOLOR" : "GREEN", "ALIVE" : True, "KINGED" : False, "INIT_TILE_ID": "I2", "NEW COORDINATES" : [0,0], "OLD COORDINATES" : [0,0]},
    {"ID" : 12, "TEAMCOLOR" : "GREEN", "ALIVE" : True, "KINGED" : False, "INIT_TILE_ID": "I4", "NEW COORDINATES" : [0,0], "OLD COORDINATES" : [0,0]},
    {"ID" : 13, "TEAMCOLOR" : "GREEN", "ALIVE" : True, "KINGED" : False, "INIT_TILE_ID": "I6", "NEW COORDINATES" : [0,0], "OLD COORDINATES" : [0,0]},
    {"ID" : 14, "TEAMCOLOR" : "GREEN", "ALIVE" : True, "KINGED" : False, "INIT_TILE_ID": "I8", "NEW COORDINATES" : [0,0], "OLD COORDINATES" : [0,0]},
    {"ID" : 15, "TEAMCOLOR" : "GREEN", "ALIVE" : True, "KINGED" : False, "INIT_TILE_ID": "I10", "NEW COORDINATES" : [0,0], "OLD COORDINATES" : [0,0]},
    {"ID" : 16, "TEAMCOLOR" : "GREEN", "ALIVE" : True, "KINGED" : False, "INIT_TILE_ID": "J1", "NEW COORDINATES" : [0,0], "OLD COORDINATES" : [0,0]},
    {"ID" : 17, "TEAMCOLOR" : "GREEN", "ALIVE" : True, "KINGED" : False, "INIT_TILE_ID": "J3", "NEW COORDINATES" : [0,0], "OLD COORDINATES" : [0,0]},
    {"ID" : 18, "TEAMCOLOR" : "GREEN", "ALIVE" : True, "KINGED" : False, "INIT_TILE_ID": "J5", "NEW COORDINATES" : [0,0], "OLD COORDINATES" : [0,0]},
    {"ID" : 19, "TEAMCOLOR" : "GREEN", "ALIVE" : True, "KINGED" : False, "INIT_TILE_ID": "J7", "NEW COORDINATES" : [0,0], "OLD COORDINATES" : [0,0]},
    {"ID" : 20, "TEAMCOLOR" : "GREEN", "ALIVE" : True, "KINGED" : False, "INIT_TILE_ID": "J9", "NEW COORDINATES" : [0,0], "OLD COORDINATES" : [0,0]}    
]

BUTTON_IMAGE = pygame.image.load('C:/Users/091318/Downloads/gear.png')  
BUTTON_RECT = BUTTON_IMAGE.get_rect()
BUTTON_RECT.topleft = (WINDOW_WIDTH - BUTTON_RECT.width - 10, 10)  

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Isometric Checkers")

class Board_setup:
    def draw_iso_tile(self, surface, color, x, y, Tile_entry, border_color=None):
        topvx = (x,y)
        rightvx = (x + TILE_WIDTH // 2, y + TILE_HEIGHT // 2)
        bottomvx = (x, y + TILE_HEIGHT) 
        leftvx = (x - TILE_WIDTH // 2, y + TILE_HEIGHT // 2)    
        vertexes = [
            (topvx),
            (rightvx),
            (bottomvx),
            (leftvx)
        ]
        Tile_entry["VERTEXES"] = vertexes
        pygame.draw.polygon(surface, color, vertexes)
        if border_color:
            pygame.draw.polygon(surface, border_color, vertexes, 3)  #Used for the hovererd tile in tile_hover

    def index_to_letter(self, index):
        return chr(ord('A') + index)
    
    def setup_iso_grid(self, GRID_SIZE):
        TILE_SET = []
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
                Tile_entry = {"TILEID" : row_letter + str(col+1), "POSITION" : (x, y), "VERTEXES" : (), "COLOR" : TILE_COLOR, "TILE_VALIDITY" : TILE_VALIDITY, "TILE_IN_USE" : None}
                TILE_SET.append(Tile_entry)

                # Draw tile without borders for the initial board
                self.draw_iso_tile(grid_surface, TILE_COLOR, x, y, Tile_entry)
               
        return TILE_SET, grid_surface

class Draw_cubes:
    def draw_cubes(self, surface, CUBE_LIST, dragging_cube, selected_cube):
        total_cubes = len(CUBE_LIST)
        for cubes in CUBE_LIST[:total_cubes]:  
            cube_ID = cubes["ID"]
            cube_color = cubes["TEAMCOLOR"]

            if dragging_cube and cube_ID == selected_cube:
                cube_x, cube_y = cubes["NEW COORDINATES"]
                offset_y = -30
            else:
                cube_x, cube_y = cubes["OLD COORDINATES"]  
                offset_y = -15

            cube_alive = cubes["ALIVE"]
            cube_kinged = cubes["KINGED"]

            self.visualize_cubes(surface, cube_x, cube_y, offset_y, cube_alive, cube_color)

    
    def visualize_cubes(self, surface, cube_x, cube_y, offset_y, cube_alive, cube_color):
        if cube_alive:            
            if cube_color == "RED":
                color_top = CUBE_COLOR_TOP_R
                color_left = CUBE_COLOR_LEFT_R
                color_right = CUBE_COLOR_RIGHT_R
            else:
                color_top = CUBE_COLOR_TOP_G
                color_left = CUBE_COLOR_LEFT_G
                color_right = CUBE_COLOR_RIGHT_G                

            top_points = [
                (cube_x, cube_y + offset_y),
                (cube_x + CUBE_WIDTH // 2, cube_y + CUBE_HEIGHT // 2 + offset_y),
                (cube_x, cube_y + CUBE_HEIGHT + offset_y),
                (cube_x - CUBE_WIDTH // 2, cube_y + CUBE_HEIGHT // 2 + offset_y)
            ]
            pygame.draw.polygon(surface, color_top, top_points)
        
            left_points = [
                (cube_x - CUBE_WIDTH // 2, cube_y + CUBE_HEIGHT // 2 + offset_y),
                (cube_x, cube_y + CUBE_HEIGHT + offset_y),
                (cube_x, cube_y + CUBE_HEIGHT + offset_y + CUBE_HEIGHT_3D),
                (cube_x - CUBE_WIDTH // 2, cube_y + CUBE_HEIGHT // 2 + offset_y + CUBE_HEIGHT_3D)
            ]
            pygame.draw.polygon(surface, color_left, left_points)
                    
            right_points = [
                (cube_x + CUBE_WIDTH // 2, cube_y + CUBE_HEIGHT // 2 + offset_y),
                (cube_x, cube_y + CUBE_HEIGHT + offset_y),
                (cube_x, cube_y + CUBE_HEIGHT + offset_y + CUBE_HEIGHT_3D),
                (cube_x + CUBE_WIDTH // 2, cube_y + CUBE_HEIGHT // 2 + offset_y + CUBE_HEIGHT_3D)
            ]
            pygame.draw.polygon(surface, color_right, right_points)

class Game_logic:
    def check_valid_move():
        pass


class Hitbox_detection:
    def cube_hitbox(self, mouse_pos):
        for cube in CUBE_LIST:
            cube_x, cube_y = cube["OLD COORDINATES"]
            hitbox = [
                (cube_x - CUBE_WIDTH // 2, cube_y),
                (cube_x + CUBE_WIDTH // 2, cube_y),
                (cube_x + CUBE_WIDTH // 2, cube_y + CUBE_HEIGHT),
                (cube_x - CUBE_WIDTH // 2, cube_y + CUBE_HEIGHT // 2)     
            ]
            if self.hitbox_detection(mouse_pos, hitbox):
                selected_cube = cube["ID"]
                cube_hit = True
                return cube_hit, selected_cube
        return None, None

    def tile_hitbox(self, mouse_pos, dragging_cube, selected_cube): #USED FOR MOUSE/HOVER AND CUBE PLACEMENT DETECTION!
        for tile in TILE_SET:
            hitbox = tile["VERTEXES"]
            if self.hitbox_detection(mouse_pos, hitbox):
                hovered_tile = tile
                self.tile_hover(hovered_tile)
                if dragging_cube == True and isinstance(selected_cube, int): #default for both are False, None, unless a cube is selected and mouse_one is held.
                    return hovered_tile
        return None

    def tile_hover(self, hovered_tile):
        for tile in TILE_SET:
            x, y = tile["POSITION"]
            color = tile["COLOR"]
            border_color = HOVER_COLOR if tile == hovered_tile else None
            SETUP_BOARD.draw_iso_tile(grid_surface, color, x, y, tile, border_color)

    def hitbox_detection(self, mouse_pos, hitbox):
        mouse_x, mouse_y = mouse_pos          
        detection = False
        n = len(hitbox)
        p1x, p1y = hitbox[0]
        for i in range(n + 1):
            p2x, p2y = hitbox[i % n]
            if mouse_y > min(p1y, p2y):
                if mouse_y <= max(p1y, p2y):
                    if mouse_x <= max(p1x, p2x):
                        if p1y != p2y:
                            xints = (mouse_y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                        if p1x == p2x or mouse_x <= xints:
                            detection = not detection
            p1x, p1y = p2x, p2y
        return detection        

    def snap_to_tile_logic(self, mouse_pos, dragging_cube, selected_cube):
        if selected_cube is None:
            return
        
        picked_tile = self.tile_hitbox(mouse_pos, dragging_cube, selected_cube)
        
        if picked_tile is None:
            return
        
        picked_tile_coords = picked_tile["POSITION"]
        picked_tile_validity = picked_tile["TILE_VALIDITY"]
        selected_cube_old_coords = CUBE_LIST[selected_cube - 1]["OLD COORDINATES"]
        if picked_tile_validity:
            CUBE_LIST[selected_cube - 1]["OLD COORDINATES"] = [picked_tile_coords[0], picked_tile_coords[1]]
        else:
            CUBE_LIST[selected_cube - 1]["OLD COORDINATES"] = [selected_cube_old_coords[0], selected_cube_old_coords[1]]
        CUBE_LIST[selected_cube - 1]["NEW COORDINATES"] = CUBE_LIST[selected_cube - 1]["OLD COORDINATES"]

class DebugSetting:
    def __init__(self):
        self.debug_font = pygame.font.Font(None, 24)  # Initialize font once
        self.antialias = True  
        self.text_color = COLOR_WHITE

    def debug_panel_mouse_pos(self, surface, mouse_pos):
        panel_width = 200
        panel_height = 100
        panel2_surface = pygame.Surface((panel_width, panel_height))
        panel2_surface.fill(COLOR_BLACK)

        # Prepare multiline text
        mouse_info = f"Mouse Position :\nX = {mouse_pos[0]}\nY = {mouse_pos[1]}"
        lines = mouse_info.splitlines()  # Split text into lines

        # Render each line and blit it
        y_offset = 5  # Initial offset for the first line
        for line in lines:
            text_surface = self.debug_font.render(line, self.antialias, self.text_color)
            panel2_surface.blit(text_surface, (5, y_offset))
            y_offset += text_surface.get_height() + 5  # Move down for the next line (5 pixels of spacing)

        surface.blit(panel2_surface, (WINDOW_WIDTH - panel_width - 150, 10))  # Blit the panel onto the main surface

    def draw_debug_panel(self, surface, tile_info):
        """Draws the debug panel showing only the hovered tile's information."""
        panel_width = 300
        panel_height = 150
        panel_surface = pygame.Surface((panel_width, panel_height))
        panel_surface.fill(COLOR_BLACK)
        
        if tile_info:
            # Format and render the hovered tile's dictionary in the panel
            headers = ["TILEID", "POSITION", "VERTEXES", "COLOR", "VALID", "IN_USE"]
            values = [str(tile_info[key]) for key in ["TILEID", "POSITION", "VERTEXES", "COLOR", "TILE_VALIDITY", "TILE_IN_USE"]]

            for i, header in enumerate(headers):
                text_surface = self.debug_font.render(f"{header}: {values[i]}", True, COLOR_WHITE)
                panel_surface.blit(text_surface, (5, 5 + i * 25))

        # Blit the panel onto the main surface
        surface.blit(panel_surface, (10, 10))  # Top-left corner position

    def draw_tileID(self, surface, TILE_SET):
        font = pygame.font.Font(None, 32)
        for tiles in TILE_SET:
            tile_color = tiles["COLOR"]
            tile_ID = tiles["TILEID"]
            tilex, tiley = tiles["POSITION"]
            text_color = COLOR_BLACK if tile_color == COLOR_WHITE else COLOR_WHITE
            text = font.render(tile_ID, True, text_color)
            text_rect = text.get_rect(center=(tilex, tiley+25))
            surface.blit(text, text_rect)

DEBUG_SETTING = DebugSetting()
SETUP_BOARD = Board_setup()
SETUP_CUBES = Draw_cubes()
HITBOX_DETECTION = Hitbox_detection()
GAME_LOGIC = Game_logic()

TILE_SET, grid_surface = SETUP_BOARD.setup_iso_grid(GRID_SIZE)
for CUBE_ID in CUBE_LIST:
    for TILE_ID in TILE_SET:
        if CUBE_ID["INIT_TILE_ID"] == TILE_ID["TILEID"]:
            CUBE_ID["NEW COORDINATES"] = TILE_ID["POSITION"]
            CUBE_ID["OLD COORDINATES"] = TILE_ID["POSITION"]

running = True
dragging_cube = False
selected_cube = None
Tile_hover = None

while running:
    mouse_pos = pygame.mouse.get_pos()
    HITBOX_DETECTION.tile_hitbox(mouse_pos, dragging_cube, selected_cube)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if BUTTON_RECT.collidepoint(event.pos):
                DEBUG_MODE = not DEBUG_MODE
                print(f"DEBUG_MODE is now {'ON' if DEBUG_MODE else 'OFF'}")
                TILE_SET, grid_surface = SETUP_BOARD.setup_iso_grid(GRID_SIZE)  # Re-create the grid surface
            else:
                dragging_cube, selected_cube = HITBOX_DETECTION.cube_hitbox(mouse_pos)
                print(dragging_cube)
        elif event.type == pygame.MOUSEBUTTONUP:
            HITBOX_DETECTION.snap_to_tile_logic(mouse_pos, dragging_cube, selected_cube)
            dragging_cube = False
            selected_cube = None
                
        elif event.type == pygame.MOUSEMOTION:
            if dragging_cube:
                CUBE_LIST[selected_cube - 1]["NEW COORDINATES"] = [mouse_pos[0], mouse_pos[1]-30] #has a little bug where the cube moves position. This is because new coordinate and mouse_pos aren't equall. Fix later.

    screen.fill(BACKGROUND_COLOR)
    screen.blit(grid_surface, (0, 0))
    screen.blit(BUTTON_IMAGE, BUTTON_RECT.topleft)

    SETUP_CUBES.draw_cubes(screen, CUBE_LIST, dragging_cube, selected_cube) #currently this redraws all the cubes constantly, while it's only really needed when dragging a cube. Fix this later for better memory usage.
    
    if dragging_cube:
        print(dragging_cube)

    if DEBUG_MODE:
        DEBUG_SETTING.draw_tileID(screen, TILE_SET)
        DEBUG_SETTING.debug_panel_mouse_pos(screen, mouse_pos)

    pygame.display.flip()

pygame.quit()
sys.exit()
