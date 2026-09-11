from storage import texts, names, ages, passwrds
import bar_verification


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
    act2 = input(texts[lang]["choose_name_add_rem"])

    if act2 == "1":
        if len(names) == 0:
            print(texts[lang]["empty_bar"])
            continue

        for i in range(len(names)):
            print(texts[lang]["guest_line"].format(num=i + 1, name=names[i], age=ages[i]))

        nomer = input(texts[lang]["ask_exit_num"])
        try:
            i = int(nomer) - 1 # топ способ который позволяет сразу отсеить если юз написал буквы и цифры или только буквы
        except ValueError:
            print(texts[lang]["need_num"])
            continue

        if i < 0 or i >= len(names):
            print(texts[lang]["bad_num"])
            continue

        pwd = input(texts[lang]["ask_exit_password"])
        if pwd == passwrds[i]:
            print(texts[lang]["left_bar"].format(name=names[i]))
            names.pop(i)
            ages.pop(i)
            passwrds.pop(i)
        else:
            print(texts[lang]["wrong_password"])

    elif act2 == "2":
        bar_verification.run(lang)

    elif act2 == "3":
        if len(names) == 0:
            print(texts[lang]["empty_bar"])
        else:
            for i in range(len(names)):
                print(texts[lang]["guest_line"].format(num=i + 1, name=names[i], age=ages[i]))

    else:
        print("Вы ввели неправильную команду")
