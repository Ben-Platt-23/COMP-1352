"""
    Description of program
    Filename: platt_project_6.py
    Author: Ben Platt
    Date: 3/21/24
    Course: COMP-1352
    Assignment: Project 6
    Collaborators: N/A
    Internet Source: W3Schools
"""

import math
import random
import time
import dudraw

class Vector:
    def __init__(self, some_x=0, some_y=0):
        """
        Initialize a 2D vector with given x and y components.
        
        Args:
            some_x (float): x component of the vector. Default is 0.
            some_y (float): y component of the vector. Default is 0.
        """
        self.x = some_x
        self.y = some_y

    def limit(self, l):
        """
        Limit the magnitude of the vector to a given value.

        Args:
            l (float): Limit value for the magnitude of the vector.
        """
        if self.length() >= l:
            self.resize(l)

    def resize(self, l):
        """
        Resize the vector to a specified magnitude.

        Args:
            l (float): New magnitude for the vector.
        """
        length = math.sqrt(self.x ** 2 + self.y ** 2)
        self.x *= (l / length)
        self.y *= (l / length)

    def __add__(self, other_vector):
        """
        Overloaded addition operator for vector addition.

        Args:
            other_vector (Vector): Another Vector instance to add.

        Returns:
            Vector: Resultant vector after addition.
        """
        return Vector(self.x + other_vector.x, self.y + other_vector.y)

    def __sub__(self, other_vector):
        """
        Overloaded subtraction operator for vector subtraction.

        Args:
            other_vector (Vector): Another Vector instance to subtract.

        Returns:
            Vector: Resultant vector after subtraction.
        """
        return Vector(self.x - other_vector.x, self.y - other_vector.y)

    def __isub__(self, other_vector):
        """
        Overloaded in-place subtraction operator for vector subtraction.

        Args:
            other_vector (Vector): Another Vector instance to subtract in-place.

        Returns:
            Vector: Reference to self after subtraction.
        """
        self.x -= other_vector.x
        self.y -= other_vector.y
        return self

    def __iadd__(self, other_vector):
        """
        Overloaded in-place addition operator for vector addition.

        Args:
            other_vector (Vector): Another Vector instance to add in-place.

        Returns:
            Vector: Reference to self after addition.
        """
        self.x += other_vector.x
        self.y += other_vector.y
        return self

    def divide(self, s):
        """
        Divide the vector components by a scalar value.

        Args:
            s (float): Scalar value to divide the vector components by.
        """
        self.x /= s
        self.y /= s

    def length(self):
        """
        Calculate the magnitude (length) of the vector.

        Returns:
            float: Magnitude (length) of the vector.
        """
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def angle_in_radians(self):
        """
        Calculate the angle of the vector in radians.

        Returns:
            float: Angle of the vector in radians.
        """
        return math.atan2(self.y, self.x)

class Time:
    frame = 0

    @staticmethod
    def tick():
        """
        Increment the frame counter by 1.
        """
        Time.frame += 1
    
    @staticmethod
    def time():
        """
        Get the current frame count.

        Returns:
            int: Current frame count.
        """
        return Time.frame

class Particle:
    def __init__(self, x_pos=0, y_pos=0, x_vel=0, y_vel=0, x_acc=0, size=0, lifetime=0):
        """
        Initialize a particle with given parameters.

        Args:
            x_pos (float): Initial x position of the particle. Default is 0.
            y_pos (float): Initial y position of the particle. Default is 0.
            x_vel (float): Initial x velocity of the particle. Default is 0.
            y_vel (float): Initial y velocity of the particle. Default is 0.
            x_acc (float): Initial x acceleration of the particle. Default is 0.
            size (float): Size of the particle. Default is 0.
            lifetime (int): Lifetime of the particle. Default is 0.
        """
        self.position = Vector(x_pos, y_pos)
        self.velocity = Vector(x_vel, y_vel)
        self.acceleration = Vector(x_acc, 0)
        self.size = size
        self.lifetime = lifetime

    def move(self):
        """
        Update the position and velocity of the particle based on its acceleration.
        """
        self.position += self.velocity
        self.velocity += self.acceleration

    def draw(self):
        """
        Placeholder method for drawing the particle.
        """
        pass

