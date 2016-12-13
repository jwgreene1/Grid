from __future__ import division
import logging
import modules.Config as cfg
from kivy.uix.button import Button


class Plr:

    def __init__(self, num):
        self.logger = logging.getLogger('driver.modules.Plrs.Plr')
        self.num = num + 1
        self.x = 0 - num - 1
        self.y = 0 - num - 1
        self.status = cfg.PLR_WAITING
        self.printChar = cfg.PLR_POINT
        self.button = Button()

        info = self.PrintPlr()
        self.logger.info('# Initializing plr: %s' % info)

    def getButton(self):

        return self.button

    def setButton(self):

        self.button = Button(
            text='%s' % (self.num),
            size_hint=((1 / cfg.GRID_SIZE), (1 / cfg.GRID_SIZE)),
            background_color=[3,2,1,3],
            font_size=9,
            pos=(self.x * cfg.BLOCK_SIZE, self.y * cfg.BLOCK_SIZE + (2 * cfg.BLOCK_SIZE)))

    def PrintPlr(self):
        return('id: %s, printChar: %s, x: %s, y: %s' % (self.num, self.printChar, self.x, self.y))
