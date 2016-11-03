from __future__ import division
import time
import logging
import modules.Config as cfg
import modules.Util as Util
from modules.Grid import GridPoint as GridPoint
from modules.Plrs import Plr as Plr
from modules.Blot import Blot as Blot
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.app import App
from kivy.config import Config


class Gm:

    def __init__(self):
        self.logger = logging.getLogger('driver.modules.Gm.Gm')

        self.logger.info('Initializing Grid')
        self.grid = [[GridPoint() for _ in range(0, cfg.GRID_SIZE)] for _ in range(0, cfg.GRID_SIZE)]

        self.logger.info('Initializing Plrs')
        self.plrs = [Plr(_) for _ in range(0, cfg.PLR_NUM)]

        self.blots = [None for _ in range(0, cfg.BLOT_NUM)]
        self.blotCounter = 0

        self.plrsMadeIt = 0
        self.plrsHit = 0

        self.totalPos = 0

        self.GmApp = GmApp()

        Config.set('graphics', 'width', (cfg.GRID_SIZE * cfg.BLOCK_SIZE))
        Config.set('graphics', 'height', (cfg.GRID_SIZE * cfg.BLOCK_SIZE))

    def go(self):

        done = 0
        counter = 1

        print('Begin')

        self.GmApp.run()

        while not done:
            time.sleep(cfg.SLEEP_TIME)
            print('\nTIME: %d' % counter)
            counter += 1
            self.AdvancePlrs()
            self.UpdateBlots()
            self.CheckForHits()

            if cfg.PRINTING:
                Util.PrintGrid(self.grid)

            done = self.GmDone()

        print('Done!')

        self.GetStats()
        self.PrintStats()

    def PrintStats(self):

        print('Plrs             : %s' % len(self.plrs))
        print('Plrs who made it : %s' % self.plrsMadeIt)
        print('Plrs hit         : %s' % self.plrsHit)
        print('Percentage safe  : %0.2f%%' % (float(self.plrsMadeIt) / float(len(self.plrs)) * float(100)))
        print('Avg Distance     : %s' % self.avgPos)

    def GetStats(self):

        for plr in self.plrs:
            self.totalPos += plr.x

        self.avgPos = self.totalPos / len(self.plrs)

    def CheckForHits(self):
        for plr in self.plrs:
            if(plr.status is not cfg.PLR_GOING):
                continue
            else:
                for blot in self.blots:
                    if(blot is not None and blot.status is cfg.BLOT_ACTIVE):
                        distance = Util.Distance(plr, blot)
                        if(distance < blot.size):
                            plr.status = cfg.PLR_HIT
                            self.UpdateGrid(plr.x, plr.y, cfg.EMPTY_POINT)
                            self.plrsHit += 1
                            print('Distance  : %s' % distance)
                            print('Player Hit: %s' % plr.PrintPlr())
                            print('Blot      : %s' % blot.PrintBlot())
                            continue

    def UpdateBlots(self):
        # Get the new blot index
        newBlotIndex = self.blotCounter % cfg.BLOT_NUM
        # Get the old blot at that index
        oldBlot = self.blots[newBlotIndex]
        # If the blot is defined, put an empty point char in it's place
        if(oldBlot is not None):
            self.UpdateGrid(oldBlot.x, oldBlot.y, cfg.EMPTY_POINT)

        # Create a new blot, add it to blots and update the grid
        newBlot = Blot()
        self.blots[newBlotIndex] = newBlot
        self.UpdateGrid(newBlot.x, newBlot.y, newBlot.printChar)
        self.blotCounter += 1

        for blot in self.blots:
            # Deactivate blot if it's time is up
            if(blot is None or blot.status is not cfg.BLOT_ACTIVE):
                continue

            elif(blot.timer < 0):
                self.UpdateGrid(blot.x, blot.y, cfg.EMPTY_POINT)
                blot.status = cfg.BLOT_INACTIVE
                continue

            blot.timer -= 1

    def UpdateGrid(self, x, y, char):
        self.grid[x][y].printChar = char

    def AdvancePlrs(self):

        for plr in self.plrs:

            # Do nothing if done or hit
            if(plr.status is cfg.PLR_DONE or plr.status is cfg.PLR_HIT):
                continue

            # If on the grid, replace the last space with empty
            if(plr.status == cfg.PLR_GOING):
                self.UpdateGrid(plr.x, plr.y, cfg.EMPTY_POINT)

            # Advance
            plr.x += 1
            plr.y += 1

            # Test for done
            if(plr.x == len(self.grid)):
                plr.status = cfg.PLR_DONE
                self.plrsMadeIt += 1

            elif(plr.x == 0):
                plr.status = cfg.PLR_GOING

            if(plr.status == cfg.PLR_GOING):
                if(plr.num < 10):
                    self.UpdateGrid(plr.x, plr.y, ' %s ' % str(plr.num))
                else:
                    self.UpdateGrid(plr.x, plr.y, ' %s' % str(plr.num))

    def GmDone(self):
        # Assume done
        done = 1
        for plr in self.plrs:
           if(plr.status != cfg.PLR_DONE):
               if(plr.status is not cfg.PLR_HIT):
                   return 0

        return done


class GmApp(App):
    def build(self):
        layout = GridLayout(cols=cfg.GRID_SIZE, row_force_default=True, row_default_height=cfg.BLOCK_SIZE)

        height = cfg.GRID_SIZE - 1

        while height >= 0:
            width = 0
            while width < cfg.GRID_SIZE:
                layout.add_widget(Button(text='%d,%d' % (width, height), size_hint_x=None, width=cfg.BLOCK_SIZE, font_size=6))
                width += 1

            height -= 1

        return layout