class AcceleratingParticle(Particle):
    def __init__(self, x_pos=0, y_pos=0, x_vel=0, y_vel=0, x_acc=0, size=0, lifetime=0):
        """
        Initialize an accelerating particle with given parameters.
        Inherits from Particle class.

        Args:
            x_pos (float): Initial x position of the particle. Default is 0.
            y_pos (float): Initial y position of the particle. Default is 0.
            x_vel (float): Initial x velocity of the particle. Default is 0.
            y_vel (float): Initial y velocity of the particle. Default is 0.
            x_acc (float): Initial x acceleration of the particle. Default is 0.
            size (float): Size of the particle. Default is 0.
            lifetime (int): Lifetime of the particle. Default is 0.
        """
        super().__init__(x_pos, y_pos, x_vel, y_vel, x_acc, size, lifetime)
        self.acceleration = Vector(x_acc, 0)

    def move(self):
        """
        Update the position and velocity of the particle based on its acceleration.
        """
        self.position += self.velocity
        self.velocity += self.acceleration

class FireworkParticle(AcceleratingParticle):
    def draw(self):
        """
        Draw a filled square representing the firework particle.
        """
        dudraw.filled_square(self.position.x, self.position.y, self.size)

class MarbleParticle(AcceleratingParticle):
    def draw(self):
        """
        Draw a filled circle representing the marble particle.
        """
        dudraw.filled_circle(self.position.x, self.position.y, self.size)

class SparkParticle(Particle):
    def __init__(self, x_pos=0, y_pos=0, x_vel=0, y_vel=0, x_acc=0, size=0, lifetime=0):
        """
        Initialize a spark particle with given parameters.
        Inherits from Particle class.

        Args:
            x_pos (float): Initial x position of the particle. Default is 0.
            y_pos (float): Initial y position of the particle. Default is 0.
            x_vel (float): Initial x velocity of the particle. Default is 0.
            y_vel (float): Initial y velocity of the particle. Default is 0.
            x_acc (float): Initial x acceleration of the particle. Default is 0.
            size (float): Size of the particle. Default is 0.
            lifetime (int): Lifetime of the particle. Default is 0.
        """
        super().__init__(x_pos, y_pos, x_vel, y_vel, x_acc, size, lifetime)

    def draw(self):
        """
        Draw a line representing the spark particle.
        """
        dudraw.line(self.position.x, self.position.y, self.position.x + self.velocity.x, self.position.y + self.velocity.y)

class FireParticle(AcceleratingParticle):
    def __init__(self, x_pos=0, y_pos=0, x_vel=0, y_vel=0, x_acc=0, size=0, lifetime=0):
        """
        Initialize a fire particle with given parameters.
        Inherits from AcceleratingParticle class.

        Args:
            x_pos (float): Initial x position of the particle. Default is 0.
            y_pos (float): Initial y position of the particle. Default is 0.
            x_vel (float): Initial x velocity of the particle. Default is 0.
            y_vel (float): Initial y velocity of the particle. Default is 0.
            x_acc (float): Initial x acceleration of the particle. Default is 0.
            size (float): Size of the particle. Default is 0.
            lifetime (int): Lifetime of the particle. Default is 0.
        """
        super().__init__(x_pos, y_pos, x_vel, y_vel, x_acc, size, lifetime)
        # Set random color for the fire particle
        self.color = dudraw.set_pen_color_rgb(r=random.randint(0, 255), g=random.randint(0, 255), b=random.randint(0, 255))

    def draw(self):
        """
        Draw a filled circle representing the fire particle with random color.
        """
        # Set random color for the fire particle
        self.color = dudraw.set_pen_color_rgb(r=random.randint(0, 255), g=random.randint(0, 255), b=random.randint(0, 255))
        dudraw.filled_circle(self.position.x, self.position.y, self.size)

class ParticleContainer:
    def __init__(self, x_pos=0, y_pos=0):
        """
        Initialize a container for particles with a specified position.

        Args:
            x_pos (float): Initial x position of the container. Default is 0.
            y_pos (float): Initial y position of the container. Default is 0.
        """
        self.position = Vector(x_pos, y_pos)
        self.particles = []

    def animate(self):
        """
        Animate particles within the container by moving them and then drawing them.
        """
        for particle in self.particles:
            particle.move()
            particle.draw()

class Emitter(ParticleContainer):
    def __init__(self, x_pos=0, y_pos=0, fire_rate=0):
        """
        Initialize an emitter with a specified position and fire rate.
        Inherits from ParticleContainer class.

        Args:
            x_pos (float): Initial x position of the emitter. Default is 0.
            y_pos (float): Initial y position of the emitter. Default is 0.
            fire_rate (int): Rate at which particles are emitted. Default is 0.
        """
        super().__init__(x_pos, y_pos)
        self.fire_rate = fire_rate

