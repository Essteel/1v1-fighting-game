""" Functions for displaying text art in python fighter game

Functions
---------
title_text(): displays the game title text art
fight_text(): displays the game over text art
"""

def title_text():
    """ Function to display title text art

    The name of the game in text art, displayed on
    the welcome screen.
    """
    print("""
   ___       __  __               ______              __    _____      __   __  __
  / _ \__ __/ /_/ /  ___  ___    / __/ /________ ___ / /_  / __(_)__ _/ /  / /_/ /
 / ___/ // / __/ _ \/ _ \/ _ \  _\ \/ __/ __/ -_) -_) __/ / _// / _ `/ _ \/ __/_/ 
/_/   \_, /\__/_//_/\___/_//_/ /___/\__/_/  \__/\__/\__/ /_/ /_/\_, /_//_/\__(_)  
     /___/                                                     /___/              
    """)

def fight_text():
    """ Function to display game over text art

    The game over message and text art displayed on
    the game over screen.
    """
    print("""
                      GAME OVER!                                 
             @@@                   @@@.                  
           @@@@@@$$  @@            /@@@@@,               
            @@@@% @@@         @  @@@@@@@@                
            @@@@@              \\@  @@@@@                
           @@   @@@               @@@* @@@@              
          @@     &@@             @@@     @@@             
        @@       @@           @@@        @@@             
                                                         
    """)
