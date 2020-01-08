# -*- coding: utf8 -*-

import vk_api
import emojis
import json
import time
from random import random, randint
from app import db, models, app
import random

vk = vk_api.VkApi(token = YOUR_TOKEM)
vk._auth_token()

def get_button(label, color, payload=""):
    return {
        "action": {
            "type": "text",
            "payload": json.dumps(payload),
            "label": label
        },
        "color": color
    }

main_keyboard = {
    "one_time": False,
    "buttons": [
    [
    get_button(label=emojis.encode("Найти хороший фильм :clapper:"), color="positive")],
    [get_button(label=emojis.encode("Что в кинотеатре? :movie_camera:"), color="default")],
    ]
}

main_keyboard = json.dumps(main_keyboard, ensure_ascii=False).encode('utf-8')
main_keyboard = str(main_keyboard.decode('utf-8'))

advice_keyboard = {
    "one_time": False,
    "buttons": [
    [
    get_button(label=emojis.encode("Драмы :disappointed_relieved:"), color="primary"),
    get_button(label=emojis.encode("Комедии :smile:"), color="primary")],
        
    [get_button(label=emojis.encode("Детективы :mag:"), color="primary"),
     get_button(label=emojis.encode("Исторические :hourglass_flowing_sand:"), color="primary")
    ],
        
    [get_button(label=emojis.encode("Боевики :facepunch:"), color="primary"),
     get_button(label=emojis.encode("Мелодрамы :broken_heart:"), color="primary")
    ],
        
    [get_button(label=emojis.encode("Ужасы :ghost:"), color="primary"),
     get_button(label=emojis.encode("Фантастика :telescope:"), color="primary")
    ],
        
    [get_button(label=emojis.encode("Триллеры :see_no_evil:"), color="primary"),
     get_button(label=emojis.encode("Назад :leftwards_arrow_with_hook:"), color="default")
    ],
        
    ]
}

advice_keyboard = json.dumps(advice_keyboard, ensure_ascii=False).encode('utf-8')
advice_keyboard = str(advice_keyboard.decode('utf-8'))

