from os import system
# check

class ScreenCleaner:

    def Screen_cleaner(self):
        system('clear')


if __name__ == "__main__":

    SCORES_FILE_NAME = "Scores.txt"
    BAD_RETURN_CODE = 404
    ScreenCleaner().Screen_cleaner()
