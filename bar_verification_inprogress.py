# --- в помощь ---
# texts[lang][""]
# .isalpha()
# .isdigit():
# .append
# .remove

# --- в помощь ---
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
            "ask_age": f"Hewuu enter ur age to enter the club u have {max - attemps} attempts left: ",
            "letters": f"u entered letters traiii again u have {max - attemps} attempts left",
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



while True:
    act = input("""chooze ur lang. Выберите язык. 
1 - russian
2 english
""")
    if act == "1":
        print("ru enable")
        lang = "ru"
        break
    elif act == "2":
        print("en enable")
        lang = "en"
        break
    else:
        print("Вы ввели неправильную команду введите только '1' или '2'")


while True:

    text = input(texts[lang]["ask_age"])

    
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
            print(texts[lang]["letters"])
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
            print(texts[lang]["welcome"])
            name = input(texts[lang]["ask_name"])

            bukva2 = False
            cifra2 = False
            for negr2 in name:
                if negr2.isalpha():
                    bukva2 = True
                if negr2.isdigit():
                    cifra2 = True
            if cifra2:
                attemps += 1
                print(texts[lang]["digits"])
                if attemps >= max:
                    print(texts[lang]["too_many"])
                    break
                continue
            if bukva2:
                print (texts[lang]["success"])
                names.append(name)
                ages.append(age)
                break
        elif age < 0:
            print(texts[lang]["neg"])
            attemps += 1
            if attemps >= max:
                     print(texts[lang]["too_many"])
                     break
        else:
            attemps += 1
            if attemps >= max:
                print(texts[lang]["too_many"])
                break
            good = input(texts[lang]["truth"])
            if good == "0":
                    print ("до свидания!")
                    break

    except ValueError:
        attemps += 1
        print(texts[lang]["not_a_number"])
        if attemps >= max:
            print(texts[lang]["too_many"])
            break
