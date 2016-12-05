import logging
from random import randint
import modules.Config as cfg
from kivy.graphics import Line

class Blot:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = 0
        self.timer = 0
        self.status = cfg.BLOT_INACTIVE
        self.circle = Line()

    def activate(self):
        self.x = randint(0, cfg.GRID_SIZE - 1)
        self.y = randint(0, cfg.GRID_SIZE - 1)
        self.size = randint(cfg.BLOT_MIN, cfg.BLOT_MAX)
        self.timer = cfg.BLOT_TIMEOUT
        self.status = cfg.BLOT_ACTIVE
        self.circle = Line(circle=(self.x, self.y, self.size))
        self.circle.close = True
        self.circle.bind(None)

    def GetCircle(self):
        return self.circle

    def PrintBlot(self):
        return('x: %s, y: %s, size: %s' % (self.x, self.y, self.size))