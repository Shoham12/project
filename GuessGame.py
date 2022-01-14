import random


class GuessGame:
    def __init__(self):
        self.difficulty = 7

    def generate_number(self):
        num = random.randint(1, self.difficulty)
        return num

    def get_guess_from_user(self):
        users_selection = input("Please chose a number between 1 and {}: ".format(self.difficulty))
        while not users_selection.isdigit():
            users_selection = input("Please chose a number! ")
        while int(users_selection) < 1 or int(users_selection) > self.difficulty:
            users_selection = input("Please chose a number between 1 and {}! ".format(self.difficulty))
            while not users_selection.isdigit():
                users_selection = input("Please chose a number! ")

        return int(users_selection)

    def compare_results(self, num1, num2):
        if num1 == num2:
            return True
        else:
            return False

    def play(self):
        num1 = self.generate_number()
        num2 = self.get_guess_from_user()

        return self.compare_results(num1, num2)


if __name__ == "__main__":
    print(GuessGame().play())