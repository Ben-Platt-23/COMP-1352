"""
 Filename: bouncing_circle.py
 Author: Ben Platt
 Date: January 2023
 Course: COMP 1352
 Assignment: animation demo, to be modified to use classes
 Collaborators: None
 Internet Source: None
"""




from random import random
import dudraw
from dudraw import Color

# Define the BouncingCircle class
class BouncingCircle:
    def __init__(self, x_position, y_position, x_velocity, y_velocity, radius):
        self.x_position = x_position
        self.y_position = y_position
        self.x_velocity = x_velocity
        self.y_velocity = y_velocity
        self.radius = radius
        self.color = Color(int(random() * 256), int(random() * 256), int(random() * 256))
        self.is_moving = True

    def move(self):
        if self.is_moving:
            self.x_position += self.x_velocity
            self.y_position += self.y_velocity

            # Bounce off the edges of the canvas if necessary
            if (self.x_position > 1 - self.radius and self.x_velocity > 0 or
                    self.x_position < self.radius and self.x_velocity < 0):
                self.x_velocity *= -1

            if (self.y_position > 1 - self.radius and self.y_velocity > 0 or
                    self.y_position < self.radius and self.y_velocity < 0):
                self.y_velocity *= -1

    def draw(self):
        dudraw.set_pen_color(self.color)
        dudraw.filled_circle(self.x_position, self.y_position, self.radius)
        dudraw.set_pen_color(dudraw.BLACK)
        dudraw.circle(self.x_position, self.y_position, self.radius)

    def overlaps(self, other: BouncingCircle) -> bool:
        distance_squared = (self.x_position - other.x_position) ** 2 + (self.y_position - other.y_position) ** 2
        combined_radii_squared = (self.radius + other.radius) ** 2
        return distance_squared < combined_radii_squared

    def start(self):
        self.is_moving = True

    def stop(self):
        self.is_moving = False

# Set up the canvas
dudraw.set_canvas_size(400, 400)

# Create two bouncing circles
circle1 = BouncingCircle(random(), random(), 0.05 * random(), 0.05 * random(), 0.05)
circle2 = BouncingCircle(random(), random(), 0.05 * random(), 0.05 * random(), 0.05)

# Main animation loop
key = ''
while key != 'q':
    circle1.move()
    circle2.move()

    # Check for overlap and display "Crash!" if circles overlap
    if circle1.overlaps(circle2):
        dudraw.text("Crash!", 0.5, 0.5, size=20, color=dudraw.RED)

    dudraw.clear(dudraw.LIGHT_GRAY)

    # Draw the circles at their new positions
    circle1.draw()
    circle2.draw()

    key = dudraw.next_key()

    # Display the new frame and pause for 1/20 of a second
    dudraw.show(50)