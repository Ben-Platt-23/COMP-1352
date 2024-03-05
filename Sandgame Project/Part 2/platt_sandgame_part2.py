"""
    Description of program
    Filename: platt_sandgame_part2.py
    Author: Ben Platt
    Date: 3/1/24
    Course: COMP-1352
    Assignment: Sandgame Part 2
    Collaborators: N/A
    Internet Source: W3Schools
"""



import dudraw
import time
import random

# Constants
EMPTY = 0  # Constant representing an empty space
SAND = 1   # Constant representing sand particle
FLOOR = 2  # Constant representing floor particle
RAIN = 3   # Constant representing raindrop

# Global variable to track the current mode
current_mode = SAND  # Start with sand mode initially

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
    # Display current mode on the canvas
    if current_mode == SAND:
        dudraw.set_pen_color(dudraw.BLACK)  # Set text color to black
        dudraw.text(10, 10, "Mode: Sand")  # Draw text for sand mode
    elif current_mode == FLOOR:
        dudraw.set_pen_color(dudraw.BLACK)  # Set text color to black
        dudraw.text(10, 10, "Mode: Floor")  # Draw text for floor mode

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
    if world[y][x] == EMPTY:
        world[y][x] = FLOOR  # Place floor particle
        dudraw.set_pen_color(dudraw.BLACK)  # Set pen color to black
        dudraw.filled_square(x, y, 5)  # Update canvas with black floor particle

# Function to place raindrop
def place_rain(world, x, y):
    if world[y][x] == EMPTY:
        world[y][x] = RAIN  # Place raindrop
        dudraw.set_pen_color(dudraw.BLUE)  # Set pen color to blue
        dudraw.filled_square(x, y, 2)  # Update canvas with blue raindrop

# Function to simulate rain falling
def simulate_rain(world):
    for x in range(len(world[0])):
        if random.random() < 0.35:  # Adjust the probability to control rain intensity
            place_rain(world, x, 0)  # Place raindrop at the top edge

# Function to simulate sand falling and stacking
def simulate_rain_fall(world):
    for y in range(len(world) - 1, 0, -1):
        for x in range(len(world[0])):
            if world[y][x] == RAIN and world[y + 1][x] == EMPTY:
                world[y + 1][x] = RAIN  # Move raindrop down
                world[y][x] = EMPTY  # Clear current position 

# Function to simulate sand falling and stacking
def simulate_sand_fall(world):
    for y in range(1, len(world)):
        for x in range(len(world[0])):
            if world[y][x] == SAND:
                # Check if there's empty space below or if it's above a floor particle
                if world[y - 1][x] == EMPTY:
                    # Move the sand particle down
                    world[y - 1][x] = SAND
                    world[y][x] = EMPTY
                elif world[y - 1][x] == FLOOR:
                    # Leave the sand particle in its current position
                    world[y][x] = SAND
                    # Check if there's enough space to flow horizontally to the left
                    for i in range(1, 4):  # Increase the range for more aggressive flow
                        if x - i >= 0 and world[y][x - i] == EMPTY:
                            # Flow sand to the left
                            world[y][x - i] = SAND
                            world[y][x] = EMPTY
                        else:
                            break
                    # Check if there's enough space to flow horizontally to the right
                    for i in range(1, 4):  # Increase the range for more aggressive flow
                        if x + i < len(world[0]) and world[y][x + i] == EMPTY:
                            # Flow sand to the right
                            world[y][x + i] = SAND
                            world[y][x] = EMPTY
                        else:
                            break


# Function to handle key press events
def handle_key_press(key):
    global current_mode
    if key == 'f':
        current_mode = FLOOR  # Switch to floor mode
    elif key == 's':
        current_mode = SAND  # Switch to sand mode

# Main function
def main():
    # Initialization
    dudraw.set_canvas_size(512, 512)  # Set canvas size
    dudraw.set_scale(0, 512)  # Set scale
    world = create_world(512, 512)  # Create sand world

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
                if current_mode == SAND:
                    place_sand(world, px, py)
                elif current_mode == FLOOR:
                    place_floor(world, px, py)
                sand_spawned = True
        simulate_sand_fall(world)  # Simulate sand falling and stacking
        simulate_rain(world)
        simulate_rain_fall(world)
        draw_world(world)  # Draw the updated world

        # Process key presses
        keys = dudraw.keys_pressed()
        for key in keys:
            if key == 'q':
                running = False  # Set running to False to exit the loop
            else:
                handle_key_press(key)

        # Update the canvas
        dudraw.show()

        # Delay to control animation speed
        time.sleep(0.05)

# Entry point
if __name__ == "__main__":
    main()

