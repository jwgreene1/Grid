import logging
from random import randint
import modules.Config as cfg
from kivy.graphics.vertex_instructions import Line
from kivy.uix.widget import Widget

class Blot:

    def __init__(self):
        self.x = randint(0, cfg.GRID_SIZE - 1) * cfg.BLOCK_SIZE
        self.y = randint(0, cfg.GRID_SIZE - 1) * cfg.BLOCK_SIZE  + (2 * cfg.BLOCK_SIZE)
        self.size = randint(cfg.BLOT_MIN, cfg.BLOT_MAX) * cfg.BLOCK_SIZE
        self.timer = cfg.BLOT_TIMEOUT
        self.status = cfg.BLOT_INACTIVE

        wid = Widget()

        with wid.canvas:
            Line(circle=(self.x, self.y, self.size))

        self.circle = wid

    def activate(self):
        self.status = cfg.BLOT_ACTIVE

    def GetCircle(self):
        return self.circle

    def PrintBlot(self):
        return('x: %s, y: %s, size: %s' % (self.x, self.y, self.size))