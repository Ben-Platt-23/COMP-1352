from random import random
import dudraw
from dudraw import Color

class Dancer:
    def __init__(self, x=0.5, y=0.5, target_x=0.5, target_y=0.5, size=0.03, color=None):
        self.x_position = x
        self.y_position = y
        self.target_x = target_x
        self.target_y = target_y
        self.size = size
        self.color = color if color else Color(int(256*random()), int(256*random()), int(256*random()))

    def __str__(self):
        return f'Dancer at ({self.x_position}, {self.y_position}), Size: {self.size}, Color: {self.color}'

    def draw(self):
        dudraw.set_pen_color(self.color)
        dudraw.filled_circle(self.x_position, self.y_position, self.size)

    def move(self):
        # Move 5% towards the target
        self.x_position += 0.05 * (self.target_x - self.x_position)
        self.y_position += 0.05 * (self.target_y - self.y_position)

    def set_target(self, target_x, target_y):
        self.target_x = target_x
        self.target_y = target_y

# Main code block
dudraw.set_canvas_size(400, 400)
dancers = [Dancer(random(), random(), random(), random(), 0.03) for _ in range(5)]

key = ''
while key != 'q':
    # Move dancers
    for i in range(len(dancers)):
        dancers[i].move()

    # Update targets
    for i in range(len(dancers) - 1, 0, -1):
        dancers[i].set_target(dancers[i - 1].x_position, dancers[i - 1].y_position)

    # Update target of the first dancer to the mouse position
    mouse_x, mouse_y = dudraw.mouse_x(), dudraw.mouse_y()
    dancers[0].set_target(mouse_x, mouse_y)

    # Draw the frame
    dudraw.clear(dudraw.LIGHT_GRAY)
    for dancer in dancers:
        dancer.draw()

    # Detect key presses
    key = dudraw.next_key()

    # Create a new dancer when 'n' is pressed
    if key == 'n':
        new_dancer = Dancer(random(), random(), random(), random(), 0.03)
        dancers.append(new_dancer)

    # Display the new frame and pause for 1/20 of a second
    dudraw.show(50)

# Cleanup
dudraw.close()