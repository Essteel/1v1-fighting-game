# 1v1-fighting-game

## Style Guide

I utilised the PEP 8 style guide created by Guido van Rossum, Barry Warsaw and Nick Coghlan (2001) as well as the PEP 257 docstring style guide created by Goodger and van Rossum (2001) to inform the style of my code.

I also used Microsoft's Pylint extension for Visual Studio Code which checks code conforms to PEP8 style conventions as well as highlighting possible bugs or issues. I made the decision to follow Pylint's suggestion to keep code length below 100 characters to allow for better readibility.

---

## Features

### Character selection

The user will be able to select from a list of characters to play as when they start the game. Each character will have a unique set of stats.

### Action

Each turn the character can use their action to either attack or use an item (if they have one). If they use a basic attack, whether the attack is successful is based on a randomly generated integer. A special attack will always hit and an item will always be used successfully.

### Basic attack

The user will have access to a basic attack which is capable of doing a set amount of damage to the opponents health based on the character's stats.

### Special attack

The user will have access to two special attacks per battle. The special attack will always hit the opponent.

### Health items

Health items can be used by the user to increase their character's health. The user will have two health items per battle.

### Power ups

Power up items will be picked up by the player if they perform a basic attack that is a critical hit (a high number for the randomly generated integer). These items can be used during the users action to perform a more powerful basic attack.

---

## Implementation plan

I used Agile methodology to implement my plan for creating the application. This can be seen in my Trello board here: <https://trello.com/b/2zmjYwyn/siannonsteelt1a3>.

I created a card for features that I wanted to implement within the program. I organised them by priority with the most important cards to complete at the top with a traffic light label system and added target dates for completion.

![Beginning of creation of a Trello board for the project](docs/trello_initial_setup.png)

Each feature has a card with a checklist of things for me to complete to get the feature working. They are also labelled with either High, Medium or Low priority as well as an ideal date for completion.

![Checklist of a card in trello](docs/trello_card.png)

I created the board with four columns so that I could see which stage I was at with each feature and cross-check this with the completion date and how many of the checklist items were completed. I would check the board when I took breaks to ensure that I was on track and to check of the tasks that were completed.

![Midway through project trello board screenshot](docs/trello_progress.png)

If I had time or decided a feature would be beneficial to the app I could then add it in once I could see that the project was on track for completion and critical features had been tested.

!["Screenshot of project nearly completed in Trello"](docs/trello_near_completion.png)

---

## Help documentation

This information can also be found within the application in the help.md file.

### Requirements

- Python 3.6 or higher
- Compatible with MacOS and Linux, and Windows (if using WSL)

Third party modules (these will be installed automatically if you follow the installation instructions below):

- Clear Module: <https://pypi.org/project/clearing/>
- python-readchar: <https://pypi.org/project/readchar/>
- Simple Terminal Menu: <https://pypi.org/project/simple-term-menu/>

### Game features

- Choose your character and the game will randomly assign you an opponent to battle.
- Attack your opponent with a basic or special attack.
- Earn power ups for performing critical attacks.
- Use health potions to help give you the edge over your opponent.

### Installation

1. Please ensure you have Python3 installed on your computer, if you do not have it installed please download it from here: <https://www.python.org/downloads/>

2. Then please either navigate to <https://github.com/Essteel/1v1-fighting-game> to download the repository or do so in your terminal using the following command:

   `git clone https://github.com/Essteel/1v1-fighting-game.git`

3. Next navigate to the location where you saved or downloaded the game using the cd command. For example:

   `cd users/downloads/1v1-fighting-game-main`

4. Run the following command to check and install all required python packages and run the game:

   `bash run_game.sh`

---

## How the application works

Upon launching the program the welcome screen is displayed and prompts the user to press any key.

!["Welcome screen for python street fighter game"](docs/welcome_screen.png)

Once a key is pressed, the user will then be presented with a menu with options to view the characters stats, select a character or quit the game. The user can select an option by navigating with the up and down keys and using enter to select an option.

!["Start menu screen for python street fighter game"](docs/start_menu.png)

Choosing the option to view character stats displays the name, health, attack and special attacks for the four playable characters. They can then use the back option to return to the menu.

Choosing the select character option will prompt the user to make their selection or to head back to the menu. If they choose the option to make a selection, they must enter a number between 1-4 to choose their character.

If they enter a number that is not between 1-4 or they enter a string, they will be prompted to try again until a number between 1-4 is entered.

They are then presented with the battle screen which prints a message confirming the character selection, displays a hud with the character and opponent health and inventory as well as the menu for carrying out actions. The user can either choose a basic attack, special attack, use an item or quit the game.

