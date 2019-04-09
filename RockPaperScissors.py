import random

def playGame ():
    while (True):
        playerHand = input("rock, paper, or scissors? [type 'end' to stop the game] : \n")
        if (playerHand == "end"):
            print("Thanks for playing!")
            exit()
        compHand = getComputerHand()
        print("computer plays:", compHand)
        outcome = assess2(playerHand, compHand)
        if outcome is None:
            print("Invalid input. Make sure your spelling is right!")
        else:
            print("You", outcome.capitalize(), "!")
        print()


def getComputerHand():
    hands = ["rock", "paper", "scissors"]
    return random.choice(hands)

def assess(playerInput, compInput):

    if (playerInput == compInput):
        return "draw"
    elif (playerInput == "rock"):
        if (compInput == "paper"):
            return "lose"
        else:
            return "win"
    elif (playerInput == "paper"):
        if (compInput == "rock"):
            return "win"
        else:
            return "lose"
    elif (playerInput == "scissors"):
        if (compInput == "rock"):
            return "lose"
        else:
            return "win"
    else:
        return None

def assess2(playerInput, compInput):

    if (playerInput == compInput):
        return "draw"

    losesTo = {
        "rock": "paper",
        "paper": "scissors",
        "scissors": "rock"
    }

    loseCase = losesTo.get(playerInput, None)

    if loseCase is None:
        return None

    if loseCase == compInput:
        return "lose"

    return "win"

def testGame():
    def testOne(playerInput, compInput, outcome):
        result = assess2(playerInput, compInput)
        if result == outcome:
            print("[%s == %s] - passed for playerInput:%s and compInput:%s" % (
                outcome, result, playerInput, compInput))
        else:
            print("[%s != %s] - failed for playerInput:%s and compInput:%s" % (
                outcome, result, playerInput, compInput))

    #testing test
    testOne("rock", "rock", "win")

    #test cases
    testOne("rock", "rock", "draw")
    testOne("rock", "paper", "lose")
    testOne("rock", "scissors", "win")
    testOne("paper", "rock", "win")
    testOne("paper", "paper", "draw")
    testOne("paper", "scissors", "lose")
    testOne("scissors", "rock", "lose")
    testOne("scissors", "paper", "win")
    testOne("scissors", "scissors", "draw")

    #bad inputs
    testOne("scissrs", "rock", None)
    testOne("rck", "rock", None)



#testGame()
playGame()


