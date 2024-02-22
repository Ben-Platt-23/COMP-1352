"""
    Description of program
    Filename: platt_sandgame_part1.py
    Author: Ben Platt
    Date: 2/20/24
    Course: COMP-1352
    Assignment: Sandgame Part 1
    Collaborators: N/A
    Internet Source: W3Schools
"""




import dudraw  # Import the dudraw module for drawing

import time  # Import the time module for time-related functions

import random  # Import the random module for generating random numbers

# Constants
EMPTY = 0  # Constant representing an empty space
SAND = 1   # Constant representing sand particle
FLOOR = 2  # Constant representing floor particle

# Function to create and initialize the sand world
def create_world(rows, cols):
    world = [[EMPTY for _ in range(cols)] for _ in range(rows)]  # Create a 2D array to represent the world
    # Set the bottom row as the floor
    for x in range(cols):
        dudraw.set_pen_color(dudraw.BLACK)  # Set the pen color to black
        place_floor(world, x, rows - 1)  # Place floor particles
    return world

# Function to draw the world
def draw_world(world):
    # Clear canvas
    dudraw.clear()
    # Draw each particle
    for y in range(len(world)):
        for x in range(len(world[0])):
            if world[y][x] == SAND:
                dudraw.filled_square(x, y, 5)  # Draw sand particle
            elif world[y][x] == FLOOR:
                dudraw.filled_square(x, y, 5)  # Draw floor particle

# Function to update a pixel
def update_pixel(x, y):
    dudraw.filled_square(x, y, 5)  # Update canvas with filled square

# Function to place sand particle
def place_sand(world, x, y):
    if world[y][x] == EMPTY:
        world[y][x] = SAND  # Place sand particle
        dudraw.set_pen_color(dudraw.YELLOW)  # Set pen color to yellow
        dudraw.filled_square(x, y, 5)  # Update canvas with yellow sand particle

# Function to place floor particle
def place_floor(world, x, y):
    bottom_row_index = len(world) - 506  # Calculate the bottom row index
    if y == bottom_row_index:  # Check if it's the bottom row
        if world[y][x] == EMPTY:
            world[y][x] = FLOOR  # Place floor particle
            update_pixel(x, y)  # Update canvas
        elif world[y][x] == SAND:
            world[y - 1][x] = FLOOR  # Place floor particle above sand
            update_pixel(x, y - 1)  # Update canvas

# Function to simulate sand falling and stacking
def simulate_sand_fall(world):
    for y in range(1, len(world)):
        for x in range(len(world[0])):
            if world[y][x] == SAND:
                # Check if there's empty space below
                if world[y - 1][x] == EMPTY:
                    # Move the sand particle down
                    world[y - 1][x] = SAND
                    world[y][x] = EMPTY
                elif world[y - 1][x] == FLOOR:
                    # Stack the sand particle on the floor
                    world[y][x] = EMPTY

# Main function
def main():
    # Initialization
    dudraw.set_canvas_size(512, 512)  # Set canvas size
    dudraw.set_scale(0, 512)  # Set scale
    world = create_world(512, 512)  # Create sand world
    draw_world(world)  # Draw initial world

    # Set pen color to yellow before the animation loop
    dudraw.set_pen_color(dudraw.YELLOW)
    
    # Animation loop
    running = True
    while running:
        # Check for mouse press
        if dudraw.mouse_is_pressed():
            # Check mouse position and convert to canvas coordinates
            mx = int(dudraw.mouse_x())
            my = int(dudraw.mouse_y())

            # Sprinkle sand from random locations near the mouse position
            sand_spawned = False  # Flag to indicate if sand has been spawned during this iteration
            for _ in range(5):  # Adjust the number of particles as needed
                px = mx + random.randint(-5, 5)
                py = my + random.randint(-5, 5)
                place_sand(world, px, py)
                sand_spawned = True
        simulate_sand_fall(world)  # Simulate sand falling and stacking
        draw_world(world)  # Draw the updated world
 
        # Process key presses
        keys = dudraw.keys_pressed()
        if 'q' in keys:
            running = False  # Set running to False to exit the loop

        # Update the canvas
        dudraw.show()

        # Delay to control animation speed
        time.sleep(0.05)

# Entry point
if __name__ == "__main__":
    main()
