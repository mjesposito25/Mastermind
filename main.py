
# make main the score keeper that calls the game function
# game function returns winner
def main():
    print("Welcome to Mastermind - Py Edition")
    selection = int(input("1 - Player vs. CPU\n 2 - Player vs. Player\n 3 - Rules\n 4 - Quit"))
    if selection == 1:
        game()

def gameScores():
    player = 0
    cpu = 0
    while True:
        print("Current Scores:\n Player:", player, "\nCPU:", cpu)
        play = input("Play? [y/n]:")
        if play == 'y':
            score  = game()
            if score > 0:
                player += 1
            else:
                cpu += 1
        else:
            break

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
    


def validateCode(rules):
    valid = False
    while valid != True:
        codeComma = input("\nWhat is the code, seperate by spaces: ")
        code = codeComma.split(" ")

        valid = True

        if len(code) != 4:
            print("The only valid code length is 4")
            valid = False

        for pin in code:
            if pin not in rules["colors"]:
                print("Sorry", pin, "is not a valid color")
                valid = False

        if rules["repeat"] == False:
            check = set([x for x in code if code.count(x) > 1])
            if len(check) > 0:
                print("The rule is set to no repeats")
                valid = False
    
    return code


def game():
    
    changeRules = input("Would you like to change the defualt rules? [y/n]: ").lower()
    if changeRules == 'n':
        rules = setRules()
    else:
        numColors = int(input("How many colors [4-8]: "))
        repeat = bool(input("The mastermind can repeat colors [True/False]: "))
        ordered = bool(input("The feedback is given in order [True/False]: "))
        rules = setRules(numColors, repeat, ordered)
    
    #white - correct color
    #black - correct placement and color
    turn = 1
    board = []

    print("\nThe available colors to use:", end=" ")
    for x in rules["colors"]: print(x, end=" ")

    code = validateCode(rules)

    while (turn < 10):
        print('\nTURN', turn)
        print(15*'-')
        guess = input("Guess what the code is: ")
        guessList = guess.split(" ")

        feedback = []
        for i in range(4):
            if guessList[i] == code[i]:
                feedback.append('black')
            elif guessList[i] in code:
                feedback.append('white')
            else:
                feedback.append("empty")
        board.append((guessList, feedback))
        for n in range(len(board)):
            print(n+1 , ":" , board[n])
        
        if 'white' in feedback or 'empty' in feedback:
            turn += 1
            if turn > 9:
                print("\nMastermind wins!")
                return -1
        else:
            print("\nCodebreaker wins!")
            return 1




if __name__ == "__main__":
    main()

"""
-two player and single player mode
    -single player computer picks and awnsers
-change difficulty between randomly placing the feedback or in order
    -4 to 8 colors
    -allowing the mastermind to repeat colors in code
"""