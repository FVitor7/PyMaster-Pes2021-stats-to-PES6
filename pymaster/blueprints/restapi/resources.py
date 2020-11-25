from flask import abort, jsonify, request
from flask_restx import Resource
from flask_marshmallow import Marshmallow
import json
from pymaster.models import Player, Pstats

ma = Marshmallow()


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Player


class UserSchema2(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Pstats


class PlayerResourceStats(Resource):
    def post(self):
        posted_data = request.get_json()
        player_id = posted_data['player_id']
        players_find = Pstats.query.filter(
            Pstats.id.like('%'+player_id+'%')).limit(1).all()
        user_schema = UserSchema2(many=True)
        output_search = user_schema.dump(players_find)
        output_search2 = output_search[0]
        list_spec = output_search2["special_abilities"].split("+")

        output_search2["special_abilities"] = list_spec

        output_search2["positions"] = output_search2["positions"].replace(
            "+", ",")

        return jsonify(output_search2)

    def get(self):
        req_id = request.args.get("id")
        if req_id == None:
            req_id = ""

        players_find = Pstats.query.filter(
            Pstats.id.like('%'+req_id+'%')).limit(1).all()
        user_schema = UserSchema2(many=True)
        output_search = user_schema.dump(players_find)
        output_search2 = output_search[0]
        output_search2["special_abilities"] = output_search2["special_abilities"].replace(
            "+", ",")
        output_search2["positions"] = output_search2["positions"].replace(
            "+", ",")

        return jsonify(output_search2)


class PlayerResource(Resource):

    def get(self):
        req_name = request.args.get("name")
        if req_name == None:
            req_name = ""

        req_team = request.args.get("team")
        if req_team == None:
            req_team = ""

        req_nation = request.args.get("nation")
        if req_nation == None:
            req_nation = ""
        players_find = Player.query.filter(Player.name.like('%'+req_name+'%'), Player.team.like(
            '%'+req_team+'%'), Player.nation.like('%'+req_nation+'%')).limit(32).all()
        user_schema = UserSchema(many=True)
        output_search = user_schema.dump(players_find)
        return jsonify(output_search)


class PlayerItemResource(Resource):
    def get(self, player_id):
        player = Player.query.filter_by(id=player_id).first() or abort(404)
        return jsonify(player.to_dict())
