import Character

bella_brawler = Character.Character('Bella Brawler', 350, 350, 30, 50)
monty_mischief = Character.Character('Monty Mischief', 200, 200, 40, 70)
sayo_swift = Character.Character('Sayo Swift', 200, 200, 50, 60)
dave_danger = Character.Character('Dave Danger', 175, 175, 50, 80)

# function that will allow user to view a list of characters and their stats
def get_character_stats():
    user_input = input('View character stats (y/n): ').lower()
    if user_input == 'y':
        return print(f'Please pick a character:\n{bella_brawler.__dict__}\n{monty_mischief.__dict__}\n{sayo_swift.__dict__}\n{dave_danger.__dict__}')

get_character_stats()
