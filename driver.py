import sys
import datetime
import logging
from modules.Gm import Gm
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

# Create the logger
logger = logging.getLogger('driver')

def initialize():

    # Create the logger
    logger.setLevel(logging.DEBUG)

    # Create file handler which logs even debug messages
    fh = logging.FileHandler('logs/driver.log')
    fh.setLevel(logging.DEBUG)

    # Create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(logging.ERROR)

    # Create formatter and add it to the handlers
    formatter = logging.Formatter('[%(levelname)8s] %(message)s (%(filename)s:%(lineno)s)')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    # Add the handlers to the logger
    logger.addHandler(fh)
    logger.addHandler(ch)

    logger.info('Logger initialized')

def main():

    initialize()

    logger.info('### Beginning Driver Execution - %s ###' % datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S'))

    gm = Gm()
    gm.go()

    logger.info('### Ending Driver Execution - %s ###' % datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S'))

if __name__ == '__main__':
    sys.exit(main())