!["Action menu screen for python street fighter game"](docs/action_menu.png)

Basic attacks for the player will be successful based on chance. If they hit, the message is printed to the screen and opponents' health is reduced by the player's attack damage. On a failed attack a message will be printed to the screen and the opponents health will not be reduced. The opponent will then attack and their attack always hits.

!["Basic attack python street fighter game"](docs/basic_attack_success.png)

Players also have 2 special attacks to use per game that do more damage than the basic attack and will always be successful. When a special attack is used a message will be displayed on the screen showing how many special attacks are left and the opponent’s health is reduced by the player’s special attack damage. If the player runs out of special attacks and attempts to use it a message will show telling them they have no special attacks left.

!["Special attack in python street fighter game"](docs/special_attack.png)

The user can navigate to the items menu to choose either a health item or a power up. Players start with 2 health items and can use their action to use a health item to restore some hp. The opponent will then still attack. If the player has run out of health items a message will be printed telling the user that they have no health items left. The current number of health items is displayed on the screen.

!["Item menu screen in python street fighter game"](docs/item_menu.png)

Power up items become available if the player scores a critical hit. The number of health items currently available are displayed on the screen. Using a power up as your action will perform an attack, which reduces the opponent’s health by the value of the basic attack plus the value of the power up.

!["Getting a power up in python street fighter game"](docs/got_power_up.png)

If the player wins, loses or decides to quit the game at any time they will be taken to the game over screen which will ask them to confirm if they want to quit or play another game. Winning, losing or quitting will result in a different game over message. If the user enters a value that is not ‘q’ or ‘s’ they will be asked to try again.

!["Game over screen for python street fighter game"](docs/game_over_lost.png)

## Testing

I performed unit testing on important features to the application using pytest. I also performed manual testing after each major change to the application to ensure it was still running as expected.

