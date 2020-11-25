from flask import abort, render_template, jsonify, request
from pymaster.models import Player
from flask_simplelogin import login_required


#@login_required
def index():
    return render_template("index.html")
    #return render_template("index.html")


def player(player_id):
    player = Player.query.filter_by(id=player_id).first() or abort(
        404, "Jogador não encontrado"
    )
    return render_template("player.html", player=player)

     
