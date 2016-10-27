import logging
from random import randint
import modules.Config as cfg

class Blot:

    def __init__(self):
        self.x = randint(0, cfg.GRID_SIZE - 1)
        self.y = randint(0, cfg.GRID_SIZE - 1)
        self.size = randint(cfg.BLOT_MIN, cfg.BLOT_MAX)
        self.printChar = cfg.BLOT_PRINT
        self.timer = cfg.BLOT_TIMEOUT
        self.status = cfg.BLOT_ACTIVE

    def PrintBlot(self):
        return('x: %s, y: %s, size: %s' % (self.x, self.y, self.size))