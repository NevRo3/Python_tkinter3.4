import tkinter
import random
import time
import settings


class Game():

    def __init__(self, root):
        self.height = settings.height
        self.width = settings.width
        self.canvas = tkinter.Canvas(root, height = self.height, width = self.width, bg = settings.background,)
        self.inst_player = []
        self.ship_ID = []

        self.inst_asteroids = []
        self.asteroids_ID = []

        self.collision = False

        self.attempt = 1
        self.score = 0
        self.max_score = 0
        self.attempt_time = time.time()

    def create_player(self, player):
        shape = player.shape()
        player_ship = self.canvas.create_polygon(shape,
                                                outline = player.outline,
                                                fill = player.fill)
        self.ship_ID.append(player_ship)
        self.inst_player.append(player)
        self.canvas.pack()

    def create_asteroids(self, asteroids):
        i = 0
        while i < settings.max_asteroids:
            shape = asteroids.shape(i)
            asteroid = self.canvas.create_oval(
                                              shape,
                                              fill = random.choice(settings.colors),
                                              outline = random.choice(settings.colors))
            self.asteroids_ID.append(asteroid)
            i += 1
        self.inst_asteroids.append(asteroids)

        self.canvas_score = self.canvas.create_text(self.width * (4/5), 10, text = ('Score: ' + str(self.score)))
        self.canvas_max_score = self.canvas.create_text(self.width * (4/5), 20, text = ('Max score: ' + str(self.max_score)))
        self.canvas_attempt = self.canvas.create_text(self.width * (4/5), 30, text = ('Попытка: ' + str(self.attempt)))
        self.canvas.pack()

    def collision_check(self):
        if self.collision == True:
            pass
        else:
            i = 0
            while i < len(self.asteroids_ID):
                if (self.canvas.coords(self.ship_ID)[0] >= self.canvas.coords(self.asteroids_ID[i])[0]) \
                and (self.canvas.coords(self.ship_ID)[0] <= self.canvas.coords(self.asteroids_ID[i])[2]) \
                and (self.canvas.coords(self.ship_ID)[1] >= self.canvas.coords(self.asteroids_ID[i])[1]) \
                and (self.canvas.coords(self.ship_ID)[1] <= self.canvas.coords(self.asteroids_ID[i])[3]):
                    self.collision = True
                elif (self.canvas.coords(self.ship_ID)[2] >= self.canvas.coords(self.asteroids_ID[i])[0]) \
                and (self.canvas.coords(self.ship_ID)[2] <= self.canvas.coords(self.asteroids_ID[i])[2]) \
                and (self.canvas.coords(self.ship_ID)[3] >= self.canvas.coords(self.asteroids_ID[i])[1]) \
                and (self.canvas.coords(self.ship_ID)[3] <= self.canvas.coords(self.asteroids_ID[i])[3]):
                    self.collision = True
                elif (self.canvas.coords(self.ship_ID)[4] >= self.canvas.coords(self.asteroids_ID[i])[0]) \
                and (self.canvas.coords(self.ship_ID)[4] <= self.canvas.coords(self.asteroids_ID[i])[2]) \
                and (self.canvas.coords(self.ship_ID)[5] >= self.canvas.coords(self.asteroids_ID[i])[1]) \
                and (self.canvas.coords(self.ship_ID)[5] <= self.canvas.coords(self.asteroids_ID[i])[3]):
                    self.collision = True
                i += 1

        return self.collision

    def show_score(self):

        self.score = int(time.time() - self.attempt_time)
        if self.score > self.max_score:
            self.max_score = self.score
        self.canvas.itemconfigure(self.canvas_score, text = ('Score: ' + str(self.score)))
        self.canvas.itemconfigure(self.canvas_max_score, text = ('Max score: ' + str(self.max_score)))

    def restart(self):

        if self.collision_check() == True:

            for i in self.inst_player:
                i.position_x = settings.pos_x
                i.position_y = settings.pos_y
                i.phi = 270
                i.alpha = 270
                i.movement_speed = 0
            for i in self.inst_asteroids:
                i.x_coords = []
                i.y_coords = []
                i.asteroid_sizes = []
                i.asteroid_speeds = []
                i.asteroid_direction_angles = []
                i.fill()
                i.supply_asteroids()
            self.attempt_time = time.time()
            self.attempt += 1
            self.canvas.itemconfigure(self.canvas_attempt, text = ('Попытка: ' + str(self.attempt)))
            self.collision = False

    def update(self):

        new_player_coords = []
        for i in self.inst_player:
            new_player_coords.append(i.shape())
            i.direction()

        new_asteroids_coords = []
        for i in self.inst_asteroids:
            k = 0
            i.direction()
            while k < settings.max_asteroids:
                new_asteroids_coords.append(i.shape(k))
                k += 1

        z = 0
        while z < len(new_player_coords):
            self.canvas.coords(self.ship_ID[z], new_player_coords[z])
            z += 1

        z = 0
        while z < len(new_asteroids_coords):
            self.canvas.coords(self.asteroids_ID[z], new_asteroids_coords[z])
            z += 1

        self.show_score()
        self.restart()
        self.canvas.after(10, self.update)