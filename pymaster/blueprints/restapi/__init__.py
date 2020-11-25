from flask import Blueprint
from flask_restx import Api, fields

from .resources import PlayerItemResource, PlayerResource, PlayerResourceStats

bp = Blueprint("restapi", __name__, url_prefix="/api/")


api = Api(bp, doc='/', version='1.0', title='PesMaster Database API',
    description="Uma API com o banco de dados do PES2021 convertido para PES6\n\nDesenvolvido por: Fábio Vitor \n\nGithub: https://github.com/FVitor7\nemail: fabvitor2010@gmail.com\n\nPara acessar a api vá para a url: http://localhost:5000/api/v1/")


ns = api.namespace("players", description="API  operations")

player = api.model('API', {
    "id": fields.Integer(readonly=True, description='Necessário para identificar o jogador'),
    "image": fields.String(required=True, description='URL da imagem do jogador'),
    "name": fields.String(required=True, description='Nome do Jogador'),
    "nation": fields.String(required=True, description='Nacionalidade do Jogador'),
    "over": fields.String(required=True, description='Overall do Jogador'),
    "pos": fields.String(required=True, description='Posição do Jogador'),
    "selfLink": fields.String(required=True, description='Link externo do Jogador'),
    "team": fields.String(required=True, description='Time do Jogador'),
})



def init_app(app):
    app.register_blueprint(bp)
    api.add_resource(PlayerResource, "/v1/")
    api.add_resource(PlayerItemResource, "/v1/<player_id>")
    api.add_resource(PlayerResourceStats, "/v1/stats/")
    
