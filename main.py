


good = None
attemps = 0
max = 3



while True:
    text = input(f"Здрасте, введите ваш возраст для прохода в клуб у вас всего {max - attemps} попытки ")

    if text.isalpha():
        attemps += 1
        print(f"вы ввели буквы попробуйте еще раз! у вас осталось {max - attemps} попыток")
        if attemps >= max:
            print("Слишком много попыток пока")
            break
        continue

    bukva = False
    cifra = False
    for s in text:
        if s.isalpha():
            bukva = True
        if s.isdigit():
            cifra = True

    if bukva and cifra:
        attemps += 1
        print(f"вы ввели цифры и буквы попробуйте еще раз")
        if attemps >= max:
            print("Слишком много попыток пока")
            break
        continue
    if bukva:
            attemps += 1
            print(f"вы ввели буквы попробуйте еще раз")
            if attemps >= max:
                print("Слишком много попыток пока")
                break
            continue
    try:
        age = int(text)

        if age > 99:
            print("Хорошая попытка введите реальный возраст")
            attemps += 1
            if attemps >= max:
                print("Слишком много попыток пока")
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
                    print("Слишком много попыток пока")
                    break
                continue
            if bukva2:
                print (f"Ну наконец то здрасте о великий {name} вы прошли в наш клуб в возрасте {age}")
                break
        elif age < 0:
            print(f"Возраст не может быть отрицательным попробуйте ещё раз у вас осталось {attemps} попыток ")
            attemps += 1
            if attemps >= max:
                     print("Слишком много попыток пока")
                     break
        elif age < 0:
            attemps += 1
            print(f"Возраст не может быть отрицательным попробуйте ещё раз")
            if attemps >= max:
                print("Слишком много попыток пока")
                break
        else:
            attemps += 1
            if attemps >= max:
                print("Слишком много попыток пока")
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
            print("Слишком много попыток пока")
            break