| Feature (location)                       | Test case                                                                                                                                                      | Expected Outcome                                                                                                                                                        | Actual Outcome                                                                                                                                                          | Notes               |
| ---------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- |
| Unit tests                               |
| Character selection                      | Test if correct name attribute is assigned and in the correct format when the bella\_brawler object is passed to the select\_character function                | Name attribute is 'Bella Brawler'                                                                                                                                       | Name attribute is 'Bella Brawler'                                                                                                                                       | Working as expected |
| Character selection                      | Test if correct name attribute is assigned and in the correct format when the monty\_mischief object is passed to the select\_character function               | Name attribute is 'Monty Mischief'                                                                                                                                      | Name attribute is 'Monty Mischief'                                                                                                                                      | Working as expected |
| Character selection                      | Test if the correct value for hp is assigned and in the correct format when the sayo\_swift object is passed to the select\_character function                 | Hp attribute is 200                                                                                                                                                     | Hp attribute is 200                                                                                                                                                     | Working as expected |
| Character selection                      | Test if the correct value for hp is assigned and in the correct format when the dave\_danger object is passed to the select\_character function                | Hp attribute is 175                                                                                                                                                     | Hp attribute is 175                                                                                                                                                     | Working as expected |
| Character selection                      | Test if the correct value for special\_attack is assigned and in the correct format when the dave\_danger object is passed to the select\_character function   | Special\_attack attribute is 80                                                                                                                                         | Special\_attack attribute is 80                                                                                                                                         | Working as expected |
| Character selection                      | Test if the correct value for special\_attack is assigned and in the correct format when the bella\_brawler object is passed to the select\_character function | Special\_attack attribute is 50                                                                                                                                         | Special\_attack attribute is 50                                                                                                                                         | Working as expected |
| Character selection                      | Test if the correct attributes are assigned to the opponent object when the bella\_brawler and opponent objects are passed to the copy\_attributes function    | Opponent.\_\_dict\_\_ = {'name': 'Bella Brawler', 'max\_hp': 350, 'hp': 350, 'basic\_attack': 30, 'special\_attack': 50}                                                | Opponent.\_\_dict\_\_ = {'name': 'Bella Brawler', 'max\_hp': 350, 'hp': 350, 'basic\_attack': 30, 'special\_attack': 50}                                                | Working as expected |
| Character selection                      | Test if the correct attributes are assigned to the opponent object when the dave\_danger and opponent objects are passed to the copy\_attributes function      | Opponent.\_\_dict\_\_ = {'name': 'Dave Danger', 'max\_hp': 175, 'hp': 175, 'basic\_attack': 50, 'special\_attack': 80}                                                  | Opponent.\_\_dict\_\_ = {'name': 'Dave Danger', 'max\_hp': 175, 'hp': 175, 'basic\_attack': 50, 'special\_attack': 80}                                                  | Working as expected |
| Performing attacks                       | Test if the basic attack attribute value has been correctly assigned to the dave\_danger object                                                                | Basic\_attack is 50                                                                                                                                                     | Basic\_attack is 50                                                                                                                                                     | Working as expected |
| Performing attacks                       | Test if the basic attack attribute value has been correctly assigned to the monty\_mischief object                                                             | Basic\_attack is 40                                                                                                                                                     | Basic\_attack is 40                                                                                                                                                     | Working as expected |
| Performing attacks                       | Test if the special attack attribute value has been correctly assigned to the bella\_brawler object                                                            | Special\_attack is 50                                                                                                                                                   | Special\_attack is 50                                                                                                                                                   | Working as expected |
| Performing attacks                       | Test if the basic attack attribute value has been correctly assigned to the sayo\_swift object                                                                 | Special\_attack is 60                                                                                                                                                   | Special\_attack is 60                                                                                                                                                   | Working as expected |
| Performing attacks                       | Tests if the value of Monty's hp is calculated correctly after a basic attack performed by Bella                                                               | Opponent hp is 170                                                                                                                                                      | Opponent hp is 170                                                                                                                                                      | Working as expected |
| Performing attacks                       | Tests if the value of Dave's hp is calculated correctly after a basic attack performed by Sayo                                                                 | Opponent hp is 125                                                                                                                                                      | Opponent hp is 125                                                                                                                                                      | Working as expected |
| Performing attacks                       | Tests if the value of Bella's hp is calculated correctly after a basic attack performed by Sayo                                                                | Opponent hp is 290                                                                                                                                                      | Opponent hp is 290                                                                                                                                                      | Working as expected |
| Performing attacks                       | Tests if the value of Monty's hp is calculated correctly after a basic attack performed by Dave                                                                | Opponent hp is 120                                                                                                                                                      | Opponent hp is 120                                                                                                                                                      | Working as expected |
| Manual tests                             |
| Welcome screen                           | Pressing a button other than Enter on the welcome screen                                                                                                       | Program continues to start menu                                                                                                                                         | Program continues to start menu                                                                                                                                         | Working as expected |
| Character selection (start menu)         | Test the response when the 'view character stats' sub menu is selected                                                                                         | Program prints name, health, basic attack and special attack for all four characters                                                                                    | Program prints name, health, basic attack and special attack for all four characters                                                                                    | Working as expected |
| Character selection (start menu)         | Test the response when pressing buttons other than Up, Down and Enter whilst on the menu                                                                       | There should be no response within the program                                                                                                                          | J and K keys also move selector up and down                                                                                                                             | Not an issue        |
| Character selection (start menu)         | Test the response when a negative number is input on the 'make a selection' sub-menu                                                                           | User is told they did not enter a number between 1-4 and is prompted to try again                                                                                       | User is told they did not enter a number between 1-4 and is prompted to try again                                                                                       | Working as expected |
| Character selection (start menu)         | Test the response when a string is input on the 'make a selection' sub-menu                                                                                    | User is told to select a character by entering a number between 1-4                                                                                                     | User is told to select a character by entering a number between 1-4                                                                                                     | Working as expected |
| Quitting the game (start menu)           | Test the outcome of selecting the 'Quit' option                                                                                                                | Game over screen displays asking user if they want to exit or try again                                                                                                 | Game over screen displays asking user if they want to exit or try again                                                                                                 | Working as expected |
| Performing attacks (action menu)         | Test the basic attack function when successful reduces the opponents health                                                                                    | Message printed that the attack hit. HUD shows that opponent health is reduced                                                                                          | Message printed that the attack hit. HUD shows that opponent health is reduced                                                                                          | Working as expected |
| Performing special attacks (action menu) | Test the special attack function reduces the opponents health                                                                                                  | Message printed that user used a special attack, how many special attacks they have left and the HUD shows that the opponent health is reduced                          | Message printed that user used a special attack, how many special attacks they have left and the HUD shows that the opponent health is reduced                          | Working as expected |
| Performing special attacks (action menu) | Test that the special attack function can no longer be used when the special attack guage is 0                                                                 | Message printed that the user has run out of special attacks                                                                                                            | Message printed that the user has run out of special attacks                                                                                                            | Working as expected |
| Using items (items sub-menu)             | Test the response when a health item is selected                                                                                                               | Message printed that a health item was used and how many the user has left. HUD updates to display remaining health items                                               | Message printed that a health item was used and how many the user has left. HUD updates to display remaining health items                                               | Working as expected |
| Using items (items sub-menu)             | Test the response when a power up is used                                                                                                                      | Message printed that a power up item was used and how many the user has left. HUD updates to display remaining power items. Damage is taken off of the opponents health | Message printed that a power up item was used and how many the user has left. HUD updates to display remaining power items. Damage is taken off of the opponents health | Working as expected |
| Quitting the game (action menu)          | Test the outcome of selecting the 'Quit' option                                                                                                                | Game over screen displays asking user if they want to exit or try again                                                                                                 | Game over screen displays asking user if they want to exit or try again                                                                                                 | Working as expected |
| Quitting the game (game over screen)     | Test the response when the user inputs 'q'                                                                                                                     | Program ends and prints message 'See you next time!'                                                                                                                    | Program ends and prints message 'See you next time!'                                                                                                                    | Working as expected |
| Quitting the game (game over screen)     | Test the response when the user inputs a string                                                                                                                | Message telling the user the input was invalid and prompts the user to enter 'q' or 'a'                                                                                 | Message telling the user the input was invalid and prompts the user to enter 'q' or 'a'                                                                                 | Working as expected |
| Quitting the game (game over screen)     | Test the response when the user inputs an integer                                                                                                              | Message telling the user the input was invalid and prompts the user to enter 'q' or 'a'                                                                                 | Message telling the user the input was invalid and prompts the user to enter 'q' or 'a'                                                                                 | Working as expected |
| Replay (game over screen)                | Test the response when the user inputs 'a'                                                                                                                     | Program restarts                                                                                                                                                        | Program restarts                                                                                                                                                        | Working as expected |
---

