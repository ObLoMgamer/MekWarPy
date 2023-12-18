import pygame
import pygame_gui
import sys
import os
import zipfile
# Add the root directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.core.Unit import *


class Client:
    def __init__(self):
        pygame.init()

        self.window_surface = pygame.display.set_mode((800, 600))
        self.background = pygame.Surface((800, 600))
        self.background.fill(pygame.Color('#000000'))
        self.manager = pygame_gui.UIManager((800, 600))

        self.clock = pygame.time.Clock()
        self.is_running = True

        #draw base UI elements
        self.draw_mech_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 275), (100, 50)),
                                            text='Say Hello',
                                            manager=self.manager)

    def draw_mech(self, mech):
        # Draw the Mech representation, including armor, internal structure, and equipment locations
        

        # Screen dimensions and basic Mech shape dimensions
        screen_width, screen_height = 800, 600
        body_rect = pygame.Rect(screen_width/2 - 50, screen_height/2 - 100, 100, 200)
        left_arm_rect = pygame.Rect(screen_width/2 - 100, screen_height/2 - 50, 50, 100)
        right_arm_rect = pygame.Rect(screen_width/2 + 50, screen_height/2 - 50, 50, 100)
        head_rect = pygame.Rect(screen_width/2 - 25, screen_height/2 - 130, 50, 30)

        # Draw Mech parts
        pygame.draw.rect(self.background, pygame.Color('#FFFFFF'), body_rect)
        pygame.draw.rect(self.background, pygame.Color('#FFFFFF'), left_arm_rect)
        pygame.draw.rect(self.background, pygame.Color('#FFFFFF'), right_arm_rect)
        pygame.draw.rect(self.background, pygame.Color('#FFFFFF'), head_rect)

        # Font for text
        font = pygame.font.Font(None, 24)

        # Display armor and internal structure values
        mech_parts = ['LA Armor', 'RA Armor', 'LT Armor', 'RT Armor', 'CT armor', 'HD Armor', 'RLT Armor', 'RTR Armor', 'CTR Armor']
        armor_positions = [(screen_width/2 - 120, screen_height/2 - 50), (screen_width/2 + 70, screen_height/2 - 50),
                           (screen_width/2 - 50, screen_height/2 - 100), (screen_width/2 + 50, screen_height/2 - 100),
                           (screen_width/2, screen_height/2), (screen_width/2 - 25, screen_height/2 - 130)]

        for part, position in zip(mech_parts, armor_positions):
            armor_value = mech.armor_distribution.get(f'{part}', 0)
            structure_value = mech.internal_structure.get(part, 0)
            text = f"A:{armor_value} S:{structure_value}"
            text_surface = font.render(text, True, pygame.Color('#FFFF00'))
            self.background.blit(text_surface, position)

        # Display equipment and location
        y_offset = 400
        for location, equipment in mech.critical_slots.items():
            location_text = f"{location}: " + ", ".join(equipment)
            text_surface = font.render(location_text, True, pygame.Color('#FFFFFF'))
            self.background.blit(text_surface, (20, y_offset))
            y_offset += 30

        # Add more drawing logic and interactivity as needed

    def run(self):

        sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

        mechfile = '3039u/Highlander HGN-733.mtf'

        loadedMech = Mech()
        loadedMech.zipload(mechfile)

        while self.is_running:
            time_delta = self.clock.tick(60)/1000.0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False

                if event.type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == self.draw_mech_button:
                        self.draw_mech(loadedMech)  # Call the draw_mech function here

                self.manager.process_events(event)

            self.manager.update(time_delta)

            self.window_surface.blit(self.background, (0, 0))


            self.manager.draw_ui(self.window_surface)

            pygame.display.update()


# Create the game instance with the Mech object
game = Client()

# Run the game loop
game.run()
