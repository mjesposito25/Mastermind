import os
import random

scores = {"player" : 0, "cpu" : 0, "player1" : 0, "player2" : 0}

def main():
    clear()
    print("Welcome to Mastermind - Py Edition")
    selection = int(input("1 - Player vs. CPU \n2 - Player vs. Player \n4 - Quit\n"))
    if selection == 1:
        gameScores(mode = 'pvc')
    elif selection == 2:
        gameScores(mode = 'pvp')

def gameScores(mode):
    while True:
        pvcScores = "Current Scores: \nPlayer: " + str(scores["player"]) + " \nCPU: " + str(scores["cpu"])
        pvpScores = "Current Scores: \nPlayer 1: " + str(scores["player1"]) + " \nPlayer 2: " + str(scores["player2"])
        print(pvpScores if mode == "pvp" else pvcScores)
        play = input("Play? [y/n]:")
        if play == 'y':
            if mode == "pvp":
                # for pvp players can switch roles
                mastermind = int(input("Which player is the mastermind? [1-2]: "))
                score = game(mode)
                if score < 0:
                    if mastermind == 1:
                        scores["player1"] += 10
                    else:
                        scores["player2"] += 10
                else:
                    if mastermind == 1:
                        scores["player2"] += score
                    else:
                        scores["player1"] += score
            elif mode == "pvc":
                score  = game(mode)
                if score > 0:
                    scores["player"] += score
                else:
                    scores["cpu"] += 10
            else:
                print('Something went wrong')
                break
        else:
            break
    main()

# maybe change rules to no reset every game
def setRules(numColors = 4, repeat = True, orderedFeedback = True):
    extraColors = ["black", "white", "purple", "orange"]

    rules = {
        "colors" : ["red", "blue", "green", "yellow"],
        "repeat" : repeat,
        "ordered" : orderedFeedback
    }

    # cannot go lower than 4 or higher than 8 colors
    if numColors < 4:
        return rules
    elif numColors > 8:
        numColors = 8
    
    # add extra colors
    numColors -= 4
    colors = rules["colors"] + extraColors[:numColors]
    rules["colors"] = colors
    return rules
    


def validation(rules, flavorText = 'code'):
    valid = False

    flavor = "\nWhat is the code, seperate by spaces: " if flavorText == 'code' else "What is your guess: "
    while valid != True:
        codeComma = input(flavor)
        code = codeComma.split(" ")

        valid = True
        # check if length of 4 colors
        if len(code) != 4:
            print("The only valid code length is 4")
            valid = False
        # check if correct colors
        for pin in code:
            if pin not in rules["colors"]:
                print("Sorry", pin, "is not a valid color")
                valid = False
        # if rules set to repeat = false, make sure there is no repeats 
        # using count and set save to a variable and if there is at least one repeat, set valid to false
        if rules["repeat"] == False:
            check = set([x for x in code if code.count(x) > 1])
            if len(check) > 0:
                print("The rule is set to no repeats")
                valid = False
    
    return code

def cpuGenerateCode(rules):
    colors = rules["colors"]
    code = []
    # if repeat is false, use random shuffle to chnge the order of list and then use the first 4 indices as the code
    # this works around different number of colors since it is 4-8
    if rules["repeat"] == False:
        random.shuffle(colors)
        code = colors[:4]
    # randomly get a number between the first color and last 
    # append that to the return list
    else:
        for i in range(4):
            color = colors[random.randint(0,len(colors)-1)]
            code.append(color)

    return code

# Gives player options which change the game rules
def difficulty():
    numColors = 4
    repeatColors = True
    ordered = True
    print("\n1 - 4 Colors, No Repeats, Feedback in Order")
    print("2 - 4 Colors, No Repeats, Unordered Feedback")
    print("3 - 6 Colors, No Repeats, Feedback in Order")
    print("4 - 6 Colors, Repeats Possible, Feedback in Order")
    print("5 - 6 Colors, Repeats Possible, Unordered Feedback")
    print("6 - 8 Colors, Repeats Possible, Feedback in Order")
    print("7 - 8 Colors, Repeats Possible, Unordered Feedback")
    diff = int(input("\nPick a difficulty [1-7]: "))

    if 3 <= diff <= 5:
        numColors = 6
    elif 6 <= diff <= 7:
        numColors = 8
    
    if 1 <= diff <= 3:
        repeatColors = False
    
    if diff in [2, 5, 7]:
        ordered = False
    return setRules(numColors, repeatColors, ordered)



def game(mode):
    turn = 1
    board = []
    
    # if pvp, allow players to change the rules
    if mode == "pvp":
        changeRules = input("Would you like to change the defualt rules? [y/n]: ").lower()
        if changeRules == 'n':
            rules = setRules()
        else:
            numColors = int(input("How many colors [4-8]: "))
            repeat = bool(input("The mastermind can repeat colors [True/False]: "))
            ordered = bool(input("The feedback is given in order [True/False]: "))
            rules = setRules(numColors, repeat, ordered)

    if mode == "pvc":
        rules = difficulty()
        code  = cpuGenerateCode(rules)

    if mode == "pvp":
        code = validation(rules)

        input("\nPress any key, the terminal will now clear")
    
    clear()

    # when playing against cpu would display shuffled color which the first 4 colors were the correct code
    random.shuffle(rules["colors"])

    # game is 9 turn long
    while (turn < 10):
        print('\nTURN', turn)
        print(100*'-')
        print("The available colors for this game are:", end=" ")
        for x in rules["colors"]: print(x, end=" ")
        print('\n' + 100*'-')
        
        guessList = validation(rules, "guess")

        feedback = []
        for i in range(4):
            # black is correct color and position
            if guessList[i] == code[i]:
                feedback.append('black')
            # white is correct color
            elif guessList[i] in code:
                feedback.append('white')
            # empty means color not in the code
            else:
                feedback.append("empty")

        # if unordered feedback use random shuffle
        if rules["ordered"] == False:
            random.shuffle(feedback)

        # add guess and feeback to board
        board.append((guessList, feedback))

        #display game so far
        for n in range(len(board)):
            print(n+1 , ":" , board[n])
        
        # check for continuation
        if 'white' in feedback or 'empty' in feedback:
            turn += 1
            if turn > 9:
                print("\n The code was: ", end="")
                print(code)
                print("\nMastermind wins!")
                return -10
                
        # if all black, the codebreaker wins
        else:
            print("\nCodebreaker wins!")
            return 10 - turn

# clears terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    main()
