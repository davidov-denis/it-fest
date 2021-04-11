import time


name = input("Введите имя: ").rstrip().lstrip().title()
step = ""
# \033[31m - красный
# \033[32m - зелёный
# \033[0m - отмена
# «»


def exit():
    print("Будем ждать вас снова")
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
    print("Если вы хотите поставить игру на паузу, введите в консоль «pause»")
    print("Для выхода из игры, введите в консоль «exit»")
    want_to_start()


def check_want_to_start():
    global step
    step = want_to_start
    print("Вы готовы начать игру?", "1)Да", sep="\n")
    print("Введите номер ответа")
    var = input()
    check_exit_or_pause(var)
    if var == "1" or var.lower() == "да":
        return start_story()
    else:
        print("Ошибка ввода. Попробуйте ещё раз")
        check_want_to_start()


def want_to_start():
    global step
    step = want_to_start
    print(f"Добрый день {name}, вам придёться раследовать катастрофу")
    print("Атомный ледокол «Северный ветер» застревает во льду")
    print("Связь с экипажем потеряна!")
    print("Вам, обычному метеорологу с полярной станции, предстоит провести операцию по спасению экипажа")
    return check_want_to_start()


def start_story():
    global step
    step = start_story
    print(f"\033[31mСообщение из Москвы:\033[0m {name}, Добрый день. У нас возникла проблема с ледоколом «Северный ветер»")
    print("Вам предстоит выяснить что случилось")
    print("Отправляйтесь в координаты -79.705507, -32.219695, это последнее место где он выходил на связь")
    print("Отправляйтесь быстрее, экипаж в опасности!")
    time.sleep(5)
    start_walk_to_ship()


def start_walk_to_ship():
    global step
    step = start_walk_to_ship
    print("\033[32mЗапись из дневника:\033[0m Я начал долгий путь до корабля",
          "Мне казалось, что путь не скончаемый и всё, что я вижу это белую мглу. Как же холодно", sep="\n")
    print("Через несколько дней я дошёл до корабля. Он выглядел безжизненно")
    time.sleep(5)
    print("\033[34mИстория:\033[0m С корабля спущена лестница, кто то пытался его покинуть")
    print("\033[32mЗапись из дневника:\033[0m Я решил подняться на корабль по этой шаткой лестнице, было страшно")
    time.sleep(5)
    print("Рядом находится дверь с кодом, надо попробовать открыть её. О, я вижу какой-то шифр на замке")
    print("Шифр: «19131608152911 121605»")
    complet = False
    attempt = 0
    while not complet and attempt < 3:
        code = input("Введите код с учётом пробела, подсказка - «Алфавит»").lower()
        check_exit_or_pause(code)
        if code.strip().lower() == "сложный код":
            complet = True
            entered_ship_by_door()
        else:
            print("Не верный код")
            attempt += 1
    print("Чёрт, не получилось открыть дверь, придётся искать новый вход")
    search_for_a_new_enter()


def input_for_a_new_enter():
    var = input("Введите номер ответа")
    check_exit_or_pause(var)
    if var == "1":
        enter_ship_by_machine()
    elif var == "2":
        return continue_search()
    else:
        print("Не верный ввод")
        return input_for_a_new_enter()


def search_for_a_new_enter():
    global step
    step = search_for_a_new_enter
    print("\033[32mДневник: \033[0mЧёрт, замок заблокирован, придётся искать новый проход")
    print("Я начал обходить корабль. Я увидел трубы с машинного отделения, через них я смогу пробраться")
    print("Войти через трубы?", "1)Да", "2)Нет")


def entered_ship_by_door():
    pass


def enter_ship_by_machine():
    pass


def continue_search():
    print("\033[32mДневник: \033[0mЯ обощёл весь корабль. Дверь заблокирована, единственный способ попасть - трубы")
    print("")


instructions()
