import zombiedice, random

class Bob:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll() # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information.
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        #  'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
        #            ('green', 'shotgun')]}

        # KEEP ROLLING UNTIL YOU GET TWO BRAINS
        brains = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']

            if brains < 2:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break

class Alice:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll() # first roll

        # KEEP ROLLING UNTIL YOU GET TWO SHOTGUNS
        shotgun = 0
        while diceRollResults is not None:
            shotgun += diceRollResults['shotgun']

            if shotgun < 2:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break

class Eugene:
    def __init__(self, name):
        self.name = name
        self.coin = ['heads','tails']

    def turn(self, gameState):
        diceRollResults = zombiedice.roll() # first roll

        # FLIP A COIN TO DECIDE IF YOU WILL CONTINUE OR STOP
        while diceRollResults is not None:
            coin_flip = random.choice(self.coin)

            if coin_flip == 'heads':
                diceRollResults = zombiedice.roll() # roll again
            else:
                break

class Rick:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll() # first roll

        # KEEP ROLLING UNTIL YOU GET TWO SHOTGUNS AND LESS THAN 5 BRAINS
        shotgun = 0
        brains = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']
            shotgun += diceRollResults['shotgun']

            if shotgun < 2 and brains < 5:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break

class Morgan:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll() # first roll

        # KEEP ROLLING UNTIL YOU GET MORE SHOTGUNS THAN BRAINS
        shotgun = 0
        brains = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']
            shotgun += diceRollResults['shotgun']

            if shotgun > brains:
                break
            else:
                diceRollResults = zombiedice.roll() # roll again

class Daryl:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll() # first roll

        # KEEP ROLLING UNTIL YOU GET 2 SHOTGUNS OR 1 SHOT GUN AND AT LEAST 5 BRAINS
        shotgun = 0
        brains = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']
            shotgun += diceRollResults['shotgun']

            if shotgun >= 1 and brains >= 5:
                break
            elif shotgun >= 2:
                break
            else:
                diceRollResults = zombiedice.roll() # roll again

class Maggie:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll() # first roll

        # KEEP ROLLING UNTIL YOU GET 2 SHOTGUNS OR 1 SHOT GUN AND AT LEAST 5 BRAINS
        # IF YOU GET 2 SHOTGUNS AND HAVE NO BRAINS KEEP ROLLING
        shotgun = 0
        brains = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']
            shotgun += diceRollResults['shotgun']

            if shotgun >= 1 and brains >= 5:
                break
            elif shotgun >= 2 and brains >= 1:
                break
            else:
                diceRollResults = zombiedice.roll() # roll again

class Negan:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll() # first roll

        # KEEP ROLLING UNTIL YOU GET 2 SHOTGUNS OR 1 SHOT GUN AND AT LEAST 6 BRAINS
        # IF YOU GET 2 SHOTGUNS AND HAVE NO BRAINS KEEP ROLLING
        shotgun = 0
        brains = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']
            shotgun += diceRollResults['shotgun']

            if shotgun >= 1 and brains >= 6:
                break
            elif shotgun >= 2 and brains >= 1:
                break
            else:
                diceRollResults = zombiedice.roll() # roll again

class Carl:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll() # first roll

        # KEEP ROLLING UNTIL YOU GET 2 SHOTGUNS OR 1 SHOT GUN AND AT Least 7 BRAINS
        # IF YOU GET 2 SHOTGUNS AND HAVE NO BRAINS KEEP ROLLING
        shotgun = 0
        brains = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']
            shotgun += diceRollResults['shotgun']

            if shotgun >= 1 and brains >= 7:
                break
            elif shotgun >= 2 and brains >= 1:
                break
            else:
                diceRollResults = zombiedice.roll() # roll again

class Lizzie:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll() # first roll

        # KEEP ROLLING UNTIL YOU GET 2 SHOTGUNS OR 1 SHOT GUN AND AT LEAST 6 BRAINS
        # IF YOU GET 2 SHOTGUNS AND HAVE NO BRAINS KEEP ROLLING
        # BUT IF ALL THE RED DICE HAS ALREADY BEEN ROLLED, ALWAYS KEEP GOING
        shotgun = 0
        brains = 0
        red_dice_remaining = 3
        rolled_red_dice = 0
        while diceRollResults is not None:
            for roll in diceRollResults['rolls']:
                if roll[0] == 'red':
                    red_dice_remaining -= 1
                    rolled_red_dice += 1

            if red_dice_remaining == 0 and rolled_red_dice == 3:
                diceRollResults = zombiedice.roll()
                continue

            brains += diceRollResults['brains']
            shotgun += diceRollResults['shotgun']
            if shotgun >= 1 and brains >= 6:
                break
            elif shotgun >= 2 and brains >= 1:
                break
            else:
                diceRollResults = zombiedice.roll() # roll again

class Shane:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        rolls_left = random.randint(1, 4)
        shotgun_count = 0
        while rolls_left > 0:
            diceRollResults = zombiedice.roll()
            shotgun_count += diceRollResults['shotgun']
            if shotgun_count >= 2:
                break
            rolls_left -= 1

zombies = (
    # zombiedice.examples.RandomCoinFlipZombie(name='Random'),
    # zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
    # zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 2 Shotguns', minShotguns=2),
    # zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 1 Shotgun', minShotguns=1),
    Bob(name='Bob'),
    Alice(name='Alice'),
    Rick(name='Rick'),
    Daryl(name='Daryl'),
    Maggie(name='Maggie'),
    Negan(name='Negan'),
    Carl(name='Carl'),
    Lizzie(name='Lizzie'),
    Eugene(name='Eugene'),
    Morgan(name='Morgan'),
    Shane(name='Shane'),
    # Add any other zombie players here.
)

# Uncomment one of the following lines to run in CLI or Web GUI mode:
# zombiedice.runTournament(zombies=zombies, numGames=1000)
zombiedice.runWebGui(zombies=zombies, numGames=1000)
