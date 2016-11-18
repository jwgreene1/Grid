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
#        self.button = Button(text='%s' % (self.num), size_hint_x=None, width=cfg.BLOCK_SIZE, font_size=6, background_color=[0,0,1,1])

        info = self.PrintPlr()
        self.logger.info('# Initializing plr: %s' % info)
        
    def getButton(self):
        button = Button(
            text='%s' % (self.num),
            width = cfg.BLOCK_SIZE,
            height = cfg.BLOCK_SIZE,
            font_size = 9,
            pos = (self.x * cfg.BLOCK_SIZE, self.y * cfg.BLOCK_SIZE))
            
        return button

    def PrintPlr(self):
        return('id: %s, printChar: %s, x: %s, y: %s' % (self.num, self.printChar, self.x, self.y))
