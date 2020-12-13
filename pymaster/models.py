from pymaster.ext.database import db
from sqlalchemy_serializer import SerializerMixin


class Pstats(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    img_player = db.Column(db.String(140))
    name = db.Column(db.String(140))
    team = db.Column(db.String(140))
    nation = db.Column(db.String(140))
    league = db.Column(db.String(140))
    positions = db.Column(db.String(140))
    Age = db.Column(db.String(140))
    Stronger_Foot = db.Column(db.String(140))
    Height = db.Column(db.String(140))
    Weight = db.Column(db.String(140))
    Position = db.Column(db.String(140))
    special_abilities = db.Column(db.String(140))
    attack = db.Column(db.String(140))
    defence = db.Column(db.String(140))
    balance = db.Column(db.String(140))
    stamina = db.Column(db.String(140))
    speed = db.Column(db.String(140))
    acceleration = db.Column(db.String(140))
    response = db.Column(db.String(140))
    agility = db.Column(db.String(140))
    dribble_accuracy = db.Column(db.String(140))
    dribble_speed = db.Column(db.String(140))
    short_pass_accuracy = db.Column(db.String(140))
    short_pass_speed = db.Column(db.String(140))
    long_pass_accuracy = db.Column(db.String(140))
    long_pass_speed = db.Column(db.String(140))
    shot_accuracy = db.Column(db.String(140))
    shot_power = db.Column(db.String(140))
    shot_technique = db.Column(db.String(140))
    free_kick_accuracy = db.Column(db.String(140))
    swerve = db.Column(db.String(140))
    heading = db.Column(db.String(140))
    jump = db.Column(db.String(140))
    technique = db.Column(db.String(140))
    aggression = db.Column(db.String(140))
    mentality = db.Column(db.String(140))

    gk_skills = db.Column(db.String(140))
    team_work = db.Column(db.String(140))
    consistency = db.Column(db.String(140))
    condition = db.Column(db.String(140))
    weak_foot_accuracy = db.Column(db.String(140))
    weak_foot_frequency = db.Column(db.String(140))

    free_kick_style = db.Column(db.String(140))
    drop_kick_style = db.Column(db.String(140))
    dribbling_style = db.Column(db.String(140))
    penalty_style = db.Column(db.String(140))
    injury = db.Column(db.String(140))


class Player(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(140))
    selfLink = db.Column(db.String(140))
    name = db.Column(db.String(140))
    team = db.Column(db.String(140))
    nation = db.Column(db.String(140))
    pos = db.Column(db.String(140))
    over = db.Column(db.String(140))


class User(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(140))
    password = db.Column(db.String(512))