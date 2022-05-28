import tkinter

from player import Player
from game import Game
from asteroids import Asteroids

root = tkinter.Tk()
player = Player(root)
asteroids = Asteroids(root)
game = Game(root)

game.create_player(player)
game.create_asteroids(asteroids)

game.update()

root.mainloop()