## Resources referenced

### Style guide

van Rossum, G, Warsaw, B, and Coghlan, N, 2001, *PEP 8 - Style Guide for Python Code*, python.org <https://peps.python.org/pep-0008/>

Goodger, D and van Rossum, G, 2001, *PEP 257 - Docstring Conventions*, python.org <https://peps.python.org/pep-0257/>

### ASCII art

- I used 'Many Tools.org' to convert an image I created to a simple ASCII representation: <https://manytools.org/hacker-tools/convert-images-to-ascii-art/go/>

- I created the welcome message ASCII art using 'Patorjk.com':
  <http://patorjk.com/software/taag/>

### Third party modules<img width="509" alt="action_menu" src="https://user-images.githubusercontent.com/110761232/192143176-5b7bc484-e5d2-453b-a5f3-5c14c778052c.png">
<img width="328" alt="basic_attack_success" src="https://user-images.githubusercontent.com/110761232/192143178-7e414943-2192-4142-a9c8-561c31db0a2d.png">
<img width="430" alt="game_over_lost" src="https://user-images.githubusercontent.com/110761232/192143180-c505c829-b678-4dc1-be3c-6d5a07de7505.png">
![got_power_up](https://user-images.githubusercontent.com/110761232/192143182-740ddffd-2728-4054-bf4e-32bb6412c9a2.png)
<img width="430" alt="item_menu" src="https://user-images.githubusercontent.com/110761232/192143184-a9004761-4304-4f5f-bcc1-3dc8ed08044b.png">
<img width="430" alt="special_attack" src="https://user-images.githubusercontent.com/110761232/192143185-8209606a-3a3c-4feb-a625-2e3906a91931.png">
<img width="188" alt="start_menu" src="https://user-images.githubusercontent.com/110761232/192143187-e301ec63-7b46-4a8d-aae0-6fd0bce9a420.png">
![trello_card](https://user-images.githubusercontent.com/110761232/192143190-1cdf30ef-7554-461f-b843-07e633c1779b.png)
![trello_initial_setup](https://user-images.githubusercontent.com/110761232/192143191-6677e2a1-d892-4e53-b462-d0de557b966a.png)
![trello_near_completion](https://user-images.githubusercontent.com/110761232/192143193-da830b6a-7df6-4010-8cb6-07968523bc4b.png)
![trello_progress](https://user-images.githubusercontent.com/110761232/192143194-d28f73ea-9619-474a-9123-6eff302bed09.png)
<img width="602" alt="welcome_screen" src="https://user-images.githubusercontent.com/110761232/192143195-ae910755-380b-42f6-9c89-6d06d98acf47.png">


Clear Module
Dixon, J, 2020, *Clear Module*, last updated 2020, Python Package Index <https://pypi.org/project/clearing/>

python-readchar
García, M, 2014, *python-readchar*, last updated 2022, Python Package Index <https://pypi.org/project/readchar/>

Simple Terminal Menu
Meyer, I, 2019, *Simple Terminal Menu*, last updated 2022, Python Package Index <https://pypi.org/project/simple-term-menu/>
