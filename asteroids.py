import math
import random
import settings


class Asteroids():

    def __init__(self, root):
        self.MIN_SIZE = settings.min_size
        self.MAX_SIZE = settings.max_size
        self.MIN_SPEED = settings.min_speed
        self.MAX_SPEED = settings.max_speed
        self.MAX_ASTEROIDS = settings.max_asteroids

        self.x_coords = []
        self.y_coords = []
        self.asteroid_sizes = []
        self.asteroid_speeds = []
        self.asteroid_direction_angles = []

        self.fill()

    def fill(self):
        while len(self.x_coords) != self.MAX_ASTEROIDS:
            self.y_coords.append('x')
            self.x_coords.append('x')
            self.asteroid_sizes.append('x')
            self.asteroid_speeds.append('x')
            self.asteroid_direction_angles.append('x')

    def borders(self):
        i = 0
        while i < self.MAX_ASTEROIDS:
            if (self.x_coords[i] >= settings.width) or (self.y_coords[i] >= settings.height):
                self.x_coords[i] = 'x'
                self.y_coords[i] = 'x'
                self.asteroid_sizes[i] = 'x'
                self.asteroid_speeds[i] = 'x'
                self.asteroid_direction_angles[i] = 'x'
            elif (self.x_coords[i] <= 0) or (self.y_coords[i] <= 0):
                self.x_coords[i] = 'x'
                self.y_coords[i] = 'x'
                self.asteroid_sizes[i] = 'x'
                self.asteroid_speeds[i] = 'x'
                self.asteroid_direction_angles[i] = 'x'
            i += 1

    def supply_asteroids(self):
        i = 0
        while i < self.MAX_ASTEROIDS:
            if self.x_coords[i] == 'x': # check for lack of asteroids
                x_or_y = random.choice(['x', 'y'])
                if x_or_y == 'x':
                    self.x_coords[i] = random.randint(0, settings.width)
                    self.y_coords[i] = random.choice([1, settings.height - 1])
                else:
                    self.y_coords[i] = random.randint(0, settings.height)
                    self.x_coords[i] = random.choice([1, settings.width - 1])
                self.asteroid_speeds[i] = random.randint(self.MIN_SPEED, self.MAX_SPEED)
                self.asteroid_direction_angles[i] = random.randint(0, 360)
                self.asteroid_sizes[i] = random.randint(self.MIN_SIZE, self.MAX_SIZE)
            i += 1

    ''' main methods '''
    def shape(self, i):
        self.supply_asteroids()
        shape = [
                self.x_coords[i] - self.asteroid_sizes[i],
                self.y_coords[i] - self.asteroid_sizes[i],
                self.x_coords[i] + self.asteroid_sizes[i],
                self.y_coords[i] + self.asteroid_sizes[i]
                ]
        return shape

    def direction(self):
        i = 0
        while i < self.MAX_ASTEROIDS:
            self.x_coords[i] = self.x_coords[i] + self.asteroid_speeds[i] \
                               * math.cos(math.radians(self.asteroid_direction_angles[i]))
            self.y_coords[i] = self.y_coords[i] + self.asteroid_speeds[i] \
                               * math.sin(math.radians(self.asteroid_direction_angles[i]))
            i += 1
        self.borders()
        self.supply_asteroids()