import sys
import pygame as py
from vector import Vector
from gm import GameManager
from enemy import Enemy
import pygame_gui
py.init()

# Window
size = width, height = 640, 480

# RGBA constants
blue = 0, 0, 225, 0
color = 100, 50, 20, 10
paddle_color = 0, 0, 0
gloria_position: Vector = Vector(50, 200)
gloria: Enemy = Enemy(gloria_position, paddle_color, 8.0)
fish_list: list[Enemy] = []
FRAMES = 60
# Makes Screen
screen = py.display.set_mode(size)

# Game clock
clock = py.time.Clock()

# Keeps game loop running
playing = True

# Handles GUI
manager = pygame_gui.UIManager((width, height))

# UI Elements for GUI
fish_total = pygame_gui.elements.UILabel(relative_rect=py.Rect((420, 40), (200, 50)),
        text='Fish: ' + str(len(fish_list)),
                manager=manager) 

# Game Loop
while playing:
    # Games internal clock, sets number of frames run per second
    clock.tick(FRAMES)
    pos = py.mouse.get_pos()

    # Tracks player interaction
    for event in py.event.get():
        if event.type == py.QUIT: sys.exit()
        # Places fighter if game manager agrees
        if event.type == py.MOUSEBUTTONUP:
            fish_list.append(Enemy(Vector(pos[0], pos[1]), paddle_color, 5.0))


    screen.fill(blue)

    for gloria in fish_list:
        py.draw.circle(screen, paddle_color, (gloria.position.x, gloria.position.y), 20)
        gloria.move_fish((Vector(pos[0] + 1, pos[1] + 1)))
    # GUI Updates
    fish_total.set_text("Fish: " + str(len(fish_list)))
    manager.process_events(event)
    manager.update(20)
    manager.draw_ui(screen)

    # Flips all the updates from the loop onto screen
    py.display.update()