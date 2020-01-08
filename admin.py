# -*- coding: utf8 -*-

from flask import Flask, render_template, send_from_directory, session, redirect, url_for, escape, request
from flask_sqlalchemy import SQLAlchemy
from app import models, app, db
from werkzeug.utils import secure_filename
import os

@app.route('/', methods = ['GET', 'POST'])
def edit_premiers():
    #Добавление, редактирование, удаление премьер
    if 'nickname' in session:
        premiers = models.Premiere.query.all()

        if request.method == 'POST':
            new_id = request.form['new_id']
            new_name = request.form['new_name']
            new_description = "."
            new_trailer = request.form['new_trailer']

            u = models.Premiere.query.filter_by(id = new_id).first()
            u.name = new_name
            u.trailer = new_trailer
            db.session.commit()

        return render_template('premiers.html', 
                               premiers = premiers)
    else:
        return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    #Авторизация с помощью логина и пароля
    if request.method == 'POST':
        nickname = request.form['nickname']
        password = request.form['password']
        p = models.User.query.filter(models.User.nickname == nickname and models.User.password == password).all()
        if p:
            session['nickname'] = nickname
            session['password'] = password
            return redirect(url_for('edit_premiers'))
        else:
            return redirect(url_for('login'))
    return render_template('login.html')
    
@app.route('/upload', methods = ['GET', 'POST'])
def upload_film():
    #Страница загрузки фильмов в БД
    if 'nickname' in session:
        if request.method == 'POST':
            new_style = request.form['new_style']
            new_name = request.form['new_name']
            new_description = request.form['new_description']
            new_poster = request.form['new_poster']
            new_trailer = request.form['new_trailer']
            new_film = request.form['new_film']
            
            u = models.Film(style = new_style, name = new_name, description = new_description, poster = new_poster, trailer = new_trailer, film = new_film)
            db.session.add(u)
            db.session.commit()
            
        return render_template('upload_film.html')
    else:
        return redirect(url_for('login'))

@app.route('/films', methods = ['GET', 'POST'])
def edit_films():
    #Удаление и просмотр доступных фильмов
    if 'nickname' in session:
        films = models.Film.query.all()

        if request.method == 'POST':
            delete_id = request.form['new_id']
            film = models.Film.query.filter_by(id=delete_id)[0]
            print(film)
            db.session.delete(film)
            db.session.commit()
            return redirect(url_for('edit_premiers'))
            
        return render_template('film_list.html', 
                               films = films)
    else:
        return redirect(url_for('login'))

if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    app.run()