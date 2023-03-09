import random
numberOfStreaks = 0

for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    coinFlips = []
    streakExists = False
    streakCounter = 1
    for i in range(100):
        randomNumber = random.randint(0,1)
        if randomNumber == 0:
            coinFlips.append('H')
        elif randomNumber == 1:
            coinFlips.append('T')

        # Code that checks if there is a streak of 6 heads or tails in a row.
        if i > 0 and coinFlips[i] == coinFlips[i - 1]:
            streakCounter += 1
            if streakCounter == 6:
                streakExists = True
        else:
            streakCounter = 1
    if streakExists == True:
        numberOfStreaks += 1

print('Chance of streak: %s%%' % (numberOfStreaks / 100))