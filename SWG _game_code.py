                                                #Exercise: 6
                                     #Game developmet: Snake, Water, Gun
#Modules used
import random
import string

#                                                 Game code
#                                                   Menu
def level():
    
    """This is the menu function of the game snake, water, gun. It will ask from the user to enter his/her name and number of rounds he/she wants to play"""

    print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\tSnake vs Water vs Gun")
    print("\t\t\t\t\t\t\t\t\t\t\t\t|---------------Menu---------------|")
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tStart: Press 0\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tRules: Press 1\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tExit: 2 ")
    play = int(input("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t"))
    if play == 0 :
        print("Enter your name: ", end=""),
        n = input()
        print("Choose many rounds game you want: \n\t\t1. 5 Rounds\n\t\t2. 11 Rounds\n\t\t3. 15 Rounds")
        print("Rounds: ",  end=""),
        r = int(input())
#                                                   Rounds
#                                                   level 1
        if r == 5:
            game(r, n)
#                                                   level 2
        elif r == 11:
            game(r, n)
#                                                   level 3
        elif r == 15:
            game(r, n)
        else:
            print("Please select rounds from given options")


#                                                   Rules
    elif play == 1:
        print("\t\t\t\t\t\t\t\t\t\t\t\t|---------------Rules---------------|")
        print("1. You have to choose 1 thing from the 3 options")
        print("2. Options are: Snake(s), Water(w), Gun(g)")
        print("3. You have to select one of the round level by typing the number of given rounds")
        print("4. You will get 1 point of each win")
        print("5. You have to play and win all the rounds to win the game")
        print("6. Criteria of win:")
        print("\t\t\t\ta. Snake kills Water\n\t\t\t\tb. Water kills Gun\n\t\t\t\tc. Gun kills Snake")
        print("7. Remember if match has draw both did not get any points")
        print("Enjoy the game")
    elif play == 2:
        print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tExiting...")
    else:
        print("Please choose correct key")


#                                           Gameplay code
def game(rounds, name):
    """This function is for snake, water, gun game. it need a rounds variable and name of player from user. This is the main function where all the gameplay run"""

    human_wins = 0
    comp_wins = 0
    start = 1
    while (start <= rounds):
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tRound: ", start)
        options = ["Snake", "Water", "Gun"]
        random.shuffle(options)
        comp = options[0]
        start += 1
        print("Enter your Choise: ", end=""),
        human = input()

        if human == "Snake" or human == "snake" or human == "s" or human == "S" or human == "Snakes" or human == "snakes":
            human = "Snake"
            print("\n\nComputer choise:", comp, "\nYour choise: ", human, "\n")
            if comp == "Water":

                print("You won", name)
                human_wins += 1
            elif comp == "Gun":
                print("Computer wins, sorry next time better luck!")
                comp_wins += 1
            else:
                print("Match draw")

        elif human == "Water" or human == "water" or human == "w" or human == "W":
            human = "Water"
            print("\n\nComputer choise:", comp, "\nYour choise: ", human, "\n")
            if comp == "Gun":
                print("You won", name)
                human_wins += 1
            elif comp == "Snake":
                print("Computer wins, sorry next time better luck!")
                comp_wins += 1
            else:
                print("Match draw")

        elif human == "Gun" or human == "gun" or human == "g" or human == "G" or human == "Guns" or human == "guns":
            human = "Gun"
            print("\n\nComputer choise:", comp, "\nYour choise: ", human, "\n")
            if comp == "Snake":
                print("You won", name)
                human_wins += 1
            elif comp == "Water":
                print("Computer wins, sorry next time better luck!")
                comp_wins += 1
            else:
                print("Match draw")

    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tResult of 5 round:")
    print("\t\t\t\t", name, "total wins\t\t\t\tComputer total wins")
    print("\t\t\t\t\t\t", human_wins, "\t\t\t\t\t\t\t\t", comp_wins)
    if human_wins > comp_wins:
        print("\n\t\t\t\tCongratulations", name, "You won the game")
    elif human_wins < comp_wins:
        print("\n\t\t\t\tSorry, computer wins the game, Try again to beat computer")
    else:
        print("\n\t\t\t\t\t\t\t\t\tGame has been draw")

    print("\nHome: Press 1\nExit: Press any key")
    again = input()
    if again == "1":
        level()
    else:
        print("Exiting...")


#                                                   opening of game
print("\t\t\t\t\t\t\t\t\t\t\t\t\tJHASA GAMES PRESENTS")
print("Press any key to open the game: ", end=""),
key = input()
level()