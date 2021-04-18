import time
import os


__author__ = "Денис Давыдов"
name = input("Введите имя: ").rstrip().lstrip().title()
step = ""


def custom_print(text):
    if os.name == "nt":
        print(text.replace("\033[31m", "").replace("\033[32m", "").replace("\033[0m", "").replace("\033[34m", ""))
    else:
        print(text)


def exit():
    custom_print("Будем ждать вас снова")
    quit()


def check_exit_or_pause(var):
    if var == "exit":
        return exit()
    elif var == "pause":
        return wait_game()


def wait_game():
    a = input("Что бы продолжить игру нажмите Enter...")
    if a.strip() == "":
        return step()
    else:
        return wait_game()


def instructions():
    custom_print("Если вы хотите поставить игру на паузу, введите в консоль «pause»")
    custom_print("Для выхода из игры, введите в консоль «exit»")
    want_to_start()


def check_want_to_start():
    global step
    step = want_to_start
    print("Вы готовы начать игру?", "1)Да", sep="\n")
    custom_print("Введите номер ответа")
    var = input()
    check_exit_or_pause(var)
    if var == "1" or var.lower() == "да":
        return start_story()
    else:
        custom_print("Ошибка ввода. Попробуйте ещё раз")
        check_want_to_start()


def want_to_start():
    global step
    step = want_to_start
    custom_print(f"Добрый день {name}, вам придёться раследовать катастрофу")
    custom_print("Атомный ледокол «Северный ветер» застревает во льду")
    custom_print("Связь с экипажем потеряна!")
    custom_print("Вам, обычному метеорологу с полярной станции, предстоит провести операцию по спасению экипажа")
    return check_want_to_start()


def start_story():
    global step
    step = start_story
    custom_print(
        f"\033[31mСообщение из Москвы:\033[0m {name}, Добрый день. У нас возникла проблема с ледоколом «Северный ветер»")
    custom_print("Вам предстоит выяснить что случилось")
    custom_print("Отправляйтесь в координаты -79.705507, -32.219695, это последнее место где он выходил на связь")
    custom_print("Отправляйтесь быстрее, экипаж в опасности!")
    time.sleep(5)
    start_walk_to_ship()


def start_walk_to_ship():
    global step
    step = start_walk_to_ship
    custom_print("\033[32mЗапись из дневника:\033[0m Я начал долгий путь до корабля")
    custom_print("Мне казалось, что путь не скончаемый и всё, что я вижу это белую мглу. Как же холодно")
    custom_print("Через несколько дней я дошёл до корабля. Он выглядел безжизненно")
    time.sleep(5)
    custom_print("\033[34mИстория:\033[0m С корабля спущена лестница, кто то пытался его покинуть")
    custom_print(
        "\033[32mЗапись из дневника:\033[0m Я решил подняться на корабль по этой шаткой лестнице, было страшно")
    time.sleep(5)
    custom_print("Рядом находится дверь с кодом, надо попробовать открыть её. О, я вижу какой-то шифр на замке")
    custom_print("Шифр: «19131608152911 121605»")
    complet = False
    attempt = 0
    while not complet and attempt < 3:
        code = input("Введите код с учётом пробела, подсказка - «Алфавит»").lower()
        check_exit_or_pause(code)
        if code.strip().lower() == "сложный код":
            complet = True
            return entered_ship_by_door()

        else:
            custom_print("Не верный код")
            attempt += 1
    search_for_a_new_enter()


def input_for_a_new_enter():
    global step
    step = input_for_a_new_enter
    var = input("Введите номер ответа: ")
    check_exit_or_pause(var)
    if var == "1" or var.lower() == "да":
        enter_ship_by_machine()
    elif var == "2" or var.lower() == "нет":
        return continue_search()
    else:
        custom_print("Не верный ввод")
        return input_for_a_new_enter()


def search_for_a_new_enter():
    global step
    step = search_for_a_new_enter
    custom_print("\033[32mДневник: \033[0mЧёрт, замок заблокирован, придётся искать новый проход")
    custom_print("Я начал обходить корабль. Я увидел трубы с машинного отделения, через них я смогу пробраться")
    custom_print("Войти через трубы?")
    custom_print("1)Да")
    custom_print("2)Нет")
    input_for_a_new_enter()


def entered_ship_by_door():
    global step
    step = entered_ship_by_door
    custom_print("\033[32mДневник: \033[0mИтак я попал на корабль. Где же может быть команда?")
    input_enter_ship_by_machine()


def input_enter_ship_by_machine():
    global step
    step = input_enter_ship_by_machine
    custom_print("Куда идти?")
    custom_print("1)На мостик")
    custom_print("2)В кают компанию")
    custom_print("3)В спасательный отсек")
    var = input()
    check_exit_or_pause(var)
    if var == "1":
        go_to_mostik()
    elif var == "2":
        go_to_kaiut_company()
    elif var == "3":
        go_to_save_otsek()
    else:
        print("Ошибка ввода")
        input_enter_ship_by_machine()


def enter_ship_by_machine():
    global step
    step = enter_ship_by_machine
    custom_print(
        "\033[32mДневник: \033[0mИтак я смог забраться на корабль, надо узнать что произошло")
    custom_print("Для начала попробую найти команду")
    input_enter_ship_by_machine()


def continue_search():
    global step
    step = continue_search
    custom_print(
        "\033[32mДневник: \033[0mЯ обощёл весь корабль. Дверь заблокирована, единственный способ попасть - трубы")
    enter_ship_by_machine()


def go_to_mostik():
    global step
    step = go_to_mostik
    custom_print("\033[32mДневник: \033[0mУ меня получилось попасть на мостик. Всё выглядит безжизненным и холодным")
    custom_print("Я увидел записку. На ней написанно:")
    custom_print("  «Часть команды отправилась на поиски помощи, другие же остались на корабле")
    custom_print("                                                                  Капитан»")
    custom_print("Если часть команды на корабле, надо их найти и спасти. Где они могут быть? Я очень долго задавался этим вопросом и решил пойти в спасательный отсек")
    go_to_otsek()


def go_to_otsek():
    global step
    step = go_to_otsek
    custom_print("Что бы попасть в отделение с отсеком, надо пройти пройти через дверь.")
    custom_print("Слава богу эта дверь была открыта. Я добежал до спасательного отсека и открыл его. Там не было команды, но были лишь тёплые трупу. Видимо я промедлил")
    custom_print("Надо связаться с базой и рассказать о находке. Пусть ищут остальных")
    end_game()


def go_to_kaiut_company():
    global step
    step = go_to_kaiut_company
    custom_print("Пока я шёл в кают компанию я услышал стук из спасательного отсека и сразу побежал туда")
    custom_print("Я добежал до отсека и открыл дверь. Там была вся команда корабля. Через несколько часов я связался со станцией и передал информацию о нахождении команды")
    end_game()

def go_to_save_otsek():
    global step
    step = go_to_save_otsek
    custom_print("Команды не было в отсеке. Они ушли за помощью. Надо связаться с базой и сказать что бы искали их на суше")
    end_game()


def end_game():
    custom_print("Спасибо за игру")
    time.sleep(60)
    quit()

instructions()
