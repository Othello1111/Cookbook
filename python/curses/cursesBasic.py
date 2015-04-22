import curses

stdscr = curses.initscr()

# Don't echo keys to screen when pressed
curses.noecho()

# React to keys instantly instead of normal buffer w/ return
curses.cbreak()

# Allow multibye keys like curses.KEY_LEFT
stdscr.keypad(1)


# Clean up and terminate
#curses.nocbreak()
#stdscr.keypad(0)
#curses.echo()
