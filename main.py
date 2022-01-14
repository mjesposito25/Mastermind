
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
            game()
        else:
            break


def game():

    #white - correct color
    #black - correct placement and color
    turn = 1

    colors = ["red", "blue", "green", "yellow"]
    for x in colors: print(x, end=" ")

    codeComma = input("\nWhat is the code, seperate by commas no spaces: ")
    code = codeComma.split(",")
    # add check for correct length and colors

    while (turn < 10):
        print('\nTURN', turn)
        print(10*'-')
        guess = input("Guess what the code is: ")
        guessList = guess.split(",")

        feedback = []
        for i in range(4):
            if guessList[i] == code[i]:
                feedback.append('black')
            elif guessList[i] in code:
                feedback.append('white')
            else:
                feedback.append("blank")
        print(feedback)
        
        if 'white' in feedback or 'blank' in feedback:
            turn += 1
            if turn > 9:
                print("Mastermind wins!")
        else:
            print("Codebreaker wins!")
            break



if __name__ == "__main__":
    game()

"""
-two player and single player mode
    -single player computer picks and awnsers
-change difficulty between randomly placing the feedback or in order
    -4 to 8 colors
    -allowing the mastermind to repeat colors in code
"""