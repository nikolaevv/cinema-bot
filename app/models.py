from app import db

class Film(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    style = db.Column(db.String(255))
    #Жанр фильма
    name = db.Column(db.String(255))
    #Название фильма
    description = db.Column(db.String(255))
    #Описание фильма
    poster = db.Column(db.String(255))
    #Адрес постера фильма
    trailer = db.Column(db.String(255))
    #Адрес трейлера фильма
    film = db.Column(db.String(255))
    #Адрес фильма
    
class Premiere(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255))
    #Название фильма
    description = db.Column(db.String(255))
    #Описание фильма
    trailer = db.Column(db.String(255))
    #Адрес трейлера фильма
    
class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nickname = db.Column(db.String(64), unique = True)
    #Никнейм администратора
    password = db.Column(db.String(128))
    #Пароль администратора