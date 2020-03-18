import random
cross = {0: "Do Nothing", 1: "North", 2: "East", 3: "West"}
eastStoryLine = {1: "the front yard",
                 2: "an old house",
                 3: "door",
                 4: "the mystical room",
                 5: "the dungeon",
                 6: "the side path",
                 7: "the grave yard"}

westStoryLine = {1: "the forest",
                 2: "the T section"}

# ------------------------------------EAST STORY LINE FUNCTIONS ALL HERE------------------------------------------------
def atMonster():
    print("The boy has come to the grave yard, and he encounters a skeleton soldier.")
    print("He decides to : \n1: run \n2: fight the skeleton soldier")
    optionFight = int(input("Please enter the option number: "))
    print('-'*70)
    if optionFight == 1:
        print("The boy has run away from the skeleton soldier, and he runs so hard that he forgets where he is")
        eastStory(eastStoryLine)
    elif optionFight == 2:
        print("The boy decides to fight with the skeleton soldier")
        if random.randint(1, 11) > 5:
            print("And he wins his battle, and returns to the garden")
            eastStory(eastStoryLine)
        else:
            print("And he lose his battle and gets killed by the skeleton")
            print("Game Over !")
    else:
        print("Wrong Message, Please try again!")


def atTheMysticRoom(eastStoryLine):
    print("The boy is at {}, and he finds a key to unlock the door,"
          "but he needs to solve a puzzle to get the key".format(eastStoryLine[4]))
    print("If:\n 1=2 \n 3=18 \n 5=50 \n 4=32 \n then 6=?")
    answer = int(input("Please enter your answer: "))
    print('-'*70)
    if answer == 72:
        print("Nice! You got the key!")
        return 1
    else:
        print("Wrong Answer! The trap is activated, the little boy is died.")
        print("Game Over!")
        return 0

def atTheHouse(eastStoryLine):
    print("The boy now is at {}".format(eastStoryLine[2]))
    print("And the boy has found that there was a {}, "
          "but it is locked".format(eastStoryLine[3]))
    print("Now he has two ways which he can go, "
          "\n1: {0} on the left or "
          "\n2: {1} on the right".format(eastStoryLine[4], eastStoryLine[6]))


def eastStory(eastStoryLine):
    print("The boy has come to the east garden, there are two ways he can go: ")
    print("1: {}".format(eastStoryLine[2]))
    print("2: {}".format(eastStoryLine[7]))
    optionEast = int(input("Please enter your option number: "))
    print('-'*70)
    if optionEast == 1:
        while True:
            atTheHouse(eastStoryLine)
            optionHouse = int(input("Please enter your option number: "))
            print('-'*70)
            if optionHouse == 1:
                key = atTheMysticRoom(eastStoryLine)
                if key == 0:
                    break
                else:
                    print("The little boy has escaped from the house, now he is at the backyard")
                    print("He spends few hours on walking through the hill")
                    print("Finally, he successfully meets his uncle, thanks for playing the game")
                    break
            elif optionHouse == 2:
                print("The boy is at {}, and he keeps going to find a way out".format(eastStoryLine[6]))
                atMonster()
                break
            else:
                print("Wrong Message, Please try again!")
                print('-'*70)
    elif optionEast == 2:
        atMonster()
    else:
        print("Wrong Message, Please try again!")

# ----------------------------------------------------------------------------------------------------------------------
# ------------------------------------WEST STORY LINE FUNCTIONS ALL HERE------------------------------------------------
def codePuzzle():
    num1 = random.randint(1,4)
    num2 = random.randint(1,4)
    num3 = random.randint(1,4)
    sum = num1 + num2 + num3
    product = num1 * num2 * num3
    print("The code requires three numbers to unlock, it's X+X+X = {0} and X * X * X = {1}".format(sum, product))
    print("Hint: the numbers all in range of 3")
    user1 = int(input("Please enter the first number to unlock: "))
    user2 = int(input("Please enter the second number to unlock: "))
    user3 = int(input("Please enter the third number to unlock: "))
    if user1 + user2 + user3 == sum and user1 * user2 * user3 == product:
        print("Excellent! The door is unlocked. The boy has successfully escaped!")
        print("The boy finds a bush to hide just to wait until those robbers are gone")
        print("Next day in the morning, robbers are gone. "
              "The boy successfully meets his uncle, thanks for playing the game")
    else:
        print("Wrong answer, the boy does not make it and gets caught by robbers again.")
        print("Game Over!")

