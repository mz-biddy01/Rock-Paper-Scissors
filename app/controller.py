from flask import render_template, request, redirect, session, url_for
import json   
from app import app
from app.player import Player
from app.players_list import players
from app.game import Game
# from app.models.player import Player
# from app.models.player_list import players, play_new_game
# from app.models.game import Game
# JSON is a syntax for storing and exchanging data.


@app.route('/rock')
def rock():
    return "Player 1 wins by playing rock"

@app.route("/paper")
def paper():
    return "Player 2 wins by playing paper"


@app.route("/scissors")
def scissors():
    return "Player 3 wins by playing scissors"


@app.route('/play')
def index():
    return render_template('index.html')


@app.route("/winner")
def show_winner():
    result = session['result']
    return render_template("winner.html", result=json.loads(result))


@app.route('/play', methods=['POST'])
def play_game():
    game = Game()
    player1_name = request.form["player1-name"]
    player1_choice = request.form["player1-choice"]
    player1 = Player(player1_name, player1_choice)

    player2_name = request.form["player2-name"]
    player2_choice = request.form["player2-choice"]
    player2 = Player(player2_name, player2_choice)

    result = game.rock_paper_scissors(player1, player2)
    session['result'] = json.dumps(result)
    return redirect(url_for("show_winner"))
