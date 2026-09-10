# --- переменные ---
name = None
age = None
good = None
attemps = 0
max = 3
names = [] # Потом сделать базу людей в баре 
ages = [] # Потом сделать базу людей в баре
# --- переменные ---

try:
    texts = {
        "ru": {
            "ask_age": f"Здрасте, введите ваш возраст для прохода в клуб у вас всего {max - attemps} попытки ",
            "letters": f"вы ввели буквы попробуйте еще раз! у вас осталось {max - attemps} попыток",
            "too_many": "Слишком много попыток пока",
            "mixed": "вы ввели цифры и буквы попробуйте еще раз",
            "too_old": "Хорошая попытка введите реальный возраст",
            "welcome": "Добро пожаловать!",
            "ask_name": "Теперь напишите ваше имя: ",
            "digits": "В вашем имени не может быть цифр только если вы не робот!",
            "success": f"Ну наконец то здрасте о великий {name} вы прошли в наш клуб в возрасте {age}",
            "neg": "Возраст не может быть отрицательным попробуйте ещё раз",
            "truth": "Вы не проходите по параметрам возраста или попробуйте ввести число больше 18\n Enter для продолжения ",
            "bye": "до свидания!",
            "not_a_number": "Вы ввели не число! Попробуйте ещё раз",
            "error1": "folder"
        },
        "en": {
            "ask_age": "Hewuu enter ur age to enter the club u have {max - attemps} attempts left: ",
            "letters": "u entered letters traiii again u have {max - attemps} attempts left",
            "too_many": "too many attemps byee bihh",
            "mixed": "u entered letters and nums try again",
            "too_old": "nice try brotha enter ur real age",
           "welcome": "WelCUM   p.s. Daniil ystrd",
            "ask_name": "enter ur name: ",
            "digits": "ur name cannot contain nums unless u r a robot!",
           "success": f"oh lord greetings great {name} you entered our club at the {age} yo",
            "neg": "Age cannot be negative, try again",
           "truth": "ure to yuoung print 0 to exit or enter num greater than 18 \n Enter for continue",
           "bye": "Baii cya",
           "not_a_number": "not a number try again",
           "error1": "folder"
        }
    }
except ValueError:
    print("folder")
# texts[lang][""]


act = input("""chooze ur lang. Выберите язык. 
1 - russian
2 english
""")
try:
    if act == "1":
        print("ru enable")
        lang = "ru"

    elif act == "2":
        print("en enable")
        lang = "en"
    else:
        print("error error error error ONLY '1' or '2'")
except ValueError:
    print("folder")

while True:
    # if (text = input(texts[lang]["ask_age"])) == ValueError:
    #     print ("ошибка")

    text = input(texts[lang]["ask_age"])

    # try:
    #     text = input(texts[lang]["ask_age"])
    # except ValueError:
        # print("Вы написали НЕ 1 или 2"

    
    bukva = False
    cifra = False
    for s in text:
        if s.isalpha():
            bukva = True
        if s.isdigit():
            cifra = True

    if bukva and cifra:
        attemps += 1
        print(texts[lang]["mixed"])
        if attemps >= max:
            print(texts[lang]["too_many"])
            break
        continue
    if bukva:
            attemps += 1
            print(f"вы ввели буквы попробуйте еще раз")
            if attemps >= max:
                print(texts[lang]["too_many"])
                break
            continue
    try:
        age = int(text)

        if age > 99:
            print("too_old")
            attemps += 1
            if attemps >= max:
                print(texts[lang]["too_many"])
                break
        elif age >= 18:
            print("Добро пожаловать!")
            name = input("Теперь напишите ваше имя ")

            bukva2 = False
            cifra2 = False
            for negr2 in name:
                if negr2.isalpha():
                    bukva2 = True
                if negr2.isdigit():
                    cifra2 = True
            if cifra2:
                attemps += 1
                print(f"В вашем имени не может быть цифр только если вы не робот! ")
                if attemps >= max:
                    print(texts[lang]["too_many"])
                    break
                continue
            if bukva2:
                print (f"Ну наконец то здрасте о великий {name} вы прошли в наш клуб в возрасте {age}")
                names.append(name)
                ages.append(age)
                break
        elif age < 0:
            print(f"Возраст не может быть отрицательным попробуйте ещё раз у вас осталось {attemps} попыток ")
            attemps += 1
            if attemps >= max:
                     print(texts[lang]["too_many"])
                     break
        elif age < 0:
            attemps += 1
            print(f"Возраст не может быть отрицательным попробуйте ещё раз")
            if attemps >= max:
                print(texts[lang]["too_many"])
                break
        else:
            attemps += 1
            if attemps >= max:
                print(texts[lang]["too_many"])
                break
            good = input(f"""Вы не проходите по параметрам возраста или пропробуйте ввести число больше 18.
                Если вы честный то напишите ноль и программа завершиться или напишите Enter чтобы еще раз ввести ваш "реальный" возраст 
                """)
            if good == "0":
                    print ("до свидания!")
                    break

    except ValueError:
        attemps += 1
        print(f"Вы ввели не число! Попробуйте ещё раз")
        if attemps >= max:
            print(texts[lang]["too_many"])
            break
