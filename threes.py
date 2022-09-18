import random

numGames = 1000000

totalSum = 0


for i in range(numGames):
    totalHand = []
    numDice = 5
    # print("Round:", i)

    while numDice > 0:
        tempCurRoll = []
        keptDice = []
        diceRoll = []
        # print("Number of dice rolled:", numDice)
        #Roll number of dice left, parse 1's and 3's
        for i in range(numDice):
            currentDie = random.randint(1, 6)
            tempCurRoll.append(currentDie)
            if currentDie == 3:
                keptDice.append(currentDie)
            elif currentDie == 1:
                keptDice.append(currentDie)
            else:
                diceRoll.append(currentDie)
            

        #Sort leftover dice, add lowest die to keptDice if no 1 or 3
        diceRoll.sort()
        if len(keptDice) < 1:
            keptDice.append(diceRoll.pop(0))

        #Move any kept dice to totalHand, reduce die for reroll
        totalHand.extend(keptDice)
        numDice -= len(keptDice)

        # print("Current Roll:", tempCurRoll)
        # print("Dice Kept:", keptDice)
        # print("Total hand:", totalHand)
        # print("\n")


    for i in totalHand:
        if i == 3:
            totalSum += 0
        else:
            totalSum += i
print("\n")
print(f"Number of Games: {numGames:,}")
print("Average Score keeping 1's:", (totalSum/numGames))
