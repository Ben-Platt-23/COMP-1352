"""
    Description of program
    Filename: lab_11.py
    Author: Ben Platt
    Date: 2/19/24
    Course: COMP-1352
    Assignment: Lab 11
    Collaborators: N/A
    Internet Source: W3Schools
"""

from random import randint, random
import dudraw
import time

####### Bouncing Shape ###############
class BouncingShape:
    def __init__(self, x: float = random(), y: float = random(), xv: float = random()*0.06 - 0.03, yv: float = random()*0.06 - 0.03, s: float = 0.04):
        # Constructor initializes position, velocity, size, and color
        self.x_pos = x
        self.y_pos = y
        self.x_vel = xv
        self.y_vel = yv
        self.size = s
        self.color = (randint(0, 255), randint(0, 255), randint(0, 255))  # Tuple representing RGB color values

    def move(self):
        # Move the shape according to its velocity
        self.x_pos += self.x_vel
        self.y_pos += self.y_vel 
        
        # Check for collisions with the canvas edges and change direction if necessary
        if ((self.x_pos + self.size > 1 and self.x_vel > 0) or 
            (self.x_pos - self.size < 0 and self.x_vel < 0)):
            self.x_vel *= -1

        if ((self.y_pos + self.size > 1 and self.y_vel > 0) or
            (self.y_pos - self.size < 0 and self.y_vel < 0)):
            self.y_vel *= -1  

    def draw(self):
        # This method will be overridden by subclasses
        pass

class BouncingCircle(BouncingShape):
    def __init__(self, x: float = random(), y: float = random(), xv: float = random()*0.06 - 0.03, yv: float = random()*0.06 - 0.03, s: float = 0.04):
        # Constructor for BouncingCircle, sets the color to blue
        super().__init__(x, y, xv, yv, s)
        self.color = dudraw.BLUE  # Blue color for circle

    def draw(self):
        # Draw a circle with current position, size, and color
        dudraw.set_pen_color(self.color)  # Set the pen color
        dudraw.circle(self.x_pos, self.y_pos, self.size)

class WobblyCircle(BouncingCircle):
    def __init__(self, x: float = random(), y: float = random(), xv: float = random()*0.06 - 0.03, yv: float = random()*0.06 - 0.03, s: float = 0.04):
        # Constructor for WobblyCircle, sets the color to red
        super().__init__(x, y, xv, yv, s)
        self.color = dudraw.RED  # Red color for circle

    def move(self):
        # Move the circle and add a random perturbation to its position
        super().move()
        self.x_pos += random() * 0.04 - 0.02
        self.y_pos += random() * 0.04 - 0.02

class PatrollingSquare(BouncingShape):
    def __init__(self, x: float = random(), y: float = random(), xv: float = random()*0.06 - 0.03, yv: float = random()*0.06 - 0.03, s: float = 0.04):
        # Constructor for PatrollingSquare, sets the color to green and initializes step_count
        super().__init__(x, y, xv, yv, s)
        self.color = dudraw.GREEN  # Green color for square
        self.step_count = 0

    def draw(self):
        # Draw a square with current position, size, and color
        dudraw.set_pen_color(self.color)  # Set the pen color
        dudraw.square(self.x_pos, self.y_pos, self.size)

    def move(self):
        # Move the square and change velocity and reset step_count after every 10 steps
        super().move()
        self.step_count += 1
        if self.step_count >= 10:
            self.step_count = 0
            self.x_vel = random() * 0.06 - 0.03
            self.y_vel = random() * 0.06 - 0.03

def main():
    # Set the canvas size
    dudraw.set_canvas_size(600, 600)
    
    # Create instances of bouncing objects
    bouncing_objects = [
        BouncingCircle(),
        WobblyCircle(),
        PatrollingSquare()
    ]

    # Animation loop
    while True:
        dudraw.clear()
        for obj in bouncing_objects:
            obj.move()
            obj.draw()
        dudraw.show()
        time.sleep(0.02)  # Adjust the speed of animation here

if __name__ == "__main__":
    main()
