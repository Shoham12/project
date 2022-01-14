from flask import Flask


class ScoreServer:

    def score_server(self):
        try:
            with open('Score.txt') as f:
                number = f.readlines()
                SCORE = int(number[0])
            return f"<html> <head> <title>Scores Game</title> </head> <body> <h1>The score is <div id=score>{SCORE}</div></h1> </body> </html>"
        except:
            ERROR = "There is an error!!!"
            return f"<html> <head> <title>Scores Game</title> </head> <body> <body> <h1><div id=score style=color:red>{ERROR}</div></h1> </body> </html>"


app = Flask(__name__)


@app.route('/')
def hello_world():
    return ScoreServer().score_server()


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')