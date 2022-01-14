import random
import time
import sys


class MemoryGame:
    def __init__(self):
        self.difficulty = 3

    def generate_sequence(self):
        random_list = random.sample(range(1, 101), self.difficulty)
        print(random_list, end="")
        # flush stdout
        sys.stdout.flush()
        # wait a second
        time.sleep(0.7)
        # write a carriage return and new text
        print('\rThat was quick.. Lets see what you can remember.. ')
        return random_list

    def get_list_from_user(self):
        users_list = []
        for i in range(self.difficulty):
            users_selection = input("Please chose a number between 1 to 101: ")
            while not users_selection.isdigit():
                users_selection = input("Please chose a number! ")
            while int(users_selection) < 1 or int(users_selection) > 101:
                users_selection = input("Please chose between 1 and 101! ")
                while not users_selection.isdigit():
                    users_selection = input("Please chose a number! ")

            users_list.append(int(users_selection))

        return users_list

    def is_list_equal(self, list1, list2):
        if list1 == list2:
            return True
        else:
            return False

    def play(self):
        list1 = self.generate_sequence()
        list2 = self.get_list_from_user()

        return self.is_list_equal(list1, list2)


if __name__ == "__main__":
    print(MemoryGame().play())