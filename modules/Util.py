import sys
import math
import modules.Config as cfg

def Distance(plr, blot):
    return math.sqrt((blot.x - plr.x) ** 2 + (blot.y - plr.y) ** 2)


def PrintGrid(grid):
    # Print the grid from the top down
    x = len(grid) - 1
    while(x >= 0):
        print
        if(x < 10):
            sys.stdout.write(' %s' % (x))
        else:
            sys.stdout.write('%s' % (x))

        # Print left to right
        for y in range(0, len(grid)):
            sys.stdout.write(grid[x][y].printChar)

        x -= 1

    print
    counter = 0
    sys.stdout.write('  ')
    while(counter < len(grid)):
        if(counter < 10):
            sys.stdout.write('  %d' % counter)
        else:
            sys.stdout.write(' %d' % counter)
        counter += 1
    print