def robber():
    print("The boy is on his way to meet his uncle, but he counters a group of robber and gets kidnapped...")
    print("Few hours later, the sky tuns into night. \nThose robbers have their meal done and ready to sleep")
    print("The boy has no idea where he is and he is tied with the rope")
    print("He figures a way to escapes and he made it, but accidentally wakes one of robbers")
    print("Robbers start chasing him while the boy is running as hell")
    print("The boy has come to the front gate and the gate is locked with a series of code")
    print('-'*70)
    codePuzzle()

def oldLady():
    print("Wolves are gone. The boy decides to take a rest under the tree and leave next day in the morning")
    print("He comes to a public square, and he sees an old lady fells on the floor. He wonders he should: ")
    print("1: Help her \n2: ignore her")
    ladyOption = int(input("Please enter the option numbers: "))
    print('-'*70)
    if ladyOption == 1:
        print("The boy decides to help the old lady, the old lady thanks for his help and decides to"
              " invite the boy to have dinner.")
        print("The boy meets the old lady's husband John, John decides to escort him to meet the boy's uncle")
        print("Finally, the boy successfully meets his uncle, thanks for playing the game")
    elif ladyOption == 2:
        print("The boy decides to ignore the old lady and walk away")
        robber()
    else:
        print("Error Message! Game Terminated!")

def fightWolves():
    if random.randint(1, 11) > 5:
        print("And he wins his battle!")
        eastStory(eastStoryLine)
    else:
        print("And he lose his battle and gets killed by the wolves")
        print("Game Over !")

def westStory(westStoryLine):
    print("The boy has come to the forest. When he is going to take a break, he encounters a group of wolves.")
    print("He should: \n 1: Fight with wolves \n 2: run")
    optionWolves = int(input("Please enter the option numbers: "))
    print('-'*70)
    if optionWolves == 1:
        print("The boy decides to fight with those wolves.")
        fightWolves()
    elif optionWolves == 2:
        print("The boy runs away from the wolves, but the wolves is still chasing him.")
        print("The boy arrives at {}, he decides to: ".format(westStoryLine[2]))
        print("1: Climb on the tree \n2: Fight with the wolves \n3: Keep running to other places")
        sectionOption = int(input("Please enter the option numbers: "))
        print('-'*70)
        if sectionOption == 1:
            print("The boy climbs on the tree and waits the wolves to leave")
            oldLady()
        elif sectionOption == 2:
            print("The boy decides to fight with those wolves.")
            fightWolves()
        elif sectionOption == 3:
            print("The boy decides to keep running, but he cannot out run the wolves, so he died.")
            print("Game Over!")
        else:
            print("Error Message! Game Terminated!")
# ----------------------------------------------------------------------------------------------------------------------

# -----------------------------------------------Main Function----------------------------------------------------------
print("")
print("Long time ago, a little boy wants to delivery a letter to his uncle, "
      "so he decides to leave his home and going out on his own.")

while True:
    print("The little boy has come to the cross, he needs to decide which way he should go: ")
    print("0: {}".format(cross[0]))
    print("1: {}".format(cross[1]))
    print("2: {}".format(cross[2]))
    print("3: {}".format(cross[3]))
    option = int(input("Please enter your option: "))

    if option == 1:
        print('-'*70)
        print("The little boy decides to go {}, but there is a big rock blocks his way, "
              "so the boy decides to turn back".format(cross[1]))
    elif option == 2:
        print('-'*70)
        print("The little boy decides to go {}, he will go to the east garden".format(cross[2]))
        eastStory(eastStoryLine)
        break
    elif option == 3:
        print('-'*70)
        print("The little boy decides to go {}, he will go to the west forest".format(cross[3]))
        westStory(westStoryLine)
        break
    elif option == 0:
        print('-'*70)
        print("The little boy decides to {}, and he will be back to his home, the game is over".format(cross[0]))
        break
    else:
        print("Wrong Message, End of the game!")
        break