class Fire(Emitter):
    def animate(self):
        """
        Animate the fire emitter by emitting fire particles and then animating them.
        """
        super().animate()
        for _ in range(self.fire_rate):
            fire_particle = FireParticle(self.position.x, self.position.y,
                                         random.uniform(-0.002, 0.002), random.uniform(0.002, 0.005),
                                         0, random.uniform(0.01, 0.03), 50)
            self.particles.append(fire_particle)

class Sparkler(Emitter):
    def animate(self):
        """
        Animate the sparkler emitter by emitting spark particles and then animating them.
        """
        super().animate()
        for _ in range(self.fire_rate):
            spark_particle = SparkParticle(self.position.x, self.position.y,
                                           random.uniform(-0.07, 0.07), random.uniform(-0.07, 0.07),
                                           0, 0.04, 5)
            self.particles.append(spark_particle)

class Firework(Emitter):
    def __init__(self, x_pos=0, y_pos=0, fire_rate=0):
        """
        Initialize a firework emitter with a specified position and fire rate.
        Inherits from Emitter class.

        Args:
            x_pos (float): Initial x position of the firework emitter. Default is 0.
            y_pos (float): Initial y position of the firework emitter. Default is 0.
            fire_rate (int): Rate at which particles are emitted. Default is 0.
        """
        super().__init__(x_pos, y_pos, fire_rate)
        # Initialize fireworks particles
        for _ in range(500):
            firework_particle = FireworkParticle(self.position.x, self.position.y,
                                                 random.uniform(-0.04, 0.04), random.uniform(-0.04, 0.04),
                                                 0, 0, random.uniform(-0.008, -0.012), 0.004, 50)
            self.particles.append(firework_particle)

    def animate(self):
    """
    Animate the interactions between fireworks particles within the container.
    """
    super().animate()  # Call the animate method of the parent class to move and draw particles
    for firework in self.particles:  # Iterate through each firework particle
        for other_firework in self.particles:  # Iterate through each other firework particle
            if firework != other_firework:  # Check if the particles are not the same
                # Calculate the distance between the particles
                dist = math.sqrt((firework.position.x - other_firework.position.x) ** 2 +
                                 (firework.position.y - other_firework.position.y) ** 2)
                # Check if the particles are colliding based on their sizes
                if dist < (firework.size + other_firework.size):
                    # Calculate collision normal vector
                    normal = firework.position - other_firework.position
                    normal.resize(1)  # Normalize the normal vector
                    # Calculate tangential vector
                    tangential = Vector(-normal.y, normal.x)
                    # Calculate masses and velocities
                    m1 = firework.velocity.length()
                    m2 = other_firework.velocity.length()
                    u1 = firework.velocity * normal
                    u2 = other_firework.velocity * normal
                    # Calculate final velocities after collision using 1-dimensional collision equations
                    v1 = (u1 * (m1 - m2) + 2 * m2 * u2) / (m1 + m2)
                    v2 = (u2 * (m2 - m1) + 2 * m1 * u1) / (m1 + m2)
                    # Update velocities of particles after collision
                    firework.velocity += (normal * (v1 - u1))
                    other_firework.velocity += (normal * (v2 - u2))

def main():
    # Create a dudraw object
    canvas = dudraw.set_canvas_size(500, 500)
    dudraw.set_scale(0, 100)

    # Create particle systems
    fire = Fire(0, 0, 10)  # Create a fire particle system at position (0, 0) with a fire rate of 10
    sparkler = Sparkler(0, 0, 50)  # Create a sparkler particle system at position (0, 0) with a fire rate of 50
    fireworks = []  # Create an empty list to store fireworks

    # Create fireworks
    for _ in range(5):
        # Create 5 fireworks particles at random positions and add them to the list
        fireworks.append(Firework(random.uniform(-1, 1), random.uniform(-1, 1), 1))

    # Animation loop
    while True:
        # Clear canvas
        canvas.clear()

        # Animate particle systems
        fire.animate()  # Animate the fire particle system
        sparkler.animate()  # Animate the sparkler particle system
        for firework in fireworks:
            firework.animate()  # Animate each firework particle

        # Update canvas
        canvas.show()  # Show the updated canvas
        time.sleep(0.03)  # Pause for a short time to control the animation speed

# Call the main function to start the animation
if __name__ == "__main__":
    main()
