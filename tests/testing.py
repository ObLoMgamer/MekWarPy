import pygame
import pygame_gui
import sys
import os

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
    mech_parts = ['LA', 'RA', 'LT', 'RT', 'CT', 'HD']
    armor_positions = [(screen_width/2 - 120, screen_height/2 - 50), (screen_width/2 + 70, screen_height/2 - 50),
                       (screen_width/2 - 50, screen_height/2 - 100), (screen_width/2 + 50, screen_height/2 - 100),
                       (screen_width/2, screen_height/2), (screen_width/2 - 25, screen_height/2 - 130)]

    for part, position in zip(mech_parts, armor_positions):
        armor_value = mech.armor_distribution.get(f'{part} Armor', 0)
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

pygame.init()

pygame.display.set_caption('MekWarPy Client')
window_surface = pygame.display.set_mode((800, 600))

background = pygame.Surface((800, 600))
background.fill(pygame.Color('#000000'))

manager = pygame_gui.UIManager((800, 600))

#connect to server


hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 275), (100, 50)),
                                            text='Say Hello',
                                            manager=manager)

# Add the root directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.core.Unit import *
import zipfile

mechfile = '3039u/Highlander HGN-733.mtf'

loadedMech = Mech()
loadedMech.zipload(mechfile)


clock = pygame.time.Clock()
is_running = True

draw_mech(loadedMech)

while is_running:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == hello_button:
                print('Hello World!')

        manager.process_events(event)

    manager.update(time_delta)

    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)

    pygame.display.update()