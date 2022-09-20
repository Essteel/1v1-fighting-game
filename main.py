import curses
import time

# welcome screen
def main(stdscr):
    stdscr.clear()
    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_YELLOW)
    yellow_and_black = curses.color_pair(1)
    black_and_yellow = curses.color_pair(2)

    for i in range(30):
        stdscr.clear()
        color = black_and_yellow

        if i % 2 == 0:
            color = yellow_and_black
        
        stdscr.addstr('Python Street Fight!\n\n', color)
        stdscr.addstr('Press any key')
        stdscr.refresh()
        time.sleep(0.2)

    while True:
        key = stdscr.getkey()
        if key == curses.KEY_ENTER:
            break

    stdscr.getch()
# stdscr.addstr(0, 0, 'Please select a character:')
curses.wrapper(main)

# import Character

# # Create character objects
# bella_brawler = Character.Character('Bella Brawler', 350, 350, 30, 50)
# monty_mischief = Character.Character('Monty Mischief', 200, 200, 40, 70)
# sayo_swift = Character.Character('Sayo Swift', 200, 200, 50, 60)
# dave_danger = Character.Character('Dave Danger', 175, 175, 50, 80)

# Character.get_character_stats()
