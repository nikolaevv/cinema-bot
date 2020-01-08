# -*- coding: utf8 -*-

import vk_api
import time
from app import db, models, app

vk = vk_api.VkApi(login = YOUR_LOGIN, password = YOUR_PASSWORD)
vk.auth()
#Авторизация через пользователя

while True:
    try:
        posts = vk.method("wall.get", {"owner_id": "YOUR_ID", "offset": 1, "filter": "all", "count": 20})
        #Получаем посты
        for post in posts:
            text = posts["items"][0]["text"]
            #Получаем текст поста
            if text.find("#Кино") != -1:
                p = models.Film.query.filter(models.Film.description == text).all()
                if not p:
                    #Проверка наличия идентичной записи в БД
                    poster = ""
                    film = ""
                    trailer = ""
                    style = ""
                    if text.find("драма") != -1:
                        style = "Драмы"
                    elif text.find("комедия") != -1:
                        style = "Комедии"
                    elif text.find("детектив") != -1:
                        style = "Детективы"
                    elif text.find("исторический") != -1:
                        style = "Исторические"
                    elif text.find("боевик") != -1:
                        style = "Боевики"
                    elif text.find("мелодрама") != -1:
                        style = "Мелодрамы"
                    elif text.find("ужасы") != -1:
                        style = "Ужасы"
                    elif text.find("фантастика") != -1:
                        style = "Фантастика"
                    elif text.find("триллер") != -1:
                        style = "Триллеры"
                    #Определение жанра фильма
                    attachments = posts["items"][0]["attachments"]
                    #Получаем вложения поста
                    for att in attachments:

                        if att["type"] == "photo":
                            owner_id = att["photo"]["owner_id"]
                            media_id = att["photo"]["id"]
                            poster = "photo" + str(owner_id) + "_" + str(media_id)

                        if att["type"] == "video":
                            if att["video"]["duration"] <= 300:
                                #Если длительность меньше или равна 300 секунд, то это трейлер
                                owner_id = att["video"]["owner_id"]
                                media_id = att["video"]["id"]
                                trailer = "video" + str(owner_id) + "_" + str(media_id)

                            if att["video"]["duration"] > 300:
                                #Если длительность больше 300 секунд, это фильм
                                owner_id = att["video"]["owner_id"]
                                media_id = att["video"]["id"]
                                film = "video" + str(owner_id) + "_" + str(media_id)

                    u = models.Film(style = style, name = " ", description = text, poster = poster, trailer = trailer, film = film)
                    db.session.add(u)
                    db.session.commit()    

        time.sleep(60)
        
    except Exception as e:
        with open('exceptions_checker.txt', 'a') as log:
            print(e, file = log)