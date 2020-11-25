from flask import Blueprint

from .views import player, index



bp = Blueprint("webui", __name__, template_folder="templates")


bp.add_url_rule("/", view_func=index)
bp.add_url_rule(
    "/api/player/<player_id>", view_func=player, endpoint="playerview"
)


def init_app(app):
    app.register_blueprint(bp)
