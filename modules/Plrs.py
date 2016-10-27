import logging
import modules.Config as cfg


class Plr:

    def __init__(self, num):
        self.logger = logging.getLogger('driver.modules.Plrs.Plr')
        self.num = num + 1
        self.x = 0 - num - 1
        self.y = 0 - num - 1
        self.status = cfg.PLR_WAITING
        self.printChar = cfg.PLR_POINT

        info = self.PrintPlr()
        self.logger.info('# Initializing plr: %s' % info)

    def PrintPlr(self):
        return('id: %s, printChar: %s, x: %s, y: %s' % (self.num, self.printChar, self.x, self.y))
