good = None
attemps = 0
max = 3



while True:
    try:
        age = int(input(f"Здрасте, введите ваш возраст для прохода в клуб у вас всего {attemps} попытки "))

        if age > 99:
            print("Хорошая попытка введите реальный возраст")
        elif age >= 18:
            print("Добро пожаловать!")
            name = input("Теперь напишите ваше имя ")
            for negr2 in name:
                if negr.isalpha():
                    bukva2 = True
                if negr.isdigit():
                    cifra2 = True
            if cifra2:
                attemps += 1
                print(f"В вашем имени не может быть букв только если вы не робот! ")
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
        else:
            good = input(f"""Вы не проходите по параметрам возраста или пропробуйте ввести число больше 18.
                Если вы честный то напишите ноль и программа завершиться или напишите Enter чтобы еще раз ввести ваш "реальный" возраст 
                у вас осталось {attemps} попыток
                """) 
            if good == "0":
                    print ("до свидания!")
                    break

            attemps += 1
            if attemps >= max:
                 print("Слишком много попыток пока")
                 break
                
                
    except ValueError:
        print("Вы ввели не число! Попробуйте ещё раз.")