while True:
    try:
        #Получаем сообщения и проверяем новые
        messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unread"})
        if messages["count"] >= 1:
            id = messages["items"][0]["last_message"]["from_id"]
            body = messages["items"][0]["last_message"]["text"]

            #Выводит приветственное сообщение в ответ на "старт" и главную клавиатуру
            if body.lower() == "начать":
                vk.method("messages.send", {"peer_id": id, "message": emojis.encode(':wave: Привет! В нашем сообществе ты сможешь познакомиться со всеми новинками, первым узнавать новости из мира кино и поугарать с наших мемов. \n\n:robot: Наш бот поможет подобрать фильм на вечер, узнать о предстоящих новинках и многое другое. Скорее выбирай нужный раздел! \n\nТы в команде!'), "keyboard": main_keyboard, "random_id": randint(0, 1000)})

            elif body.lower() == emojis.encode("найти хороший фильм :clapper:"):
                vk.method("messages.send", {"peer_id": id, "message": "Выбери жанр:", "keyboard": advice_keyboard, "random_id": randint(0, 1000)})

            elif body.lower() == emojis.encode("драмы :disappointed_relieved:"):
                u = models.Film.query.filter(models.Film.style == "Драмы").all()
                print(u)
                p = random.choice(u)
                film_attachment = p.poster + "," + p.trailer + "," + p.film
                print(film_attachment)
                vk.method("messages.send", {"peer_id": id, "message": (p.name + "\n\n" + p.description), "attachment": film_attachment, "random_id": randint(0, 1000)})

            elif body.lower() == emojis.encode("комедии :smile:"):
                u = models.Film.query.filter(models.Film.style == "Комедии").all()
                print(u)
                p = random.choice(u)
                film_attachment = p.poster + "," + p.trailer + "," + p.film
                print(film_attachment)
                vk.method("messages.send", {"peer_id": id, "message": (p.name + "\n\n" + p.description), "attachment": film_attachment, "random_id": randint(0, 1000)})

            elif body.lower() == emojis.encode("детективы :mag:"):
                u = models.Film.query.filter(models.Film.style == "Детективы").all()
                print(u)
                p = random.choice(u)
                film_attachment = p.poster + "," + p.trailer + "," + p.film
                print(film_attachment)
                vk.method("messages.send", {"peer_id": id, "message": (p.name + "\n\n" + p.description), "attachment": film_attachment, "random_id": randint(0, 1000)})

            elif body.lower() == emojis.encode("исторические :hourglass_flowing_sand:"):
                u = models.Film.query.filter(models.Film.style == "Исторические").all()
                print(u)
                p = random.choice(u)
                film_attachment = p.poster + "," + p.trailer + "," + p.film
                print(film_attachment)
                vk.method("messages.send", {"peer_id": id, "message": (p.name + "\n\n" + p.description), "attachment": film_attachment, "random_id": randint(0, 1000)})

            elif body.lower() == emojis.encode("боевики :facepunch:"):
                u = models.Film.query.filter(models.Film.style == "Боевики").all()
                print(u)
                p = random.choice(u)
                film_attachment = p.poster + "," + p.trailer + "," + p.film
                print(film_attachment)
                vk.method("messages.send", {"peer_id": id, "message": (p.name + "\n\n" + p.description), "attachment": film_attachment, "random_id": randint(0, 1000)})

            elif body.lower() == emojis.encode("мелодрамы :broken_heart:"):
                u = models.Film.query.filter(models.Film.style == "Мелодрамы").all()
                print(u)
                p = random.choice(u)
                film_attachment = p.poster + "," + p.trailer + "," + p.film
                print(film_attachment)
                vk.method("messages.send", {"peer_id": id, "message": (p.name + "\n\n" + p.description), "attachment": film_attachment, "random_id": randint(0, 1000)})

            elif body.lower() == emojis.encode("ужасы :ghost:"):
                u = models.Film.query.filter(models.Film.style == "Ужасы").all()
                print(u)
                p = random.choice(u)
                film_attachment = p.poster + "," + p.trailer + "," + p.film
                print(film_attachment)
                vk.method("messages.send", {"peer_id": id, "message": (p.name + "\n\n" + p.description), "attachment": film_attachment, "random_id": randint(0, 1000)})

            elif body.lower() == emojis.encode("фантастика :telescope:"):
                u = models.Film.query.filter(models.Film.style == "Фантастика").all()
                print(u)
                p = random.choice(u)
                film_attachment = p.poster + "," + p.trailer + "," + p.film
                print(film_attachment)
                vk.method("messages.send", {"peer_id": id, "message": (p.name + "\n\n" + p.description), "attachment": film_attachment, "random_id": randint(0, 1000)})

            elif body.lower() == emojis.encode("триллеры :see_no_evil:"):
                u = models.Film.query.filter(models.Film.style == "Триллеры").all()
                print(u)
                p = random.choice(u)
                film_attachment = p.poster + "," + p.trailer + "," + p.film
                print(film_attachment)
                vk.method("messages.send", {"peer_id": id, "message": (p.name + "\n\n" + p.description), "attachment": film_attachment, "random_id": randint(0, 1000)})

            elif body.lower() == emojis.encode("назад :leftwards_arrow_with_hook:"):
                vk.method("messages.send", {"peer_id": id, "message": "Возвращаю...", "keyboard": main_keyboard, "random_id": randint(0, 1000)})

            elif body.lower() == emojis.encode("что в кинотеатре? :movie_camera:"):
                premiers = models.Premiere.query.all()
                print(premiers)
                names = []
                trailers = ""
                for p in premiers:
                    names.append(p.name)
                    trailers = trailers + p.trailer + ","
                first_premiere = names[0]
                second_premiere = names[1]
                third_premiere = names[2]
                fourth_premiere = names[3]
                fivth_premiere = names[4]
                vk.method("messages.send", {"peer_id": id, "message": ("1. " + first_premiere + "\n" + "2. " + second_premiere + "\n" + "3. " + third_premiere + "\n" + "4. " + fourth_premiere + "\n" + "5. " + fivth_premiere), "attachment": trailers, "random_id": randint(0, 1000)})


        time.sleep(1)
        
    except Exception as e:
        with open('exceptions.txt', 'a') as log:
            print(e, file = log)