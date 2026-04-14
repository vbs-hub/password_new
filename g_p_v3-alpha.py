import datetime as dt
import os
from random import choice, randint

from colorama import Back, Fore, Style, init

init(autoreset=True)

MY_ORANGE = "\033[48;2;255;138;24m"
MY_ORANGE_V2 = "\033[38;2;255;138;24m"
MY_WHITE = "\033[38;2;255;255;255m"
MY_YELLOW = "\033[38;2;233;238;79m"
MY_BLUE_V1 = "\033[38;2;0;49;83m"
MY_BLUE_V2 = "\033[38;2;48;213;200m"

abc = "abcdefghijklmnopqrstuvwxyz"
numbers = "1234567890"

adjectives = [
    "Silver",
    "Golden",
    "Strong",
    "Silent",
    "Happy",
    "Brave",
    "Swift",
    "Smart",
    "Cool",
    "Mighty",
    "Wild",
    "Epic",
    "Magic",
    "Royal",
    "Lucky",
]

nouns = [
    "Tiger",
    "Eagle",
    "Panda",
    "Ninja",
    "Hacker",
    "Dragon",
    "Wolf",
    "Ghost",
    "Knight",
    "Falcon",
    "Lion",
    "Storm",
    "Phoenix",
    "Rocket",
    "Alpha",
]

password = ""
file_name = "password.txt"


def save_password(password, mode="Созданный", site=""):
    genert_id = randint(1000, 9999)
    with open("password.txt", "a", encoding="utf-8") as file:
        log_entry = (
            f"ID: {genert_id} | "
            f"{dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | "
            f"Сайт: {site} - {mode} Пароль: {password}\n"
        )
        file.write(log_entry)
    print(
        f"{Fore.RED}Пароль (ID: {genert_id}){Fore.RESET} сохранен в {Fore.GREEN}{file_name}{Fore.RESET}"
    )


def show_history():
    if not os.path.exists(file_name):
        print(f"{Fore.RED}История пуста (файл не найден).{Fore.RESET}")
        return

    with open(file_name, "r", encoding="utf-8") as file:
        lines = file.readlines()
        if not lines:
            print(f"{Fore.YELLOW}В истории пока ничего нет.{Fore.RESET}")
            return

        print(f"\n{Back.BLUE}{Fore.WHITE} ПОСЛЕДНИЕ 3 ЗАПИСИ: {Back.RESET}")
        last_3 = lines[-3:]
        for line in last_3:
            print(f"{Fore.CYAN}{line.strip()}")
        print("")


def find_password_by_id(search_id):
    if not os.path.exists(file_name):
        print(f"{Fore.RED}Файл с паролями не найден.{Fore.RESET}")
        return

    with open(file_name, "r", encoding="utf-8") as file:
        found = False
        for line in file:
            if f"ID: {search_id}" in line:
                print(f"\n{Fore.GREEN}Результат поиска:{Fore.RESET}")
                print(f"{Fore.CYAN}{line.strip()}\n")
                found = True

        if not found:
            print(f"{Fore.RED}Пароль с ID {search_id} не найден.{Fore.RESET}\n")


