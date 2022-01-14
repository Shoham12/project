
class AddScore:

    def add_score(self, difficulty):

        points_of_winning = (difficulty * 3) + 5
        try:
            with open('Score.txt') as f:
                number = f.readlines()
                print(int(number[0]))

        except:

            file = open('Score.txt', "w")
            file.write("{}".format(points_of_winning))


if __name__ == "__main__":
    difficulty = 4
    AddScore().add_score(difficulty)
