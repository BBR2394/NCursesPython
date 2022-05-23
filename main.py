#!/usr/bin/env python3

import sys
import curses
from curses.textpad import Textbox, rectangle

def loopncurses(win):
    win.addstr(0, 0, "Current mode: Typing mode", curses.A_REVERSE)
    win.refresh()
    win.getkey()

def startCurses():
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)

    stdscr.clear() 

    stdscr.refresh()
    loopncurses(stdscr)
    # stdscr.getkey()

    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()

def windowExample():
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)
    
    stdscr.addstr(0, 0, "Enter IM message: (hit Ctrl-G to send)")

    editwin = curses.newwin(5,30, 2,1)
    rectangle(stdscr, 1,0, 1+5+1, 1+30+1)
    stdscr.refresh()

    box = Textbox(editwin)

    # Let the user edit until Ctrl-G is struck.
    box.edit()

    # Get resulting contents
    message = box.gather()

def main(av):
    print("ici tout commence")
    print(av)
    #startCurses()
    windowExample()

if __name__ == '__main__':
    main(sys.argv)