def welcome(name):
    return "Hello {} and welcome to the World of Games (WoG). Here you can find many cool games to play.".format(name)


def load_game():
    print("Please choose a game to play: 1. Memory Game - a sequence of numbers will appear for 1 second and you have "
          "to guess it back \n2. Guess Game - guess a number and see if you chose like the computer \n3. Currency Roulette"
          " - try and guess the value of a random amount of USD in ILS\n")

    game_number = input()

    while not game_number.isdigit():
        print("Please choose a digit! ")
        game_number = input()

    while int(game_number) < 1 or int(game_number) > 3:
        print("Please choose a game number between 1-3: ")
        game_number = input()
        while not game_number.isdigit():
            print("Please choose a digit! ")
            game_number = input()

    game_difficulty = input("Please choose game difficulty from 1 to 5: ")
    while not game_difficulty.isdigit():
        print("Please choose a digit! ")
        game_difficulty = input()

    while int(game_difficulty) < 1 or int(game_difficulty) > 5:
        print("Please choose a difficulty between 1-5: ")
        game_difficulty = input()
        while not game_difficulty.isdigit():
            print("Please choose a digit! ")
            game_difficulty = input()
