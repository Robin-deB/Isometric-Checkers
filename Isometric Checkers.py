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
CUBE_COLOR_TOP_R_H = (250, 0, 0)
CUBE_COLOR_LEFT_R_H = (225, 0, 0)
CUBE_COLOR_RIGHT_R_H = (200, 0, 0)
CUBE_COLOR_TOP_G = (0, 200, 0)
CUBE_COLOR_LEFT_G = (0, 150, 0)
CUBE_COLOR_RIGHT_G = (0, 100, 0)
CUBE_COLOR_TOP_G_H = (0, 250, 0)
CUBE_COLOR_LEFT_G_H = (0, 225, 0)
CUBE_COLOR_RIGHT_G_H = (0, 200, 0)
DEBUG_COLOR_KINGED = (255, 255, 0)

CUBE_WIDTH = TILE_WIDTH - 20
CUBE_HEIGHT = TILE_HEIGHT - 10
CUBE_HEIGHT_3D = 20

CROWN_IMAGE = pygame.image.load("C:/Users/091318/OneDrive - Stedin Groep/Robin/Coding/Python/money.png")
CROWN_IMAGE = pygame.transform.scale(CROWN_IMAGE, (40, 30))

CUBE_LIST = [
    {"ID" : 1, "TEAMCOLOR" : "RED", "ALIVE" : True, "KINGED" : False, "INIT_TILE_ID": "A2", "COORDINATES" : [0,0]},
    {"ID" : 2, "TEAMCOLOR" : "RED", "ALIVE" : True, "KINGED" : False, "INIT_TILE_ID": "A4", "COORDINATES" : [0,0]},
    {"ID" : 3, "TEAMCOLOR" : "RED", "ALIVE" : True, "KINGED" : False, "INIT_TILE_ID": "A6", "COORDINATES" : [0,0]},
    {"ID" : 4, "TEAMCOLOR" : "RED", "ALIVE" : True, "KINGED" : False, "INIT_TILE_ID": "A8", "COORDINATES" : [0,0]},
    {"ID" : 5, "TEAMCOLOR" : "RED", "ALIVE" : True, "KINGED" : False, "INIT_TILE_ID": "A10", "COORDINATES" : [0,0]},
    {"ID" : 6, "TEAMCOLOR" : "RED", "ALIVE" : True, "KINGED" : False, "INIT_TILE_ID": "B1", "COORDINATES" : [0,0]},
    {"ID" : 7, "TEAMCOLOR" : "RED", "ALIVE" : True, "KINGED" : False, "INIT_TILE_ID": "B3", "COORDINATES" : [0,0]},
    {"ID" : 8, "TEAMCOLOR" : "RED", "ALIVE" : True, "KINGED" : False, "INIT_TILE_ID": "B5", "COORDINATES" : [0,0]},
    {"ID" : 9, "TEAMCOLOR" : "RED", "ALIVE" : True, "KINGED" : False, "INIT_TILE_ID": "B7", "COORDINATES" : [0,0]},
    {"ID" : 10, "TEAMCOLOR" : "RED", "ALIVE" : True, "KINGED" : False, "INIT_TILE_ID": "B9", "COORDINATES" : [0,0]},
    {"ID" : 11, "TEAMCOLOR" : "GREEN", "ALIVE" : True, "KINGED" : False, "INIT_TILE_ID": "I2", "COORDINATES" : [0,0]},
    {"ID" : 12, "TEAMCOLOR" : "GREEN", "ALIVE" : True, "KINGED" : False, "INIT_TILE_ID": "I4", "COORDINATES" : [0,0]},
    {"ID" : 13, "TEAMCOLOR" : "GREEN", "ALIVE" : True, "KINGED" : False, "INIT_TILE_ID": "I6", "COORDINATES" : [0,0]},
    {"ID" : 14, "TEAMCOLOR" : "GREEN", "ALIVE" : True, "KINGED" : False, "INIT_TILE_ID": "I8", "COORDINATES" : [0,0]},
    {"ID" : 15, "TEAMCOLOR" : "GREEN", "ALIVE" : True, "KINGED" : False, "INIT_TILE_ID": "I10", "COORDINATES" : [0,0]},
    {"ID" : 16, "TEAMCOLOR" : "GREEN", "ALIVE" : True, "KINGED" : False, "INIT_TILE_ID": "J1", "COORDINATES" : [0,0]},
    {"ID" : 17, "TEAMCOLOR" : "GREEN", "ALIVE" : True, "KINGED" : False, "INIT_TILE_ID": "J3", "COORDINATES" : [0,0]},
    {"ID" : 18, "TEAMCOLOR" : "GREEN", "ALIVE" : True, "KINGED" : False, "INIT_TILE_ID": "J5", "COORDINATES" : [0,0]},
    {"ID" : 19, "TEAMCOLOR" : "GREEN", "ALIVE" : True, "KINGED" : False, "INIT_TILE_ID": "J7", "COORDINATES" : [0,0]},
    {"ID" : 20, "TEAMCOLOR" : "GREEN", "ALIVE" : True, "KINGED" : False, "INIT_TILE_ID": "J9", "COORDINATES" : [0,0]}    
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
        VERTICES = [
            (topvx),
            (rightvx),
            (bottomvx),
            (leftvx)
        ]
        Tile_entry["VERTICES"] = VERTICES
        pygame.draw.polygon(surface, color, VERTICES)
        if border_color:
            pygame.draw.polygon(surface, border_color, VERTICES, 3)  #Used for the hovererd tile in tile_hover

    def index_to_letter(self, index):
        return chr(ord('A') + index)
    
    def setup_iso_grid(self, GRID_SIZE):
        TILE_SET = []
        grid_surface = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        grid_surface.fill(BACKGROUND_COLOR)
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                print(f"Row: {row}, Col: {col}")
                x = (col - row) * (TILE_WIDTH // 2) + WINDOW_WIDTH // 2
                y = (col + row) * (TILE_HEIGHT // 2) + WINDOW_HEIGHT // 4
                
                if (row + col) % 2 == 0:
                    TILE_COLOR = COLOR_WHITE
                    TILE_VALIDITY = False
                else:
                    TILE_COLOR = COLOR_BLACK
                    TILE_VALIDITY = True

                row_letter = self.index_to_letter(row)
                Tile_entry = {"TILEID" : row_letter + str(col+1), "POSITION" : (x, y), "VERTICES" : (), "COLOR" : TILE_COLOR, "TILE_VALIDITY" : TILE_VALIDITY, "TILE_IN_USE" : None,"TEAM_COLOR" : None, "TILE_COL_ROW" : (col, row)}
                TILE_SET.append(Tile_entry)

                # Draw tile without borders for the initial board
                self.draw_iso_tile(grid_surface, TILE_COLOR, x, y, Tile_entry)
               
        return TILE_SET, grid_surface

class Draw_cubes:
    def draw_cubes(self, surface, CUBE_LIST, cube_dragging, selected_cube_drag, cube_hover, selected_cube_hover):
        total_cubes = len(CUBE_LIST)
        for cubes in CUBE_LIST[:total_cubes]:  
            cube_ID = cubes["ID"]
            cube_color = cubes["TEAMCOLOR"]
            cube_alive = cubes["ALIVE"]
            cube_kinged = cubes["KINGED"]

            if cube_alive:
                if cube_dragging is True and isinstance(selected_cube_drag, int) and selected_cube_drag == cube_ID:
                    cube_x, cube_y = pygame.mouse.get_pos()
                    offset_y = -40
                    self.visualize_cubes(surface, cube_x, cube_y, offset_y, cube_color, True, cube_kinged)

                elif cube_hover is True and isinstance(selected_cube_hover, int) and selected_cube_hover == cube_ID and cube_dragging == False:
                    cube_x, cube_y = cubes["COORDINATES"]  
                    offset_y = -15
                    self.visualize_cubes(surface, cube_x, cube_y, offset_y, cube_color, True, cube_kinged)

                else:
                    cube_x, cube_y = cubes["COORDINATES"]  
                    offset_y = -15
                    self.visualize_cubes(surface, cube_x, cube_y, offset_y, cube_color, False, cube_kinged)
       
            else:
                break
    
    def visualize_cubes(self, surface, cube_x, cube_y, offset_y, cube_color, cube_hover, cube_kinged):      
        if cube_color == "RED" and cube_hover == False:
            color_top = CUBE_COLOR_TOP_R
            color_left = CUBE_COLOR_LEFT_R
            color_right = CUBE_COLOR_RIGHT_R
        elif cube_color == "GREEN" and cube_hover == False:
            color_top = CUBE_COLOR_TOP_G
            color_left = CUBE_COLOR_LEFT_G
            color_right = CUBE_COLOR_RIGHT_G
        elif cube_color == "RED" and cube_hover == True:
            color_top = CUBE_COLOR_TOP_R_H
            color_left = CUBE_COLOR_LEFT_R_H
            color_right = CUBE_COLOR_RIGHT_R_H     
        else:
            color_top = CUBE_COLOR_TOP_G_H
            color_left = CUBE_COLOR_LEFT_G_H
            color_right = CUBE_COLOR_RIGHT_G_H

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
        
        if cube_kinged:
            self.draw_crown(surface, cube_x, cube_y + offset_y)

    def draw_crown(self, surface, cube_x, cube_y):
        crown_x = cube_x - CROWN_IMAGE.get_width() // 2
        crown_y = cube_y -2
        surface.blit(CROWN_IMAGE, (crown_x, crown_y))

class Game_logic:
    def check_valid_move(self, mouse_pos, selected_cube_drag):
        if selected_cube_drag is None: #if no cube is selected while mousebuttonup, do nothing.
            return
       
        picked_tile = HITBOX_DETECTION.tile_hitbox(mouse_pos)
        
        if picked_tile is None: #if no tile is selected while mousebuttonup, do nothing (returns cube back to original place).
            move_text = "Out of bounds"
            GAME_COMMUNICATION.move_communication(screen, move_text)
            print(move_text)
            return

        #Unpack the chosen cubes data for gamelogic checks later. 
        cube_ID = CUBE_LIST[selected_cube_drag - 1]["ID"] 
        cube_team = CUBE_LIST[selected_cube_drag - 1]["TEAMCOLOR"]
        cube_kinged = CUBE_LIST[selected_cube_drag - 1]["KINGED"]

        #Unpacks cube coordinates and checks these with all the tiles. That one that matches is the Tile the cube came from.        
        cube_old_coordinates = CUBE_LIST[selected_cube_drag - 1]["COORDINATES"] #unpacking and checking waht the current's cube occupied tile col and row are for valid move logic
        for current_tile in TILE_SET:
            if current_tile["POSITION"] == cube_old_coordinates:# Checks the tile where the cube started at.
                current_tile_ID = current_tile["TILEID"]
                col, row = current_tile["TILE_COL_ROW"] #Column and Row are needed for the valid movement logic.

        #unpacks the picked_tile to check for valid moves. This is the tile where the cube is dropped on!
        picked_tile_ID = picked_tile["TILEID"]#to update the list latern
        picked_tile_coords = picked_tile["POSITION"]#to update the cubes new coordinates
        tile_valid = picked_tile["TILE_VALIDITY"]#to check if the tile is valid for play
        tile_occupied = picked_tile["TILE_IN_USE"]#to check if the tile is occupied
        tile_occupied_by_team = picked_tile["TEAM_COLOR"]#to check which team occupies that tile
        [picked_col, picked_row] = picked_tile["TILE_COL_ROW"]#to check if the tiles column and row are in the allowed ranges of movement. 
         
        if tile_valid is False: # tile is invalid (white) - return to old coordinates
            move_text = "Tile is invalid (White)"
            GAME_COMMUNICATION.move_communication(screen, move_text)
            print(move_text)
            return

        elif tile_occupied is not None: #occupied - return to old coordinates
            move_text = "Tile is already occupied"
            GAME_COMMUNICATION.move_communication(screen, move_text)
            print(move_text)
            return

        elif tile_occupied is None and cube_kinged is False: #normal cube movement when diagonal tiles is empty, only one diagonal forward allowed, None backwards. Based off the tile the cube was picked from.
            allowed_tiles_a, allowed_tiles_b = self.game_rules_movement(col, row, cube_team, cube_kinged)
            
            if (picked_col, picked_row) == allowed_tiles_a or (picked_col,picked_row) == allowed_tiles_b:
                CUBE_LIST[selected_cube_drag - 1]["COORDINATES"] = picked_tile_coords #this updates the coordinates of the cube, ensuring it gets snapped to the new coordinates.

                #if it finds a valid tile to move to, update the TILE-LIST entries to their new values.
                for tile in TILE_SET:
                    if current_tile_ID == tile["TILEID"]: #resets the old tile where the cube was on.
                        tile["TILE_IN_USE"] = None
                        tile["TEAM_COLOR"] = None


                    if picked_tile_ID == tile["TILEID"]: #updates the tile the cube was dropped on with the relevant cube data.
                        tile["TILE_IN_USE"] = cube_ID
                        tile["TEAM_COLOR"] = cube_team











            else:
                print(f"picked_col:{picked_col}, picked_row:{picked_row}")
                print(f"allowed_tiles_a: {allowed_tiles_a}, allowed_tiles_b: {allowed_tiles_b}")
                return

        elif tile_occupied is not None and tile_occupied_by_team != cube_team: #occupied by oppo team how to do attack.. gotta think about this one
            return #implement later
    





    def game_rules_movement(self, col, row, playercolor, kinged):
        if kinged is False: #Ensures that the cube can only move 1 tile diagonally, depending on teamcolor which way
            if playercolor == "RED": #is only allowed downwards
                if col == 0:
                    allowed_tiles_a, allowed_tiles_b = (None, None), (col +1, row +1)
                elif col == 9:
                    allowed_tiles_a, allowed_tiles_b = (col -1, row +1), (None, None)
                else:
                    allowed_tiles_a, allowed_tiles_b = (col -1, row +1), (col +1, row +1)
                return allowed_tiles_a, allowed_tiles_b








            elif playercolor == "GREEN": #is only allowed upwards.
                if col == 0:
                    allowed_tiles_a, allowed_tiles_b = (None, None), (col +1, row -1)
                elif col == 9:
                    allowed_tiles_a, allowed_tiles_b = (col -1, row -1), (None, None)
                else:
                    allowed_tiles_a, allowed_tiles_b = (col -1, row -1), (col +1, row -1)
                return allowed_tiles_a, allowed_tiles_b     


    def opponent_AI():
        pass

class Game_communication:
    def __init__(self):
        self.game_font = pygame.font.Font(None, 24)
        self.antialias = True  
        self.text_color = COLOR_WHITE

    def move_communication(self, surface, move_text): #communicates wether a move is allowed or not, or why not. 
        panel_width = 400
        panel_height = 100
        move_com_surface = pygame.Surface((panel_width, panel_height))
        move_com_surface.fill(COLOR_BLACK)

        move_text_surface = self.game_font.render(move_text, self.antialias, self.text_color)
        move_com_surface.blit(move_text_surface, (5,5))

        surface.blit(move_com_surface, (10, 600))

class Hitbox_detection:
    def cube_hitbox(self, mouse_pos):
        for cube in CUBE_LIST:
            cube_x, cube_y = cube["COORDINATES"]
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
        return False, None

    def tile_hitbox(self, mouse_pos): #USED FOR MOUSE/HOVER AND CUBE PLACEMENT DETECTION!
        for tile in TILE_SET:
            hitbox = tile["VERTICES"]
            if self.hitbox_detection(mouse_pos, hitbox):
                hovered_tile = tile
                self.tile_hover(hovered_tile)
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

class DebugSetting:
    def __init__(self):
        self.debug_font = pygame.font.Font(None, 24)  # Initialize font once
        self.antialias = True  
        self.text_color = COLOR_WHITE

    def debug_panel_tile_info(self, surface, mouse_pos):
        panel_width1 = 300
        panel_height1 = 200
        panel1_surface = pygame.Surface((panel_width1, panel_height1))
        panel1_surface.fill(COLOR_BLACK)

        hovered_tile = HITBOX_DETECTION.tile_hitbox(mouse_pos)
        
        if hovered_tile is not None:  
            tile_id = hovered_tile["TILEID"]
            tile_pos = hovered_tile["POSITION"]
            tile_validity = hovered_tile["TILE_VALIDITY"]
            tile_in_use = hovered_tile["TILE_IN_USE"]
            tile_team = hovered_tile["TEAM_COLOR"]
            tile_col_row = hovered_tile["TILE_COL_ROW"]

            # Create debug information text
            tile_info = (
                f"Tile ID: {tile_id}\n"
                f"Position: {tile_pos}\n"
                f"Valid: {'Yes' if tile_validity else 'No'}\n"
                f"In Use: {tile_in_use if tile_in_use else 'No'}\n"
                f"Team Color: {tile_team if tile_team else 'None'}\n"
                f"Column, Row: {tile_col_row}"
            )

            # Render each line of text
            lines = tile_info.splitlines()
            y_offset = 5
            for line in lines:
                text_surface = self.debug_font.render(line, self.antialias, self.text_color)
                panel1_surface.blit(text_surface, (5, y_offset))
                y_offset += text_surface.get_height() + 5

        # Blit the panel onto the main surface
        surface.blit(panel1_surface, (10, 10))  # Position of debug panel 

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
            
    def debug_draw_board_edges(self, surface, TILE_SET):
        font = pygame.font.Font(None, 32)
        for tile in TILE_SET:
            # Unpack vertices and adjust position as necessary
            if tile["TILEID"] == "A1":
                x, y = tile["VERTICES"][0]  # Top-left
                y -= 25  # Adjust y-coordinate upwards by 25 pixels
            elif tile["TILEID"] == "A10":
                x, y = tile["VERTICES"][1]  # Top-right
                x += 50  # Adjust x-coordinate to the right by 25 pixels
            elif tile["TILEID"] == "J10":
                x, y = tile["VERTICES"][2]  # Bottom-right
                y += 25  # Adjust y-coordinate downwards by 25 pixels
            elif tile["TILEID"] == "J1":
                x, y = tile["VERTICES"][3]  # Bottom-left
                x -= 50  # Adjust x-coordinate to the left by 25 pixels

            # Render the text as stringified coordinates
            text = font.render(f"({x}, {y})", True, COLOR_BLACK)
            
            # Center the text at the adjusted (x, y) position
            text_rect = text.get_rect(center=(x, y))
            surface.blit(text, text_rect)  # Draw text on the given surface

    def debug_buttondown_kinged(self, mouse_pos):
        cube_hit, selected_cube_kinged = HITBOX_DETECTION.cube_hitbox(mouse_pos)
        if cube_hit == False:
            return
        elif cube_hit is True and isinstance(selected_cube_kinged, int):
            is_cube_kinged = CUBE_LIST[selected_cube_kinged -1]["KINGED"]
            if is_cube_kinged:
                CUBE_LIST[selected_cube_kinged -1]["KINGED"] = False
            else:
                CUBE_LIST[selected_cube_kinged -1]["KINGED"] = True


DEBUG_SETTING = DebugSetting()
SETUP_BOARD = Board_setup()
SETUP_CUBES = Draw_cubes()
HITBOX_DETECTION = Hitbox_detection()
GAME_LOGIC = Game_logic()
GAME_COMMUNICATION = Game_communication()

TILE_SET, grid_surface = SETUP_BOARD.setup_iso_grid(GRID_SIZE)
for CUBE_ID in CUBE_LIST:
    for TILE_ID in TILE_SET:
        if CUBE_ID["INIT_TILE_ID"] == TILE_ID["TILEID"]:
            CUBE_ID["COORDINATES"] = TILE_ID["POSITION"]
            TILE_ID["TILE_IN_USE"] = CUBE_ID["ID"]
            TILE_ID["TEAM_COLOR"] = CUBE_ID["TEAMCOLOR"]


running = True
cube_dragging = False
cube_hover = False
selected_cube_drag = None
selected_cube_hover = None
Tile_hover = None

while running:
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if BUTTON_RECT.collidepoint(event.pos):
                DEBUG_MODE = not DEBUG_MODE
                print(f"DEBUG_MODE is now {'ON' if DEBUG_MODE else 'OFF'}")
            else:
                cube_dragging, selected_cube_drag = HITBOX_DETECTION.cube_hitbox(mouse_pos)

        elif event.type == pygame.MOUSEMOTION:
            HITBOX_DETECTION.tile_hitbox(mouse_pos)
            cube_hover, selected_cube_hover = HITBOX_DETECTION.cube_hitbox(mouse_pos)

        elif event.type == pygame.MOUSEBUTTONUP:
            GAME_LOGIC.check_valid_move(mouse_pos, selected_cube_drag)
            dragging_cube = False
            selected_cube_drag = None

                
    screen.fill(BACKGROUND_COLOR)
    screen.blit(screen, (0, 0))
    screen.blit(grid_surface, (0, 0))
    screen.blit(BUTTON_IMAGE, BUTTON_RECT.topleft)

    SETUP_CUBES.draw_cubes(screen, CUBE_LIST, cube_dragging, selected_cube_drag, cube_hover, selected_cube_hover) #currently this redraws all the cubes constantly, while it's only really needed when dragging a cube. Fix this later for better memory usage.

    if DEBUG_MODE:
        DEBUG_SETTING.draw_tileID(screen, TILE_SET)
        DEBUG_SETTING.debug_panel_mouse_pos(screen, mouse_pos)
        DEBUG_SETTING.debug_draw_board_edges(screen, TILE_SET)
        DEBUG_SETTING.debug_panel_tile_info(screen, mouse_pos)

    pygame.display.flip()

pygame.quit()
sys.exit()