while True:
    otvet = input(
        "Выберите вариант"
        f" ({Back.RED + Style.BRIGHT + Fore.BLACK}выход{Back.RESET}"
        f" /{MY_BLUE_V1}создать{Fore.RESET}"
        f" /{MY_BLUE_V2}сохранить{Fore.RESET}"
        f" /{Fore.GREEN}открыть{Fore.RESET}"
        f" /{MY_YELLOW}история{Fore.RESET}"
        f" /{MY_ORANGE + Fore.BLACK}поиск{Fore.RESET}{Fore.RESET + Style.RESET_ALL}): "
    ).lower()
    if otvet == "выход":
        break
    elif otvet == "поиск":
        search_id = input(f"Введите {Fore.YELLOW}ID{Fore.RESET} пароля для поиска: ")
        if search_id:
            find_password_by_id(search_id)
        else:
            print(f"{Fore.RED}Вы не ввели ID!{Fore.RESET}")
    elif otvet == "история":
        show_history()
    elif otvet == "сохранить":
        site_on = input("Пароль для сайта: ")
        if site_on == "да":
            site_input = input("Домен сайта: ")
            password_saved = input(f"Введите {Fore.RED}пароль{Fore.RESET}: ")
            if password_saved:
                print(
                    f"{MY_ORANGE_V2}Сайт{Fore.RESET}: {MY_BLUE_V2}{site_input}{Fore.RESET} - {Fore.RED}Пароль{Fore.RESET}: {Fore.GREEN}{password_saved}{Fore.RESET}"
                )
                save_password(password_saved, mode="Сохраненный", site=site_input)
            else:
                print(f"{Fore.RED}Пусто!{Fore.RESET}")
        elif site_on == "нет":
            password_saved = input(f"Введите {Fore.RED}пароль{Fore.RESET}: ")
            if password_saved:
                print(
                    f"{Fore.RED}Пароль{Fore.RESET}: {Fore.GREEN}{password_saved}{Fore.RESET}"
                )
                save_password(password_saved, mode="Сохраненный", site="НЕТ")
            else:
                print(f"{Fore.RED}Пусто!{Fore.RESET}")
        else:
            print(
                f"{Fore.RED}Неверный ввод{Fore.RESET}. Пожалуйста, введите '{Fore.GREEN}да{Fore.RESET}' или '{Fore.RED}нет{Fore.RESET}'"
            )

    elif otvet == "открыть":
        print(f"{Fore.GREEN}Открытие файла...{Fore.RESET}\n")
        if os.path.exists(file_name):
            os.startfile(file_name)
            print(f"{Fore.GREEN}Файл{Fore.RESET} успешно открыт.")
        else:
            print(
                f"{Fore.GREEN}Файл{Fore.RESET} {Fore.RED}{file_name}{Fore.RESET} не найден или пока не создан (чтобы он появился, сначала создайте или сохраните пароль)."
            )
    elif otvet == "создать":
        site_on = input("Пароль для сайта: ")
        if site_on == "да":
            site_input = input("Домен сайта: ")

            print("Выберите тип генерации 1 - случайный пароль, 2 - умный пароль")
            gen_type = input("Ваш выбор (1/2): ")

            if gen_type == "2":

                def generate_smart_password():
                    adj = choice(adjectives).capitalize()  # С большой буквы
                    noun = choice(nouns).capitalize()
                    num = randint(10, 99)  # Добавляем число в конце
                    return f"{adj}{noun}{num}"

                password = generate_smart_password()
                if password:
                    print(
                        f"{MY_ORANGE_V2}Сайт{Fore.RESET}: {MY_BLUE_V2}{site_input}{Fore.RESET} - {Fore.RED}Пароль{Fore.RESET}: {Fore.GREEN}{password}{Fore.RESET}"
                    )
                    save_password(password, mode="Созданый(умный)", site=site_input)
            elif gen_type == "1":
                sinca_password = int(
                    input(f"Сколько символов в {Fore.RED}пароле{Fore.RESET}: ")
                )
                numbers_in_password = input(
                    f"Включить {Fore.BLUE}цифры{Fore.RESET} в {Fore.RED}пароле{Fore.RESET} ({Fore.GREEN}д{Fore.RESET}/{Fore.RED}н{Fore.RESET}): "
                ).lower()

                def generate_password_not_numbers(sinca):
                    result = ""
                    for _ in range(sinca):
                        result += choice(abc)
                    return result

                def generate_password(sinca):
                    result = ""
                    for _ in range(sinca):
                        result += choice(abc + numbers)
                    return result

                if numbers_in_password == "д":
                    password = generate_password(sinca_password)
                elif numbers_in_password == "н":
                    password = generate_password_not_numbers(sinca_password)
                else:
                    print(
                        f"{Fore.RED}Неверный ввод{Fore.RESET}. Пожалуйста, введите '{Fore.GREEN}д{Fore.RESET}' или '{Fore.RED}н{Fore.RESET}'"
                    )

                if password:
                    print(
                        f"{MY_ORANGE_V2}Сайт{Fore.RESET}: {MY_BLUE_V2}{site_input}{Fore.RESET} - {Fore.RED}Пароль{Fore.RESET}: {Fore.GREEN}{password}{Fore.RESET}"
                    )

                    save_password(password, site=site_input)
                else:
                    print(
                        f"{Fore.RED}Неверный ввод{Fore.RESET}. Пожалуйста, выберите один из вариантов."
                    )
        elif site_on == "нет":
            print("Выберите тип генерации 1 - случайный пароль, 2 - умный пароль")
            gen_type = input("Ваш выбор (1/2): ")
            if gen_type == "2":

                def generate_smart_password():
                    adj = choice(adjectives).capitalize()  # С большой буквы
                    noun = choice(nouns).capitalize()
                    num = randint(10, 99)  # Добавляем число в конце
                    return f"{adj}{noun}{num}"

                password = generate_smart_password()
                if password:
                    print(
                        f"{MY_ORANGE_V2}Сайт{Fore.RESET}: {MY_BLUE_V2}Нету{Fore.RESET} - {Fore.RED}Пароль{Fore.RESET}: {Fore.GREEN}{password}{Fore.RESET}"
                    )

                    save_password(password, mode="Созданый(умный)", site="Нету")
                else:
                    print(
                        f"{Fore.RED}Неверный ввод{Fore.RESET}. Пожалуйста, выберите один из вариантов."
                    )
            elif gen_type == "1":
                sinca_password = int(
                    input(f"Сколько символов в {Fore.RED}пароле{Fore.RESET}: ")
                )
                numbers_in_password = input(
                    f"Включить {Fore.BLUE}цифры{Fore.RESET} в {Fore.RED}пароле{Fore.RESET} ({Fore.GREEN}д{Fore.RESET}/{Fore.RED}н{Fore.RESET}): "
                ).lower()

                def generate_password_not_numbers(sinca):
                    result = ""
                    for _ in range(sinca):
                        result += choice(abc)
                    return result

                def generate_password(sinca):
                    result = ""
                    for _ in range(sinca):
                        result += choice(abc + numbers)
                    return result

                if numbers_in_password == "д":
                    password = generate_password(sinca_password)
                elif numbers_in_password == "н":
                    password = generate_password_not_numbers(sinca_password)
                else:
                    print(
                        f"{Fore.RED}Неверный ввод{Fore.RESET}. Пожалуйста, введите '{Fore.GREEN}д{Fore.RESET}' или '{Fore.RED}н{Fore.RESET}'"
                    )

                if password:
                    print(
                        f"{MY_ORANGE_V2}Сайт{Fore.RESET}: {MY_BLUE_V2}Нету{Fore.RESET} - {Fore.RED}Пароль{Fore.RESET}: {Fore.GREEN}{password}{Fore.RESET}"
                    )

                    save_password(password, site="Нету")
                else:
                    print(
                        f"{Fore.RED}Неверный ввод{Fore.RESET}. Пожалуйста, введите '{Fore.GREEN}д{Fore.RESET}' или '{Fore.RED}н{Fore.RESET}'"
                    )
    else:
        print(
            f"{Fore.RED}Неверный ввод{Fore.RESET}. Пожалуйста, введите '{Fore.GREEN}д{Fore.RESET}' или '{Fore.RED}н{Fore.RESET}'"
        )
